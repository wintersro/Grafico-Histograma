import matplotlib.pyplot as plt
import numpy as np

# Dados da distribuição de frequência
classes = ['2,25 - 15,25', '15,25 - 28,25', '28,25 - 41,25', '41,25 - 54,25', '54,25 - 67,25', '67,25 - 80,25']
frequencia_absoluta = [13, 9, 13, 3, 1, 1]

# Criar o histograma
plt.bar(classes, frequencia_absoluta, color='#004FC8')

# Adicionar rótulos com os valores das frequências nas barras
for i in range(len(classes)):
    plt.text(i, frequencia_absoluta[i], frequencia_absoluta[i], ha='center', va='bottom')

# Adicionar linha uma linha vermelha acima de cada barra
    plt.plot([i-0.4, i+0.4], [frequencia_absoluta[i], frequencia_absoluta[i]], color='red')

# Adicionar rótulos e título
plt.xlabel('Tempo de uso do celular (horas)')
plt.ylabel('Frequência')
plt.title('Gráfico de Histograma')

# Rotacionar os rótulos do eixo x para melhor legibilidade
plt.xticks(rotation=45)

# Exibir linhas de grades
#plt.grid (True) #É só retirar o comentário para exibir

# Exibir o histograma
plt.show()