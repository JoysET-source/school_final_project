from pydantic import BaseModel

class RicettaBase(BaseModel):
    nome_ricetta: str
    ingredienti_proteici: str
    carboidrati: str
    verdure_legumi: str
    ingredienti_grassi: str
    condimenti: str

class RicettaCreate(RicettaBase):
    nome_ricetta: str

class Ricetta(RicettaBase):
    nome_ricetta: str





