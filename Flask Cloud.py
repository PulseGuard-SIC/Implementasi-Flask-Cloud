from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
import tensorflow as tf

app = Flask(__name__)
run_with_ngrok(app, authtoken='cr_2ioj7OJglRuHU4EYUlrcjy7kVLd')

model = tf.keras.models.load_model('C:/Users/namok/Desktop/AI_ML_Model.keras')

sensor_data = {"temperature": None, "heart_rate": None}

@app.route('/sensor', methods=['POST'])
def update_sensor_data():
    data = request.get_json()
    if data:
        if "temperature" in data and "heart_rate" in data:
            sensor_data["temperature"] = data["temperature"]
            sensor_data["heart_rate"] = data["heart_rate"]
            return jsonify({'message': 'Sensor data updated successfully'}), 200
        else:
            return jsonify({'message': 'Invalid sensor data format'}), 400
    else:
        return jsonify({'message': 'No data provided'}), 400

@app.route('/sensor', methods=['GET'])
def get_sensor_data():
    return jsonify(sensor_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
