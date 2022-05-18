from fastapi import FastAPI

from models import Multa
from models import Veiculo

app = FastAPI()

multas = [
        Multa(id= 1, tipoInfracao = "Leve", pontos = 3, valorMulta= 88.38),
        Multa(id= 2, tipoInfracao = "Media", pontos = 4, valorMulta= 130.16),
        Multa(id= 3, tipoInfracao = "Grave", pontos = 5, valorMulta= 195.23),
        Multa(id= 4, tipoInfracao = "Gravissima", pontos = 7, valorMulta= 293.47)
    ]

veiculos = [
        Veiculo(id=1, modelo="Ka", fabricante="Ford", anoFabricacao=2015, chassi=123456789, cor="Prata", potencia="77cv", imposto="Pago", antigoProprietario="Luis", multas=multas),
        Veiculo(id=2, modelo="Fusion", fabricante="Ford", anoFabricacao=2019, chassi=147258369, cor="Preto", potencia="150cv", imposto="Não pago", antigoProprietario="Matheus", multas=[multas[0], multas[2]])
    ]

@app.get("/")
def read_root():
    return veiculos


@app.get("/chassi/{chassi}")
def buscaVeiculoChassi(chassi: int):
    for veiculo in veiculos:
            if(veiculo.chassi == chassi):
                return veiculo


@app.post("/veiculo")
def insereVeiculo(veiculo: Veiculo):
    veiculos.append(veiculo)
    return veiculo


@app.delete("/id/{id}")
def deletarVeiculo(id: int):
    for veiculo in veiculos:
            if(veiculo.id == id):
                veiculos.remove(veiculo)
                return veiculo