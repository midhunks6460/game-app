from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    result = compare_guess(guess)
    return jsonify({'result': result})

def compare_guess(guess):
    if guess == secret_number:
        return 'correct'
    elif guess < secret_number:
        return 'higher'
    else:
        return 'lower'

if __name__ == '__main__':
    app.run(debug=True)
