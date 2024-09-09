from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def converter():
    result = ''
    if request.method == 'POST':
        try:
            temperature = float(request.form.get('temperature', 0))
            unit = request.form.get('unit')
            
            if unit == 'celsius':
                result = (temperature * 9/5) + 32  # Convert Celsius to Fahrenheit
                result = f'{result:.2f} Fahrenheit'
            elif unit == 'fahrenheit':
                result = (temperature - 32) * 5/9  # Convert Fahrenheit to Celsius
                result = f'{result:.2f} Celsius'
            else:
                result = 'Error: Invalid unit'
        except ValueError:
            result = 'Error: Invalid input'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
<!DOCTYPE html>
<html>
<head>
    <title>Temperature Converter</title>
</head>
<body>
    <h1>Temperature Converter</h1>
    <form method="post">
        <label for="temperature">Temperature:</label>
        <input type="text" id="temperature" name="temperature" required><br><br>
        
        <label for="unit">Unit:</label>
        <select id="unit" name="unit" required>
            <option value="celsius">Celsius to Fahrenheit</option>
            <option value="fahrenheit">Fahrenheit to Celsius</option>
        </select><br><br>
        
        <input type="submit" value="Convert">
    </form>
    <h2>Result:</h2>
    <p>{{ result }}</p>
</body>
</html>
