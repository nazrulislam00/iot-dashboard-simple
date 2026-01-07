from flask import Flask, jsonify

app = Flask(__name__)

sensor_data = {
    "temperature": 26,
    "humidity": 60,
    "status": "online"
}

@app.route("/data")
def data():
    return jsonify(sensor_data)

if __name__ == "__main__":
    app.run(debug=True)
