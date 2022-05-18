export interface Veiculo {
    modelo: string;
    fabricante: string;
    anoFabricacao: number | string;
    chassi: number;
    imposto?: string;
  }