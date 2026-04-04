# models/bird.py
#  models/bird.py          → WAT is een bird (structuur/tabel)
# → definieert de Bird klasse + database tabel
# → "een bird heeft nickname, ring_code, age, species_id"

from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from models.species import Species

class BirdBase(SQLModel):
    nickname: str
    ring_code: str
    age: int

class Bird(BirdBase, table=True):
    """Database table model for a bird."""
    __tablename__ = "birds"
    id: Optional[int] = Field(default=None, primary_key=True)
    species_id: int = Field(foreign_key="species.id") # add relationship between bird and species, this will create a foreign key in the database that links the bird to a specific species. We also need to add a relationship field to the Bird class to be able to access the related species data when we query for birds.
    species: Optional[Species] = Relationship() # zo krijg je effectief data onder foreign key, je kan dan bv bird.species.name gebruiken om de naam van de species te krijgen van een bird. hoezo foreign key is toch id van species? Ja, dat klopt, de foreign key is inderdaad species_id, maar door de relationship kunnen we ook direct toegang krijgen tot de gerelateerde Species data via het species veld in de Bird klasse. Dus in plaats van alleen de species_id te hebben, kunnen we ook de volledige Species objecten ophalen wanneer we een Bird object opvragen, en dan kunnen we bijvoorbeeld bird.species.name gebruiken om de naam van de species te krijgen van een bird. 
    # ja idd dr erop te klikken in swagger.

class BirdCreate(BirdBase):
    """request model for creating a new bird"""
    species_id: int