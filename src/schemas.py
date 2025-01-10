from pydantic import BaseModel

class RicettaBase(BaseModel):
    nome_ricetta: str

class RicettaCreate(RicettaBase):
    ingredienti_proteici: str
    carboidrati: str
    verdure_legumi: str
    ingredienti_grassi: str
    condimenti: str

class Ricetta(RicettaBase):
    nome_ricetta: str



