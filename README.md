# pastry-shop

### Pastry management system

---------------------

> ## Tecnologies
> - Django Rest Framework (API)
> - PostgreSQL (DB)
> - Vue (Web)
> - Flutter (Mobile)

## Developers
- <strong><span style="color: #1564A2">Marcos Souza</span> [mrcsz.m@gmail.com]</strong>
    - github: <em>github.com/marcossouz</em>

- Bruno
- Jailton


-----------------------
#### modeling suggestion
`pastel = {
  "codigo": 123456,
  "nome": "text",
  "valor": 12.34,
  "peso": 300,
  "unidade": "mg",  
  "info-extra": "",
  "ingredientes": [
      "queijo", "presunto", ...
    ]
}

adicional = {
  "texto": "text",
  "valor": 12.34
}

bebida = {
  "tipo": "suco, refri, ...",
  "apresentacao": "copo, lata, garrafa, ..." 
  "valor": 12.34,
  "quantidade": 300,
  "unidade": "ml, mg, kg, ...",
  "sabor": "laranja, limão, ...",
  "marca": "guaraná, coca, ...",
}

taxa_maquineta = {
  "percentual": 3.45,
}

taxa_entrega = {
  "km_max": 3,
  "valor": 12.34
}

pedido = [pastel, bebida, adicional, taxa]`