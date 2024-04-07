import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Nome': ['Manuella', 'Maria', 'Julia', 'Ana', 'Pedro'],
    'Idade': [25, 30, 35, 40, 45],
    'Pontuação': [70, 85, 90, 75, 80]
}

df = pd.DataFrame(dados)

# Cores e marcadores
cores = ['blue', 'green', 'orange', 'red', 'purple']
marcadores = ['o', 's', '^', 'D', 'x']

# Gráfico de dispersão
for i in range(len(df)):
    plt.scatter(df['Idade'][i], df['Pontuação'][i], color=cores[i], marker=marcadores[i], s=100, label=df['Nome'][i])

# Título e rótulos
plt.title('Pontuação em relação à Idade', fontsize=14)
plt.xlabel('Idade', fontsize=12)
plt.ylabel('Pontuação', fontsize=12)

# Grade
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Legenda com posicionamento automático
plt.legend(loc='best')

# Fonte
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.show()