from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base


class Ricette(Base):
    __tablename__ = "Ricette"

    nome_ricetta = Column(String, primary_key=True, index=True)
    ingredienti = Column(String, nullable=True, index=True)
    kcal = Column(Integer, unique=True, index=True)


# def valida_valore(value):
#     if isinstance(value, str):
#         # Se il valore è già una stringa, lo restituiamo così com'è
#         return value
#     elif isinstance(value, (int, float)):
#         # Se è un numero, lo trasformiamo in stringa
#         return str(value)
#     else:
#         raise ValueError("Il valore deve essere una stringa o un numero")
#
# def inserisci_alimento(**kwargs):
#     validated_values = {}
#     for column, value in kwargs.items():
#         validated_values[column] = valida_valore(value)
#     return validated_values

# session = SessionLocal()
# validated_values = inserisci_alimento()
# alimento = Ricette(**validated_values)
# session.add(alimento)
# session.commit()


