# Pacote grafico-andre com a classe GraficoLinha

## Descrição. 
O pacote grafico-andre é usado para:
- Gerar gráfico de linha, que é uma classe, na qual após passarmos uma estrutura de dados conforme abaixo:
```
dados = {
	'valor_x: [valores],
	'valor_y: [valores],
}
```
- Essa classe tem um método chamada gerar_grafico() que apresenta o gráfico e grava uma imagem dele.

## Instalação

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
pip install -i https://test.pypi.org/simple/ grafico_linha
```

## Uso

```python
from grafico.grafico_linha import GraficoLinha

dados = {
    'valor_x': [2, 3, 4],
    'valor_y': [5, 6, 7]
}

grafico = GraficoLinha(dados)
grafico.gerar_grafico()
```

## Author
Andre Ricardo Prazeres Rodrigues

## License
[MIT](https://choosealicense.com/licenses/mit/)