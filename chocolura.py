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
vendas = grafico(df_chocolura, 'mes', 'vendas', titulo='Vendas entre 2017 e 2018') # Picos de vendas em abril (páscoa) e junho (dia dos namorados)

plt.show()