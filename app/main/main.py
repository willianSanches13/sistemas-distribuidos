import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

dados = pd.read_csv("/app/Credit.csv")
dados.shape

@app.route('/dados', methods=['GET'])
def obter_dados():
    

    resultado = dados['age'].mean()
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)

