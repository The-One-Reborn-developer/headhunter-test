from sqlalchemy.orm import sessionmaker

from app.database.models.engine import engine


session = sessionmaker(bind=engine)