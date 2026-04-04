from decimal import Decimal
from typing import Optional
from sqlmodel import Field, SQLModel

class SpeciesBase(SQLModel):
    name: str
    scientific_name: str
    family: str
    conservation_status: str
    wingspan_cm: Decimal

class Species(SpeciesBase, table=True):
    """Database table model for a bird species."""
    id: Optional[int] = Field(default=None, primary_key=True) # default none omdat het automatisch gegenereerd wordt door de database, dus je hoeft het niet zelf in te vullen bij het aanmaken van een nieuw record

class SpeciesCreate(SpeciesBase):
    """request model for creating a new bird species"""
    pass  #pass omdat we geen extra velden nodig hebben voor het aanmaken van een nieuw record, we kunnen gewoon de velden van SpeciesBase gebruiken. We maken deze aparte klasse aan omdat we misschien in de toekomst extra validatie of logica willen toevoegen bij het aanmaken van een nieuw record, en dan is het handig om een aparte klasse te hebben voor de create operatie.