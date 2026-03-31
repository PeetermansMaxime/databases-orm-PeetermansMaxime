# repositories/bird.py    → HOE werk je met birds in database
# repositories/bird.py
# → gebruikt het model om queries uit te voeren
# → "haal alle birds op" / "voeg bird toe"

from sqlmodel import Session, select
from models.bird import Bird, BirdCreate

class BirdRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        """Get all birds from the database."""
        statement = select(Bird)
        return self.session.exec(statement).all()

    def insert(self, payload: BirdCreate):
        """Insert a new bird into the database."""
        item = Bird.model_validate(payload)
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item
    
    def get_one(self, id: int):
        """Get a single bird by id."""
        return self.session.get(Bird, id)