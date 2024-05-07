from sqlalchemy import Column
from sqlalchemy import String

from sqlalchemy.orm import relationship

from .database import db


class Cat(db.Model):
    name = Column(
        String,
        nullable=False,
        unique=True
    )

    phrases = relationship(
        "Phrase",
        back_populates="cat",
    )
    