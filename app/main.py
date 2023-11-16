import pandas as pd


def executar():
    dados = pd.read_csv("/home/williansanches/PycharmProjects/sistemas-distribuidos/app/Credit.csv")
    dados.shape
    dados.loc[dados['age'] > 25].mean()
    dados['age'].mean()
    dados.loc[dados['housing'] == 'rent']
    dados.groupby('housing', as_index=False)['age'].mean()
    dados['credit_history'].value_counts()
    dados.groupby('credit_history', as_index=False)['job'].count()
    dados.groupby('credit_history', as_index=False)['age'].agg(['min', 'max'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    executar()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
