from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal, get_db
from models import Laptop


Base.metadata.create_all(bind=engine)


def cargar_laptops_iniciales():
    db = SessionLocal()

    if db.query(Laptop).count() == 0:
        db.add_all([
            Laptop(marca="Dell", modelo="Latitude 5440", ram_gb=16, disponible=True),
            Laptop(marca="Lenovo", modelo="ThinkPad E14", ram_gb=8, disponible=False),
            Laptop(marca="HP", modelo="ProBook 450", ram_gb=16, disponible=True)
        ])
        db.commit()

    db.close()


cargar_laptops_iniciales()


app = FastAPI(
    title="API del laboratorio de cómputo",
    version="1.0.0"
)


class LaptopCreate(BaseModel):
    marca: str
    modelo: str
    ram_gb: int


def laptop_a_dict(laptop):
    return {
        "id": laptop.id,
        "marca": laptop.marca,
        "modelo": laptop.modelo,
        "ram_gb": laptop.ram_gb,
        "disponible": laptop.disponible
    }


@app.get("/")
def inicio():
    return {
        "mensaje": "API del laboratorio de cómputo"
    }


#READ
@app.get("/laptops")
def listar_laptops(db: Session = Depends(get_db)):
    resultados = db.query(Laptop).order_by(Laptop.id).all()

    laptops = []

    for laptop in resultados:
        laptops.append(laptop_a_dict(laptop))

    return laptops


@app.get("/laptops/disponibles")
def listar_laptops_disponibles(db: Session = Depends(get_db)):
    resultados = db.query(Laptop).filter(Laptop.disponible == True).order_by(Laptop.id).all()

    laptops = []

    for laptop in resultados:
        laptops.append(laptop_a_dict(laptop))

    return laptops


@app.get("/laptops/{laptop_id}")
def obtener_laptop(laptop_id: int, db: Session = Depends(get_db)):
    laptop = db.query(Laptop).filter(Laptop.id == laptop_id).first()

    if laptop is None:
        raise HTTPException(
            status_code= 404,
            detail= "Laptop no encontrada"
        )

    return laptop_a_dict(laptop)


#CREATE
@app.post("/laptops", status_code=201)
def agregar_laptop(laptop: LaptopCreate, db: Session = Depends(get_db)):
    nueva_laptop = Laptop(
        marca=laptop.marca,
        modelo=laptop.modelo,
        ram_gb=laptop.ram_gb,
        disponible=True
    )

    db.add(nueva_laptop)
    db.commit()
    db.refresh(nueva_laptop)

    return laptop_a_dict(nueva_laptop)