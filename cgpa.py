from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML for the CGPA Calculator
cgpa_calculator_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CGPA Calculator</title>
    <script>
        async function calculateCGPA() {
            const grades = document.getElementById('grades').value.split(',').map(Number);
            const credits = document.getElementById('credits').value.split(',').map(Number);
            const queryString = `grades=${grades.join('&grades=')}&credits=${credits.join('&credits=')}`;
            
            const response = await fetch(`/calculate_cgpa?${queryString}`);
            const data = await response.json();
            document.getElementById('result').innerText = `CGPA: ${data.result || data.error}`;
        }
    </script>
</head>
<body>
    <h1>CGPA Calculator</h1>
    <input type="text" id="grades" placeholder="Enter grades (comma separated)" />
    <input type="text" id="credits" placeholder="Enter credits (comma separated)" />
    <button onclick="calculateCGPA()">Calculate CGPA</button>
    <p id="result"></p>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(cgpa_calculator_html)

@app.route('/calculate_cgpa', methods=['GET'])
def calculate_cgpa():
    try:
        grades = request.args.getlist('grades', type=float)
        credits = request.args.getlist('credits', type=float)
        
        if len(grades) != len(credits) or len(grades) == 0:
            return jsonify({'error': 'Invalid input. Ensure that grades and credits lists are of equal length and not empty.'})
        
        total_points = sum(g * c for g, c in zip(grades, credits))
        total_credits = sum(credits)
        
        cgpa = total_points / total_credits
        return jsonify({'result': f'{cgpa:.2f}'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
