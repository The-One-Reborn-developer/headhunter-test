from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from app.database.models.base import Base


class RSSSources(Base):
    __tablename__ = 'rss_sources'

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped['User'] = relationship('User', back_populates='rss_sources')