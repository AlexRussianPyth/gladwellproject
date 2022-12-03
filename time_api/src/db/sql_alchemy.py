from sqlalchemy.ext.asyncio import create_async_engine

from src.core.config import settings


engine = create_async_engine(
    settings.postgres.get_alchemy_engine_url,
    echo=settings.alchemy.echo,
    future=True,
)
