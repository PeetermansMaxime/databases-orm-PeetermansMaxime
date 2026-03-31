# routers/bird.py
# routers/bird.py         → WAAR kan je birds bereiken via API
# → maakt endpoints aan die de repository gebruiken
# → GET /birds → roept repo.get_all() aan
# → POST /birds → roept repo.insert() aan


from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models.bird import Bird, BirdCreate
from repositories.bird import BirdRepository

router = APIRouter(prefix="/birds", tags=["Birds"])

def get_bird_repository(
    session: Annotated[Session, Depends(get_session)]
) -> BirdRepository:
    return BirdRepository(session)

@router.get("/", response_model=List[Bird])
async def get_birds(repo: Annotated[BirdRepository, Depends(get_bird_repository)]):
    """Get all birds from the database."""
    return repo.get_all() # deze F zie je in swagger .

@router.get("/{id}", response_model=Bird)
async def get_bird_by_id(id: int, repo: Annotated[BirdRepository, Depends(get_bird_repository)]):
    """Get a single bird by id."""
    item = repo.get_one(id)
    if not item:
        raise HTTPException(status_code=404, detail="Bird not found")
    return item

@router.post("/", response_model=Bird, status_code=201)
async def add_bird(bird: BirdCreate, repo: Annotated[BirdRepository, Depends(get_bird_repository)]):
    """Add a new bird to the database."""
    return repo.insert(bird)