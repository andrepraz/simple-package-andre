# Pacote grafico com a classe GraficoLinha

## Description. 
O pacote grafico é usado para:
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

grafico = GraficoLinha(dados)
grafico.gerar_grafico()
```

## Author
Andre Ricardo Prazeres Rodrigues

## License
[MIT](https://choosealicense.com/licenses/mit/)