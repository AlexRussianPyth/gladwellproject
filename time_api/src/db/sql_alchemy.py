from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


def create_alchemy_engine(database_url: str, logs: bool = False):
    """Создаст Engine для SQL Alchemy"""
    engine = create_engine(database_url, echo=logs)
    engine.connect()

    return engine


def recreate_tables(base, engine) -> None:
    """Пересоздаем все базы"""
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)


def get_base():
    """Возвращаем декларативный базовый класс"""
    return declarative_base()


Base = get_base()
