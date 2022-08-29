import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ranksums

df_gorjetas = pd.read_csv('dados_gorjetas/tips.csv')

df_gorjetas = df_gorjetas.rename(columns={'total_bill': 'valor_conta',
                                          'tip': 'valor_gorjeta',
                                          'dessert': 'sobremesa',
                                          'day': 'dia_da_semana',
                                          'time': 'refeicao',
                                          'size': 'qtd_pessoas'})

df_gorjetas['sobremesa'].replace({'Yes': 'sim',
                                  'No': 'nao'}, inplace=True)

df_gorjetas['dia_da_semana'].replace({'Sun': 'domingo',
                                      'Sat': 'sabado',
                                      'Thur': 'quinta',
                                      'Fri': 'sexta'}, inplace=True)

df_gorjetas['refeicao'].replace({'Dinner': 'janta',
                                 'Lunch': 'almoco'}, inplace=True)


# Visualização com gráficos
# Valor da conta x valor da gorjeta

# valor_conta_gorjeta = sns.scatterplot(x='valor_conta', y='valor_gorjeta', data=df_gorjetas) # Visualmente, o valor da gorjeta cresce conforme aumenta o valor da conta

# fig_1 = valor_conta_gorjeta.get_figure()

# fig_1.savefig('valor_conta_gorjeta.png') # Salvando gráfico em um arquivo


dados_nao_nulos = df_gorjetas.count() # Não há valores nulos no dataframe


df_gorjetas['porcentagem'] = ((df_gorjetas['valor_gorjeta'] / df_gorjetas['valor_conta']) * 100).round(2)

# porcent_gorjeta = sns.scatterplot(x='valor_conta', y='porcentagem', data=df_gorjetas) # Visualmente, o valor da conta não é proporcional ao valor da gorjeta

# fig_2 = porcent_gorjeta.get_figure()

# fig_2.savefig('porcent_gorjeta.png')


# porcent_gorjeta_linha = sns.lineplot(x='valor_conta', y='porcentagem', data=df_gorjetas)

# fig_3 = porcent_gorjeta_linha.get_figure()

# fig_3.savefig('porcent_gorjeta_linha.png')


# valor_conta_gorjeta_linha = sns.lmplot(x='valor_conta', y='porcentagem', data=df_gorjetas)

# valor_conta_gorjeta_linha.savefig('valor_conta_gorjeta_linha.png')


# Visualização com gráficos
# Sobremesa x valor da gorjeta

desc_sobremesa_gorjeta = df_gorjetas[df_gorjetas['sobremesa'] == 'sim'].describe() # estatísticas descritivas
# print(desc_sobremesa_gorjeta)

desc_sem_sobremesa_gorjeta = df_gorjetas[df_gorjetas['sobremesa'] == 'nao'].describe()
# print(desc_sem_sobremesa_gorjeta)

# sobremesa_gorjeta = sns.catplot(x='sobremesa', y='valor_gorjeta', data=df_gorjetas)

# sobremesa_gorjeta.savefig('sobremesa_gorjeta.png')


# regre_conta_gorjeta = sns.lmplot(x='valor_conta', y='valor_gorjeta', col='sobremesa', hue='sobremesa', data=df_gorjetas)

# regre_conta_gorjeta.savefig('regre_conta_gorjeta.png')


# regre_porcent_gorjeta = sns.lmplot(x='valor_conta', y='porcentagem', col='sobremesa', hue='sobremesa', data=df_gorjetas)

# regre_porcent_gorjeta.savefig('regre_porcent_gorjeta.png')


# Teste de hipótese
# Hipótese nula - a distribuição da gorjeta é a mesma entre quem pediu e quem não pediu sobremesa
# Hipótese não nula - a distribuição da gorjeta é diferente entre quem pediu e quem não pediu sobremesa

porcent_sobremesa_gorjeta = df_gorjetas.query('sobremesa == "sim"').porcentagem

# print(porcent_sobremesa_gorjeta)

porcent_sem_sobremesa_gorjeta = df_gorjetas.query('sobremesa == "nao"').porcentagem

# print(porcent_sem_sobremesa_gorjeta)

comparativo = ranksums(porcent_sobremesa_gorjeta, porcent_sem_sobremesa_gorjeta)

print(comparativo)