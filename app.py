from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')
@app.route('/task1/', methods=['POST','GET'])
def task1():
    return render_template('task1.html')
if __name__ == "__main__":
    app.run(debug=True)

