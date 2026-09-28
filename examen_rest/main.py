from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine, SessionLocal, Base
from models import Laptop

INITIAL_LAPTOPS = [
    {"marca": "Dell", "modelo": "XPS 13", "ram_gb": 16, "disponible": True},
    {"marca": "Apple", "modelo": "MacBook Pro M2", "ram_gb": 16, "disponible": True},
    {"marca": "Lenovo", "modelo": "ThinkPad X1 Carbon", "ram_gb": 32, "disponible": False},
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Al arrancar, si la tabla no existe, créala con Base.metadata.create_all
    Base.metadata.create_all(bind=engine)
    
    # Si la tabla está vacía, inserta las tres laptops de abajo. 
    # Si ya tiene registros, no las vuelvas a insertar.
    db = SessionLocal()
    try:
        count = db.query(Laptop).count()
        if count == 0:
            for lap_data in INITIAL_LAPTOPS:
                db.add(Laptop(**lap_data))
            db.commit()
    finally:
        db.close()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def index():
    return {"message": "API de Laptops iniciada correctamente"}