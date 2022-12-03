from pydantic import BaseSettings, Field


class DotEnvMixin(BaseSettings):
    """Миксин, который позволяет настройкам работать с переменными окружения"""

    class Config:
        env_file = ".env"


class PostgresSettings(DotEnvMixin):
    """Настройки для БД PostgreSQL"""

    user: str = Field("admin", env="POSTGRES_USER")
    password: str = Field("admin", env="POSTGRES_PASSWORD")
    database: str = Field("gladwell", env="POSTGRES_DB")
    host: str = Field("localhost", env="POSTGRES_HOST")
    port: str = Field(5432, env="POSTGRES_PORT")

    @property
    def get_alchemy_engine_url(self):
        base = "postgresql+asyncpg://"
        return (
            f"{base}{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        )


class SqlAlchemySettings(DotEnvMixin):
    echo: bool = Field(True, env="ECHO")


class FakeDataGeneratorSettings(DotEnvMixin):
    num_users: int = Field(40, env="NUM_USERS")
    max_goals_per_user: int = Field(5, env="MAX_GOALS_PER_USER")
    max_timeunits_per_goal: int = Field(30, env="MAX_TIMEUNITS_PER_GOAL")


class Settings(DotEnvMixin):
    postgres: PostgresSettings = PostgresSettings()
    alchemy: SqlAlchemySettings = SqlAlchemySettings()
    fakedata: FakeDataGeneratorSettings = FakeDataGeneratorSettings()


settings = Settings()
