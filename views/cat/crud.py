from typing import Sequence
from models import db
from models import Cat
from models import Phrase
from sqlalchemy import Result, select



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