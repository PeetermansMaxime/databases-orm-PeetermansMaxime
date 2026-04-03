# main.py → de applicatie zelf:
# zelfde met depend(dependency injection): hierbij gaat over inhoud van database, maar ook over de routers, die we in de main.py gaan importeren en gebruiken. (depend = argument in parameter mee drgeven)
from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import start_db   
from routers.species import router as species_router
from routers.bird import router as bird_router # hier is wel juist
from routers.birdspotting import router as birdspotting_router
# maar hier heb ik toch ook niet  gedaan, gewoon alle routers geimporteeerd in deze main.py, en dan in de app.include_router() gebruiken om ze toe te voegen aan de applicatie. Zo kan je dan alle endpoints van die routers gebruiken in je API. ja waarom zou ik dan nog get_bird_repository nodig hebben in de bird router? Ja, dat klopt, je hebt inderdaad nog steeds de get_bird_repository functie nodig in de bird router, omdat die functie verantwoordelijk is voor het aanmaken van een instantie van de BirdRepository class, die vervolgens wordt gebruikt in de endpoints van de bird router om toegang te krijgen tot de database. Dus zelfs als je de bird router importeert en toevoegt aan de applicatie in main.py, heb je nog steeds de get_bird_repository functie nodig in de bird router om ervoor te zorgen dat je toegang hebt tot de database via de repository in die router.
# ok maar dit was mij hier nooit opgevallen, ik kreeg nooit een foutmelding? hoe komt dit? alles werkte gewoon? Ja, dat klopt, je kreeg waarschijnlijk geen foutmelding omdat je de bird router nog niet had geïmplementeerd of gebruikt in je API, dus de get_bird_repository functie werd nog niet aangeroepen. Maar zodra je de endpoints van de bird router gaat gebruiken in je API, bijvoorbeeld door een GET of POST request te doen naar /birds, dan zal de get_bird_repository functie worden aangeroepen om een instantie van de BirdRepository class te maken, en als die functie er niet is, dan zou je inderdaad een foutmelding krijgen dat de dependency niet gevonden kan worden. Dus het is belangrijk om ervoor te zorgen dat je alle benodigde dependencies hebt geïmplementeerd en beschikbaar hebt in je routers voordat je ze gaat gebruiken in je API.


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

