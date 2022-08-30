import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_alucar = pd.read_csv('dados_vendas/alucar.csv') # 24 linhas, 2 colunas

df_alucar_nulos = df_alucar.isna().sum() # Não há dados nulos

df_alucar['mes'] = pd.to_datetime(df_alucar['mes'])


# Analises visuais
sns.set_palette('Paired')
vendas = sns.lineplot(data=df_alucar, x='mes', y='vendas')
vendas.figure.set_size_inches(12, 5)
vendas.set_title('Crescimento de vendas entre 2017 e 2018', loc='left', fontsize=18)
vendas.set_xlabel('Meses', fontsize=14)
vendas.set_ylabel('Qtd. de vendas', fontsize=14)
vendas = vendas.get_figure()
vendas.savefig('graficos_vendas/vendas.png')

print(df_alucar)