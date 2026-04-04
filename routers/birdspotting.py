from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models.birdspotting import Birdspotting, BirdspottingCreate
from repositories.birdspotting import BirdspottingRepository

router = APIRouter(prefix="/birdspottings", tags=["Birdspotting"])

def get_birdspotting_repository(
    session: Annotated[Session, Depends(get_session)]
) -> BirdspottingRepository:
    return BirdspottingRepository(session)

@router.get("/", response_model=List[Birdspotting])
async def get_birdspottings(repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]):
    return repo.get_all()

@router.get("/{id}", response_model=Birdspotting)
async def get_birdspotting(id: int, repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]):
    item = repo.get_one(id)
    if not item:
        raise HTTPException(status_code=404, detail="Birdspotting not found")
    return item

@router.post("/", response_model=Birdspotting, status_code=201)
async def add_birdspotting(birdspotting: BirdspottingCreate, repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]):
    return repo.insert(birdspotting)