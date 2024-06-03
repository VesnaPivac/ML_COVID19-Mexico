from flask import Flask, request, jsonify
import mlflow.pyfunc
import pandas as pd

app = Flask(__name__)

# Configurar la conexión a DagsHub y cargar el modelo
dagshub_repo_owner = 'VesnaPivac'
dagshub_repo_name = 'ML_COVID19-Mexico'
mlflow.set_tracking_uri("https://dagshub.com/VesnaPivac/ML_COVID19-Mexico.mlflow")

model_name = "LogisticRegressionModel"  # Nombre del modelo que se desee utilizar
model_version = 1                       # Versión del modelo que se desee utilizar
model_uri = f"models:/{model_name}/{model_version}"

model = mlflow.pyfunc.load_model(model_uri)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        df = pd.DataFrame(data)
        predictions = model.predict(df)
        return jsonify(predictions.tolist())
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)