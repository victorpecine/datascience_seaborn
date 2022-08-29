import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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


# valor_conta_gorjeta = sns.scatterplot(x='valor_conta', y='valor_gorjeta', data=df_gorjetas) # Visualmente, o valor da gorjeta cresce conforme aumenta o valor da conta
# plt.show()

dados_nao_nulos = df_gorjetas.count() # Não há valores nulos no dataframe


df_gorjetas['porcentagem'] = ((df_gorjetas['valor_gorjeta'] / df_gorjetas['valor_conta']) * 100).round(2)

# porcent_gorjeta = sns.scatterplot(x='valor_conta', y='porcentagem', data=df_gorjetas) # Visualmente, o valor da conta não é proporcional ao valor da gorjeta
# plt.show()


# porcent_gorjeta = sns.lineplot(x='valor_conta', y='porcentagem', data=df_gorjetas)
# plt.show()


# regressao = sns.lmplot(x='valor_conta', y='porcentagem', data=df_gorjetas)
# plt.show()
