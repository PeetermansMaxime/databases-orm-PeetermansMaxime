from typing import Optional
from datetime import datetime, timezone
from sqlmodel import Field, Relationship, SQLModel
from models.bird import Bird

class BirdspottingBase(SQLModel):
    location: str
    observer_name: str
    notes: Optional[str] = None
    spotted_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Birdspotting(BirdspottingBase, table=True):
    """Database table model for a birdspotting observation."""
    __tablename__ = "birdspottings"
    id: Optional[int] = Field(default=None, primary_key=True)
    bird_id: int = Field(foreign_key="birds.id")
    bird: Optional[Bird] = Relationship()

class BirdspottingCreate(BirdspottingBase):
    """request model for creating a new birdspotting observation""""
    bird_id: int # foreign key naar de bird die gespot is, dit veld is verplicht bij het aanmaken van een nieuw record, omdat we willen weten welke bird er gespot is. We maken deze aparte klasse aan omdat we misschien in de toekomst extra validatie of logica willen toevoegen bij het aanmaken van een nieuw record, en dan is het handig om een aparte klasse te hebben voor de create operatie.