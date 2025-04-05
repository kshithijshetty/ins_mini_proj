from flask import Flask, render_template, request
from dss import SimpleDSA

app = Flask(__name__)
dsa = SimpleDSA()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sign', methods=['POST'])
def sign():
    message = request.form['message']
    r, s = dsa.sign(message)
    return render_template('result.html', 
                         message=message,
                         r=hex(r),
                         s=hex(s),
                         action="sign")

@app.route('/verify', methods=['POST'])
def verify():
    message = request.form['message']
    r = int(request.form['r'], 16)
    s = int(request.form['s'], 16)
    is_valid = dsa.verify(message, r, s)
    return render_template('result.html', 
                         message=message,
                         r=hex(r),
                         s=hex(s),
                         is_valid=is_valid,
                         action="verify")

if __name__ == '__main__':
    app.run(debug=True)