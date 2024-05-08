from models import db

from models import Phrase

def get_list_of_phrases() -> list[Phrase]:
    return Phrase.query.all()

    
def get_phrase_by_id(phrase_id: int) -> Phrase:
    return Phrase.query.get_or_404(
        phrase_id,
        f"this phrase not found"
    )

    
def create_phrase(phras: str) -> Phrase:
    phrase = Phrase(
        str_phrase=phras
    )
    db.session.add(phrase)
    db.session.commit()
    return phrase

