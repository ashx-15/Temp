from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ''
    if request.method == 'POST':
        try:
            # Extract values from the form
            num1 = float(request.form.get('num1', 0))
            num2 = float(request.form.get('num2', 0))
            operation = request.form.get('operation')

            # Perform the calculation based on the operation
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = 'Error: Division by zero'
            else:
                result = 'Error: Invalid operation'
        except ValueError:
            result = 'Error: Invalid input'

    # HTML template
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Calculator</title>
    </head>
    <body>
        <h1>Simple Calculator</h1>
        <form method="post">
            <label for="num1">Number 1:</label>
            <input type="text" id="num1" name="num1" required><br><br>
            
            <label for="num2">Number 2:</label>
            <input type="text" id="num2" name="num2" required><br><br>
            
            <label for="operation">Operation:</label>
            <select id="operation" name="operation" required>
                <option value="add">Add</option>
                <option value="subtract">Subtract</option>
                <option value="multiply">Multiply</option>
                <option value="divide">Divide</option>
            </select><br><br>
            
            <input type="submit" value="Calculate">
        </form>
        <h2>Result:</h2>
        <p>{{ result }}</p>
    </body>
    </html>
    '''

    return render_template_string(html, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
