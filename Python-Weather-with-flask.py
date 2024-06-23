from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

def get_weather(city):
    city = city.replace(' ', '+')
    url = f'http://wttr.in/{city}?format=3'
    response = requests.get(url)

    if response.status_code == 200:
        return response.text.strip()
    else:
        return 'City not found or service unavailable.'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
    return render_template_string(TEMPLATE, weather=weather)

TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }

        .container {
            text-align: center;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        form {
            margin-bottom: 20px;
        }

        input[type='text'] {
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            width: 80%;
        }

        button {
            padding: 10px 20px;
            background-color: #007BFF;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 20px; /* Add margin-top to move the button down */
        }

        button:hover {
            background-color: #0056b3;
        }

        .weather {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class='container'>
        <h1>Weather App</h1>
        <form method='post'>
            <input type='text' name='city' placeholder='Enter city name' required>
            <button type='submit'>Get Weather</button>
        </form>
        {% if weather %}
        <div class='weather'>
            <h2>{{ weather }}</h2>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
