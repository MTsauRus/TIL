from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hgr():
    return 'Hello World!'

@app.route('/hgr', methods = ['GET'])
def hgr2():
    return render_template('hgr.html')

@app.route('/login', methods = ['GET'])
def login():
    return render_template('loginform.html')

@app.route('/login', methods = ['POST'])
def login_post():
    id = request.form['id']
    print(f'id = {id}')
    return render_template('loginresult.html', id=id) # model

if __name__ == '__main__':
    app.run(debug=True, port=8080)