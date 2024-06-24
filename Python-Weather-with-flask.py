from flask import Flask, request, render_template_string
from requests import get
import os

app = Flask(__name__)

def get_weather(city):
    city = city.replace(' ', '+')
    url = f'http://wttr.in/{city}?format=2'
    response = get(url)

    if response.status_code == 200:
        return response.text.strip()
    else:
        return 'Error: City not found or service unavailable.'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    error = None
    
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        
        if 'Error' in weather:
            error = weather
            weather = None

    template_path = os.path.join('C:/Users/ABC/Desktop/VsCode Projects/Python Projects/Python-Weather-With-Flask', 'weather_template.html')

    try:
        with open(template_path, 'r') as file:
            template = file.read()
    except FileNotFoundError:
        return "Error: Template file not found", 500
    
    return render_template_string(template, weather=weather, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
