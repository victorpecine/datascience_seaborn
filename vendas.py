import pandas as pd
import seaborn as sns
from biblioteca import grafico

df_alucar = pd.read_csv('dados_vendas/alucar.csv') # 24 linhas, 2 colunas

df_alucar_nulos = df_alucar.isna().sum() # Não há dados nulos


# Formatação da data para 'Mês, ano'
serie_data = pd.Series(df_alucar['mes'])
serie_data = pd.to_datetime(serie_data)

data_formatada = serie_data.dt.strftime('%b, %y')

df_alucar['mes'] = data_formatada


# Análise visual das vendas
# sns.set_palette('Paired')
# vendas = sns.lineplot(data=df_alucar, x='mes', y='vendas')

# vendas.figure.set_size_inches(12, 5)
# vendas.set_title('Vendas entre 2017 e 2018', loc='left', fontsize=18)
# vendas.set_xlabel('Meses', fontsize=14)
# vendas.set_xticklabels(df_alucar['mes'], rotation=30)
# vendas.set_ylabel('Qtd. de vendas', fontsize=14)

# vendas = vendas.get_figure()
# vendas.savefig('graficos_vendas/vendas.png')


# Análise visual da variacao das vendas nos meses
# df_alucar['variacao_vendas'] = df_alucar['vendas'].pct_change()
# variacao_vendas = sns.lineplot(data=df_alucar, x='mes', y='variacao_vendas')

# variacao_vendas.figure.set_size_inches(12, 5)
# variacao_vendas.set_title('Queda no crescimento de vendas entre 2017 e 2018', loc='left', fontsize=18)
# variacao_vendas.set_xlabel('Meses', fontsize=14)
# variacao_vendas.set_xticklabels(df_alucar['mes'], rotation=30)
# variacao_vendas.set_ylabel('Var. vendas', fontsize=14)

# variacao_vendas = variacao_vendas.get_figure()
# variacao_vendas.savefig('graficos_vendas/variacao_vendas.png')


# Análise visual das vendas com função 'grafico'
# vendas = grafico(df_alucar, 'mes', 'Meses', 'vendas', 'Qtd. de vendas', 'Aumento na qtd. de vendas entre 2017 e 2018')

# plt.show()

df_alucar['variacao_vendas'] = df_alucar['vendas'].pct_change()

# Análise visual da variacao das vendas nos meses com função 'grafico'
# variacao_vendas = grafico(df_alucar, 'mes', 'Meses', 'variacao_vendas', 'Var. vendas', 'Queda no crescimento de vendas entre 2017 e 2018')

# plt.show()
