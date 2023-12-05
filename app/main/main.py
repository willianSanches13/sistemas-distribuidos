import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

dados = pd.read_csv("/app/Credit.csv")
dados.shape

@app.route('/media', methods=['GET'])
def getMean():
    resultado = dados['age'].mean()
    return jsonify({'resultado': resultado})

@app.route('/media/house', methods=['GET'])
def getMeanByHouse():
    resultado = dados.groupby('housing',as_index=False)['age'].mean()
    return jsonify({'resultado': resultado.to_json(orient='records')})

@app.route('/credit/age', methods=['GET'])
def getCreditByAge():
    resultado = dados.groupby('credit_history', as_index=False)['age'].agg(['min','max'])
    return jsonify({'resultado': resultado.to_json(orient='records')})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)

