from crypt import methods
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    return "welcome!"

@app.route('/register')
def homepage():
    return render_template('register.html')

@app.route('/confirm', methods=['POST'])
def register():
    if request.method == 'POST':
        n = request.form.get('name')
        a = request.form.get('age')
        p = request.form.get('position')
        t = request.form.get('team')
        n1 = request.form.get('nation')
        return render_template('confirm.html',name=n, age=a, position=p, team=t, nation=n1)

if __name__ == "__main__":
    app.run(debug=True)
