from typing import Sequence

from sqlalchemy import select
from sqlalchemy import Result

from sqlalchemy.orm import joinedload
from sqlalchemy.orm import selectinload

from models import db
from models import Cat
from models import Phrase


def create_cat_user(cat_name: str):
    cat = Cat(name=cat_name)    

    db.session.add(cat)
    db.session.commit()
    return cat

    
def get_cat_by_id(cat_id: int):
    return Cat.query.get_or_404(
        cat_id,
        f"Not fount cat :("
    )


def get_cat_and_his_facts_by_id(cat_id:int):

    stmt = (
        select(Cat)
        .where(cat_id==Cat.id)
        .options(selectinload(Cat.phrases))
    )

    result: Result = db.session.execute(stmt)
    cat_facts = result.scalar_one_or_none()
    return cat_facts

        
def get_all_cats():
    return Cat.query.all()
    
    
def get_facts_of_cat(cat: Cat) -> Sequence[Phrase]:
    stmt = (
        select(Phrase)
        .where(Phrase.cat_id == cat.id)
        .order_by(Phrase.id)
    )

    result: Result = db.session.execute(stmt)
    facts = result.scalars().all()
    return facts



