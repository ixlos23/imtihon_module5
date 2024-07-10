from datetime import datetime
from enum import Enum

from sqlalchemy import BigInteger, VARCHAR, Enum as alEnum, Column, DateTime, TEXT, DECIMAL, SMALLINT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr, relationship


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):  # noqa
        return cls.__name__.lower() + 's'


class CreatedModel(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)


class User(CreatedModel):
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    full_name: Mapped[str] = mapped_column(VARCHAR(255))
    phone_number: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    is_admin: Mapped[bool] = mapped_column(default=False)