from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/task1/', methods=['POST','GET'])
def task1():
    return render_template('task1.html')

@app.route('/task2/', methods=['POST','GET'])
def task2():
    return render_template('task2.html')

@app.route('/task3/', methods=['POST','GET'])
def task3():
    return render_template('task3.html')

@app.route('/task4/', methods=['POST','GET'])
def task4():
    return render_template('task4.html')

@app.route('/task5/', methods=['POST','GET'])
def task5():
    return render_template('task5.html')

@app.route('/task6/', methods=['POST','GET'])
def task6():
    return render_template('task6.html')

@app.route('/solutions/T1', methods=['POST','GET'])
def solutionT1():
    return render_template('solutionT1.html')

@app.route('/solutions/T2', methods=['POST','GET'])
def solutionT2():
    return render_template('solutionT2.html')

@app.route('/solutions/T3', methods=['POST','GET'])
def solutionT3():
    return render_template('solutionT3.html')

@app.route('/solutions/T4', methods=['POST','GET'])
def solutionT4():
    return render_template('solutionT4.html')

@app.route('/solutions/T5', methods=['POST','GET'])
def solutionT5():
    return render_template('solutionT5.html')

@app.route('/solutions/T6', methods=['POST','GET'])
def solutionT6():
    return render_template('solutionT6.html')

@app.route('/solutions/T7', methods=['POST','GET'])
def solutionT7():
    return render_template('solutionT7.html')


if __name__ == "__main__":
    app.run(debug=True)

