from src.db.sql_alchemy import create_alchemy_engine, Base, recreate_tables
from src.core.config import settings


engine = create_alchemy_engine(settings.postgres.get_alchemy_engine_url)

recreate_tables(Base, engine)
