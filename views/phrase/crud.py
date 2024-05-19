from models import db
from models import Phrase

def get_all_phrases() -> list[Phrase]:
    return Phrase.query.all()

    
def get_phrase_by_id(phrase_id: int) -> Phrase:
    return Phrase.query.get_or_404(
        phrase_id,
        f"this phrase not found"
    )

    
def create_phrase(phras: str, cat_id: int) -> Phrase:
    phrase = Phrase(
        str_phrase=phras,
        cat_id=cat_id,
    )
    db.session.add(phrase)
    db.session.commit()
    return phrase

