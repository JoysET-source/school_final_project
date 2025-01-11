from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.schemas import RicettaCreate, Ricetta as RicetteSchemas
from src.models import Ricette

router = APIRouter(prefix="/Ricetta", tags=["RICETTE"])

"""write recipes"""
@router.post("/crea ricetta/", response_model=RicetteSchemas)
def scrivi_ricetta(ricetta: RicettaCreate, db: Session = Depends(get_db)):
    db_ricetta = db.query(Ricette).filter(Ricette.nome_ricetta == ricetta.nome_ricetta).first()
    if db_ricetta:
        raise HTTPException(status_code=400, detail="Ricetta gia esistente")
    db_ricetta = Ricette(
        nome_ricetta=ricetta.nome_ricetta,
        ingredienti=ricetta.ingredienti,
        kcal=ricetta.kcal
    )
    db.add(db_ricetta)
    db.commit()
    db.refresh(db_ricetta)
    return db_ricetta

"""cerca per nome"""
@router.get("/cerca ricetta/", response_model=RicetteSchemas)
def trova_ricetta(nome_ricetta: str, db: Session = Depends(get_db)):
    db_ricetta = db.query(Ricette).filter(Ricette.nome_ricetta == nome_ricetta).first()
    if db_ricetta is None:
        raise HTTPException(status_code=404, detail="Ricetta non trovata")
    return db_ricetta

@router.get("/cerca per calorie/", response_model=List[RicetteSchemas])
def apporto_calorie(kcal: int, db: Session = Depends(get_db)):
    pass








