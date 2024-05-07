from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

from database import db


class Phrase(db.Model):
    str_phrase = Column(
        String,
        unique=False,
        nullable=False,
    )

    cat_id = Column(
        Integer,
        ForeignKey("cats.id"),
        nullable=False,
        unique=False,
    )

    cat = relationship(
        "Cat",
        uselist=False,
    )

    

        
    
    