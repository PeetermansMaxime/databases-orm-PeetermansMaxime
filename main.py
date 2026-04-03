<<<<<<< HEAD
from fastapi import FastAPI

app = FastAPI()
=======
# main.py → de applicatie zelf:
# zelfde met depend(dependency injection): hierbij gaat over inhoud van database, maar ook over de routers, die we in de main.py gaan importeren en gebruiken. (depend = argument in parameter mee drgeven)
from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import start_db   



@asynccontextmanager
async def lifespan(app: FastAPI):
    start_db()  # bij opstarten
    yield
    # hier kan je cleanup doen bij afsluiten

app = FastAPI(lifespan=lifespan) # waarom hier lifespan, want toch al functie hierboven? isdat niet dubbel? nee, lifespan is een argument dat je meegeeft aan FastAPI, en de functie lifespan is een functie die je zelf hebt gedefinieerd. FastAPI zal deze functie aanroepen bij het opstarten en afsluiten van de applicatie. Dus het is niet dubbel, maar juist nodig om de database te starten bij het opstarten van de applicatie.
# hier gebruik lifespan dus moet na de functie lifespan komen, anders zou je een fout krijgen dat lifespan niet gedefinieerd is
>>>>>>> d5bfee58ce8ccc525920b71e2714991f3297b6c2

@app.get("/")
async def root():
    return {"message": "Hello World"}