from typing import List
from pydantic import BaseModel

class Multa (BaseModel): 
    id: int
    tipoInfracao: str
    pontos: int
    valorMulta: float


class Veiculo (BaseModel): 
    id: int
    modelo: str
    fabricante: str
    anoFabricacao: int
    chassi: int
    cor: str
    potencia: str
    imposto: str
    antigoProprietario: str
    multas: List[Multa]
