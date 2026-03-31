# main.py → de applicatie zelf:
# zelfde met depend(dependency injection): hierbij gaat over inhoud van database, maar ook over de routers, die we in de main.py gaan importeren en gebruiken. (depend = argument in parameter mee drgeven)
from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import start_db   
from routers.species import router as species_router
from routers.bird import router as bird_router
from routers.birdspotting import router as birdspotting_router


@asynccontextmanager
async def lifespan(app: FastAPI): 
    start_db()  # hier start je de database op bij het opstarten van de applicatie
    yield
    # hier kan je cleanup doen bij afsluiten

app = FastAPI(lifespan=lifespan) # waarom hier lifespan, want toch al functie hierboven? isdat niet dubbel? nee, lifespan is een argument dat je meegeeft aan FastAPI, en de functie lifespan is een functie die je zelf hebt gedefinieerd. FastAPI zal deze functie aanroepen bij het opstarten en afsluiten van de applicatie. Dus het is niet dubbel, maar juist nodig om de database te starten bij het opstarten van de applicatie.
# hier gebruik lifespan dus moet na de functie lifespan komen, anders zou je een fout krijgen dat lifespan niet gedefinieerd is


app.include_router(species_router)
app.include_router(bird_router)
app.include_router(birdspotting_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

