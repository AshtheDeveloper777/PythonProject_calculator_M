from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# Math functions
def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))
def tan(x): return math.tan(math.radians(x))
def sqrt(x): return math.sqrt(x)
def log(x): return math.log10(x)
def ln(x): return math.log(x)

ALLOWED = {
    'sin': sin, 'cos': cos, 'tan': tan,
    'sqrt': sqrt, 'log': log, 'ln': ln,
    'pi': math.pi, 'e': math.e
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expr = request.json.get('expression', '')
    try:
        # Safely evaluate the expression
        result = eval(expr, {"__builtins__": None}, ALLOWED)
        return jsonify(result=str(result))
    except:
        return jsonify(result="Error")
