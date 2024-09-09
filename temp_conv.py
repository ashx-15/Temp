from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML for the Temperature Converter
temperature_converter_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Temperature Converter</title>
    <script>
        async function convertTemperature() {
            const temp = document.getElementById('temp').value;
            const scale = document.getElementById('scale').value;
            const response = await fetch(`/convert_temperature?temp=${temp}&scale=${scale}`);
            const data = await response.json();
            document.getElementById('result').innerText = `Result: ${data.result || data.error}`;
        }
    </script>
</head>
<body>
    <h1>Temperature Converter</h1>
    <input type="number" id="temp" placeholder="Enter temperature" />
    <select id="scale">
        <option value="C">Celsius to Fahrenheit</option>
        <option value="F">Fahrenheit to Celsius</option>
    </select>
    <button onclick="convertTemperature()">Convert</button>
    <p id="result"></p>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(temperature_converter_html)

@app.route('/convert_temperature', methods=['GET'])
def convert_temperature():
    try:
        temp = float(request.args.get('temp'))
        scale = request.args.get('scale')
        
        if scale == 'C':
            converted = (temp * 9/5) + 32
            return jsonify({'result': f'{converted} F'})
        elif scale == 'F':
            converted = (temp - 32) * 5/9
            return jsonify({'result': f'{converted} C'})
        else:
            return jsonify({'error': 'Invalid scale. Use C or F.'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
