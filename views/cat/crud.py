from models import db
from models import Cat



def create_cat_user(cat_name: str):
    cat = Cat(name=cat_name)    

    db.session.add(cat)
    db.session.commit()

    
def get_cat_by_id(cat_id: int):
    return Cat.query.get_or_404(
        cat_id,
        f"Not fount cat :("
    )

        
def get_all_cats():
    return Cat.query.all()

    
    
    
    
    

    