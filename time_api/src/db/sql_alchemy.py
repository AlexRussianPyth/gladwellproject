from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.core.config import settings


def get_engine():
    """Creates async engine"""
    engine = create_async_engine(
        settings.postgres.get_alchemy_engine_url,
        echo=settings.alchemy.echo,
        future=True,
    )
    return engine


def async_session_generator(engine):
    """Creates new async session"""
    return sessionmaker(engine, class_=AsyncSession)


@asynccontextmanager
async def get_session(engine):
    """Context manager for getting and closing sessions"""
    try:
        async_session = async_session_generator(engine)
        async with async_session() as session:
            yield session
    except:
        await session.rollback()
        raise
    finally:
        await session.close()
