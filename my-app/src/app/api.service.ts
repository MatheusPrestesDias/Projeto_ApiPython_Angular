import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Veiculo } from './models/veiculos.models';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private listaDeVeiculos : any[];

  private url = 'http://127.0.0.1:8000/';

  constructor(private httpClient: HttpClient) {
    this.listaDeVeiculos = [];
   }

   dados(){
     return this.httpClient.get<Veiculo[]>(this.url);
   }
}
