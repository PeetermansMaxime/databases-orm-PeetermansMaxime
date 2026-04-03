from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models.species import Species, SpeciesCreate
from repositories.species import SpeciesRepository

router = APIRouter(prefix="/species", tags=["Species"])

def get_species_repository(
    session: Annotated[Session, Depends(get_session)],
) -> SpeciesRepository:
    return SpeciesRepository(session)

@router.get("/", response_model=List[Species])
async def get_species(repo: Annotated[SpeciesRepository, Depends(get_species_repository)]):
    """Get all species from the database."""
    return repo.get_all()
# bij get standaard statuscode 200
 

@router.get("/{id}", response_model=Species)
async def get_species_by_id(id: int, repo: Annotated[SpeciesRepository, Depends(get_species_repository)]):
    """Get a single species by id."""
    item = repo.get_one(id) #bij get standaard statuscode 200.
    if not item:
        raise HTTPException(status_code=404, detail="Species not found")
    return item # waarom hier statuscode 404? Omdat we een specifieke species opvragen met een id, en als die id niet bestaat in de database, dan willen we een foutmelding teruggeven dat de species niet gevonden is. In dat geval is 404 de juiste statuscode om aan te geven dat de resource niet gevonden is.

@router.post("/", response_model=Species, status_code=201)
async def add_species(species: SpeciesCreate, repo: Annotated[SpeciesRepository, Depends(get_species_repository)]):
    """Add a new species to the database."""
    return repo.insert(species)