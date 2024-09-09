from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML for the Calculator
calculator_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Calculator</title>
    <script>
        async function calculate() {
            const expression = document.getElementById('expression').value;
            const response = await fetch(`/calculate?expression=${encodeURIComponent(expression)}`);
            const data = await response.json();
            document.getElementById('result').innerText = `Result: ${data.result || data.error}`;
        }
    </script>
</head>
<body>
    <h1>Simple Calculator</h1>
    <input type="text" id="expression" placeholder="Enter expression (e.g., 2+2)" />
    <button onclick="calculate()">Calculate</button>
    <p id="result"></p>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(calculator_html)

@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        expression = request.args.get('expression')
        result = eval(expression)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
