import joblib
import numpy as np
from flask import Flask
from flask import jsonify

#inicializar la app
app = Flask(__name__)

#ruta
@app.route('/predict', methods = [ 'GET'])
def predict():
    X_test = np.array([0.00632,18.0,2.31,0.538,6.575,65.2,1,296.0,15.3,4.98])
    prediction = model.predict(X_test.reshape(1,-1))
    return jsonify({'prediction: ': list(prediction)})

#servidor
if __name__ == '__main__':
    model = joblib.load('./models/best_models.pkl')
    app.run(port = 8080)

