from sqlalchemy import create_engine


def create_alchemy_engine(database_url: str, logs: bool = False):
    """Создаст Engine для SQL Alchemy"""
    engine = create_engine(database_url, echo=logs)
    engine.connect()

    return engine
