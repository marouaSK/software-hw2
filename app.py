from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # This line renders the HTML form

@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        num1 = float(request.form['num1'])  # Get num1 from the form
        num2 = float(request.form['num2'])  # Get num2 from the form
        result = num1 * num2  # Perform multiplication
        return f'The result of {num1} * {num2} is {result}.'
    except ValueError:
        return 'Please enter valid numbers.', 400

if __name__ == '__main__':
    app.run(debug=True)
