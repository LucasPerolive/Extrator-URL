# Documentação do Projeto de Conversão de Câmbio
## Visão Geral
Este projeto tem como objetivo criar um programa Python orientado a objetos que seja capaz de extrair os parâmetros de uma URL de consulta de câmbio e realizar a conversão de moeda com base nas taxas de câmbio fornecidas.

## Funcionalidades Principais
### 1. Extração de Parâmetros de URL:
* O programa deve ser capaz de extrair os parâmetros relevantes de uma URL, incluindo a moeda de origem, a moeda de destino e a quantidade a ser convertida.

## 2. Conversão de Moeda:
* Com base nos parâmetros extraídos e nas taxas de câmbio obtidas(deve ser passada), o programa deve realizar a conversão de moeda e fornecer o resultado.

## Uso
Aqui está um exemplo de como usar o projeto:
```
url = "https://bytebank.com/cambio?moedaDestino=real&quantidade=100&moedaOrigem=dolar"
extrator_url = ExtratorURL(url)
print(extrator_url)

valor_dolar = 5.50
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
valor_quantidade = int(extrator_url.get_valor_parametro("quantidade"))
converter(moeda_origem, moeda_destino, valor_quantidade)
```
# Requisitos 
* Python 3.x

# Conclusão
Este projeto permite a extração de parâmetros de uma URL de consulta de câmbio e a realização de conversão de moeda com base nas taxas de câmbio.
