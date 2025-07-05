import matplotlib.pyplot as plt

class GraficoLinha:
    def __init__(self, dados):
        self.valor_x = dados.get('valor_x', [])
        self.valor_y = dados.get('valor_y', [])

    def gerar_grafico(self):
        plt.plot(self.valor_x, self.valor_y, marker='o', linestyle='-')
        plt.title('Gráfico de Linha')
        plt.xlabel('Eixo X')
        plt.ylabel('Eixo Y')
        plt.grid(True)
        plt.savefig('grafico_linha.png')
        plt.show()