import seaborn as sns

def grafico(dataframe, x, y, labelx=False, labely=False, titulo=''):
    sns.set_palette('Paired')
    ax = sns.lineplot(data=dataframe, x=x, y=y)

    ax.figure.set_size_inches(12, 5)
    ax.set_title(titulo, loc='left', fontsize=18)
    ax.set_xlabel(labelx, fontsize=14)
    ax.set_xticklabels(dataframe[x], rotation=30)
    ax.set_ylabel(labely, fontsize=14)

    ax = ax.get_figure()
