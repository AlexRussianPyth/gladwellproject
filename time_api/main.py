from src.db.alchemy_engine import create_alchemy_engine
from src.core.config import settings


engine = create_alchemy_engine(settings.postgres.get_alchemy_engine_url)

print(engine)
