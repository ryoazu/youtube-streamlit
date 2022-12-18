from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello</h1>'

@app.route('/hello')
def hello():
    return '<h1>こんにちは</h1>'

@app.route('/hello/<string:string1>/<string:string2>')
def show_string(string1, string2):
    return 'こんにちは{}さん、{}さん '.format(string1, string2)

@app.route('/add/<int:num1>/<int:num2>')
def add_num(num1, num2):
    num = num1 + num2
    return '<h1>{}</h1>'.format(num)

@app.route('/div/<float:num1>/<float:num2>')
def div_num(num1, num2):
    num = num1 // num2
    return '<h1>{}</h1>'.format(num)

if __name__ == '__main__':
    app.run(debug = True)