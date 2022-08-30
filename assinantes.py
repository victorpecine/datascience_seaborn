import pandas as pd
import matplotlib.pyplot as plt
from biblioteca import grafico

df_assinantes = pd.read_csv('dados_vendas/newsletter_alucar.csv') # 24 linhas, 2 colunas

df_assinantes_nulos = df_assinantes.isna().sum() # Não há dados nulos


# Formatação da data para 'Mês, ano'
serie_data = pd.Series(df_assinantes['mes'])
serie_data = pd.to_datetime(serie_data)

data_formatada = serie_data.dt.strftime('%b, %y')

df_assinantes['mes'] = data_formatada


# Analise visual do crescimento de assinantes
df_assinantes['novos_assinantes'] = df_assinantes['assinantes'].diff()

grafico_assiantes = grafico(df_assinantes, 'mes', 'novos_assinantes', 'Meses', 'Novos assinantes')

plt.show()
