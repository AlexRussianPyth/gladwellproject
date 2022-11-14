from pydantic import BaseSettings, Field


class DotEnvMixin(BaseSettings):
    """Миксин, который позволяет настройкам работать с переменными окружения"""

    class Config:
        env_file = ".env"


class PostgresSettings(DotEnvMixin):
    """Настройки для БД PostgreSQL"""

    user: str = Field(..., env="POSTGRES_USER")
    password: str = Field(..., env="POSTGRES_PASSWORD")
    database: str = Field(..., env="POSTGRES_DB")
    host: str = Field(..., env="POSTGRES_HOST")
    port: str = Field(..., env="POSTGRES_PORT")

    @property
    def get_alchemy_engine_url(self):
        base = "postgresql+psycopg2://"
        return f"{base}{self.user}:{self.password}@{self.host}/{self.database}"


class Settings(DotEnvMixin):
    postgres: PostgresSettings = PostgresSettings()


settings = Settings()
