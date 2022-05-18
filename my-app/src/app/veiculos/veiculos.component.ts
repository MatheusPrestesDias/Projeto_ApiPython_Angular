import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Veiculo } from '../models/veiculos.models';

@Component({
  selector: 'app-veiculos',
  templateUrl: './veiculos.component.html',
  styleUrls: ['./veiculos.component.css']
})
export class VeiculosComponent implements OnInit {

  veiculos: any[] = [];
  constructor(private service : ApiService) { }

  ngOnInit(): void {
    this.service.dados().subscribe((veiculos: Veiculo[]) => {
      console.table(veiculos);
      this.veiculos = veiculos;
    })
  }

}
