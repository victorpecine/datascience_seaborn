import pandas as pd
import matplotlib.pyplot as plt
from biblioteca import grafico

df_chocolura = pd.read_csv('dados_vendas/chocolura.csv') # 24 linhas, 2 colunas

df_chocolura_nulos = df_chocolura.isna().sum() # Não há dados nulos


# Formatação da data para 'Mês, ano'
serie_data = pd.Series(df_chocolura['mes'])
serie_data = pd.to_datetime(serie_data)

data_formatada = serie_data.dt.strftime('%b, %y')

df_chocolura['mes'] = data_formatada


# Analise visual das vendas
# vendas = grafico(df_chocolura, 'mes', 'vendas', titulo='Vendas entre 2017 e 2018') # Picos de vendas em abril (páscoa) e junho (dia dos namorados)

# plt.show()


# Analise da variação de vendas
df_chocolura['variacao_vendas'] = df_chocolura['vendas'].pct_change()

# variacao_vendas = grafico(df_chocolura, 'mes', 'variacao_vendas')

# plt.show()


# Analise de vendas diárias
df_vendas_diarias = pd.read_csv('dados_vendas/vendas_por_dia.csv') # 61 linhas, 2 colunas

df_vendas_diarias_nulos = df_vendas_diarias.isna().sum() # Não há dados nulos


serie_data_vendas = pd.Series(df_vendas_diarias['dia'])
serie_data_vendas = pd.to_datetime(serie_data_vendas)

data_formatada_vendas = serie_data_vendas.dt.strftime('%b %d')

df_vendas_diarias['dia'] = data_formatada_vendas

vendas_dia_semana = serie_data_vendas.dt.strftime('%a')

df_vendas_diarias['dia_semana'] = vendas_dia_semana


# Analise visual de vendas por dia
# vendas_dia = grafico(df_vendas_diarias, 'dia', 'vendas')
# plt.show()


qtd_vendas_dia_semana = df_vendas_diarias.groupby(['dia_semana'],)['vendas'].sum().sort_values(ascending=False)
# dia_semana
# Wed    478
# Mon    471
# Tue    465
# Thu    462
# Fri    401
# Sun    151
# Sat    127

grafico1 = grafico(df_vendas_diarias, 'dia_semana', df_vendas_diarias.groupby(['dia_semana'],)['vendas'].sum())
plt.show()


# print(qtd_vendas_dia_semana)

# print(df_vendas_diarias)

