import json
import random
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='static', template_folder='templates')

def generate_random_gas_levels():
    return {
        "CO2": f"{random.randint(300, 500)} ppm",
        "O2": f"{random.randint(20, 25)}%",
        "N": f"{random.randint(75, 80)}%"
    }

def generate_random_air_quality():
    return {
        "AQI": random.randint(50, 150),
        "PM2_5": f"{random.randint(10, 50)} µg/m³",
        "PM10": f"{random.randint(20, 80)} µg/m³",
        "Ozone": f"{random.randint(50, 100)} ppb"
    }

@app.route('/')
def index():
    gas_levels = generate_random_gas_levels()
    air_quality = generate_random_air_quality()
    return render_template('index.html', gas_levels=gas_levels, air_quality=air_quality)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(debug=True)
