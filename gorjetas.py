import pandas as pd
import seaborn as sbn

df_gorjetas = pd.read_csv('dados_gorjetas/tips.csv')

df_gorjetas = df_gorjetas.rename(columns={'total_bill': 'valor_total',
                                            'tip': 'valor_gorjeta',
                                            'dessert': 'sobremesa',
                                            'day': 'dia_da_semana',
                                            'time': 'refeicao',
                                            'size': 'qtd_pessoas'})

df_gorjetas['sobremesa'].replace({'Yes': 'sim', 'No': 'nao'}, inplace=True)

df_gorjetas['dia_da_semana'].replace({'Sun': 'domingo',
                                        'Sat': 'sabado',
                                        'Thur': 'quinta',
                                        'Fri': 'sexta'}, inplace=True)

df_gorjetas['refeicao'].replace({'Dinner': 'janta', 'Lunch': 'almoco'}, inplace=True)



print(df_gorjetas)

# print(df_gorjetas['refeicao'].unique())

