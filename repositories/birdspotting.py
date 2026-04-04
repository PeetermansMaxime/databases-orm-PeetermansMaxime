from sqlmodel import Session, select
from models.birdspotting import Birdspotting, BirdspottingCreate

class BirdspottingRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        """Get all birdspotting observations from the database."""
        statement = select(Birdspotting)
        return self.session.exec(statement).all()

    def get_one(self, id: int):
        """Get a single birdspotting observation by id."""
        return self.session.get(Birdspotting, id)

    def insert(self, payload: BirdspottingCreate):
        """Insert a new birdspotting observation into the database."""
        item = Birdspotting.model_validate(payload)
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item