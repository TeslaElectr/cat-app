from sqlalchemy import Column
from sqlalchemy import String

from .database import db



class Cat(db.Model):
    name = Column(
        String,
        nullable=False,
        unique=True
    )
    