import os.path
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os
import socket

# Definition for GET request to get status of task >>> TO BE DELETED
# def get_task_status(taskID):
#     conn = sqlite3.connect('tasks.db')
#     cursor = conn.cursor()
#     task_status=cursor.execute("SELECT status FROM tasks WHERE id = ?", (taskID,)).fetchall()
#     cursor.close()
#     conn.close()
#     return task_status

# Definition for POST request to update status of task
def update_task_status(taskID, status):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = ?  WHERE id = ?', (status, taskID,))
    conn.commit()
    cursor.close()
    conn.close()

# Definition for creating tasks
def add_new_task(taskID, status):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO tasks VALUES (?, ?)', (taskID, status,))
    conn.commit()
    cursor.close()
    conn.close()

def enable_all_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = 1  WHERE status = 0')
    conn.commit()
    cursor.close()
    conn.close()

def disable_all_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = 0  WHERE status = 1')
    conn.commit()
    cursor.close()
    conn.close()

# Flask init
app = Flask(__name__)
tasks_db=('tasks.db') #Flask DB config

# Create tasks table if not exist
conn=sqlite3.connect('tasks.db')
conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status INTEGER)
            """)
cursor=conn.cursor()
cursor.execute('UPDATE first_run SET status=1 WHERE id=1;')
cursor.close()
conn.commit()

for tasks_id in range (11):
    tasks_id = str(tasks_id)
    add_new_task(tasks_id,'1')
    enable_all_tasks()
os.system('./breakLab.sh')

# SQLite flask configuration
# This is redundant as above definitions exist
# Still to decide which style to use

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tasks.db'
db = SQLAlchemy(app)


# Flask routes
@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        # We run scrip to clear all tasks as HOME page should have button to clear or enable all tasks.
        # POST should send id and status. Task ID on home page must be 0 and it should be used
        # to 'fix' lab (status 0) or 'break' the lab (status 1)

        # Class way: Alternative method is to assign Tasks class to variable and use db.session to commit.
        # Example inline:
        task_status=(request.form.get("task_status"))
        if task_status == '1':
            enable_all_tasks()
            os.system('./breakLab.sh')
            print('Breaking LAB')
        elif task_status == '0':
            disable_all_tasks()
            os.system('./fixLab.sh')
            print('Fixing LAB')
        return redirect('/')
    elif request.method == 'GET':
        host=socket.gethostname()
        sshconn='10.48.26.76:2317'
        if host in 'TSOPREK-M-C25E':
            sshconn='href=ssh://127.0.0.1'
            return render_template('home.html', sshconn=sshconn)
        elif host == 'bootcamp1':
            sshconn = 'href=ssh://tetraining@10.48.26.76:2317'
            return render_template('home.html', sshconn=sshconn)
        elif host == 'bootcamp2':
            sshconn = 'href=ssh://tetraining@10.48.26.76:2318'
            return render_template('home.html', sshconn=sshconn)
        elif host == 'bootcamp3':
            sshconn = 'href=ssh://tetraining@10.48.26.76:2319'
            return render_template('home.html', sshconn=sshconn)
        elif host == 'bootcamp4':
            sshconn = 'href=ssh://tetraining@10.48.26.76:2320'
            return render_template('home.html', sshconn=sshconn)
        return render_template('home.html', sshconn=sshconn)

@app.route('/task1/', methods=['POST','GET'])
def task1():
    task_id = '1'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        print (task_status, type(task_status))
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./fixTeServ.sh')
        elif task_status == '1':
            os.system('./breakTeServ.sh')
        return redirect('/task1/')
    elif request.method == 'GET':
        return render_template('task1.html')

@app.route('/task2/', methods=['POST','GET'])
def task2():
    task_id = '2'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./fixID.sh')
        elif task_status == '1':
            os.system('./breakID.sh')
        return redirect('/task2/')
    elif request.method == 'GET':
        return render_template('task2.html')

@app.route('/task3/', methods=['POST','GET'])
def task3():
    task_id = '3'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./fixDNS.sh')
        elif task_status == '1':
            os.system('./breakDNS.sh')
        return redirect('/task3/')
    elif request.method == 'GET':
        return render_template('task3.html', )

@app.route('/task4/', methods=['POST','GET'])
def task4():
    task_id = '4'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./registryAccept.sh')
        elif task_status == '1':
            os.system('./registryDrop.sh')
        return redirect('/task4/')
    elif request.method == 'GET':
        return render_template('task4.html')

@app.route('/task5/', methods=['POST','GET'])
def task5():
    task_id = '5'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./fixCAcert.sh')
        elif task_status == '1':
            os.system('./breakCAcert.sh')
        return redirect('/task5/')
    elif request.method == 'GET':
        return render_template('task5.html')

@app.route('/task6/', methods=['POST','GET'])
def task6():
    task_id = '6'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./c1Accept.sh')
        elif task_status == '1':
            os.system('./c1Drop.sh')
        return redirect('/task6/')
    elif request.method == 'GET':
        return render_template('task6.html')

@app.route('/task7/', methods=['POST','GET'])
def task7():
    task_id = '7'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./dataAccept.sh')
        elif task_status == '1':
            os.system('./dataDrop.sh')
        return redirect('/task7/')
    elif request.method == 'GET':
        return render_template('task7.html')

@app.route('/task8/', methods=['POST','GET'])
def task8():
    task_id = '8'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./fixTestSSL.sh')
        elif task_status == '1':
            os.system('./breakTestSSL.sh')
        return redirect('/task8/')
    elif request.method == 'GET':
        return render_template('task8.html')

@app.route('/task9/', methods=['POST','GET'])
def task9():
    task_id = '9'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./fixNTP.sh')
        elif task_status == '1':
            os.system('./breakNTP.sh')
        return redirect('/task9/')
    elif request.method == 'GET':
        return render_template('task9.html')

@app.route('/task10/', methods=['POST','GET'])
def task10():
    task_id = '10'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            # os.system('./c1Accept.sh')
            print('Work in progress!')
        elif task_status == '1':
            # os.system('./c1Drop.sh')
            print('Work in progress!')
        return redirect('/task10/')
    elif request.method == 'GET':
        return render_template('task10.html')

@app.route('/solutionsT1/', methods=['POST','GET'])
def solutionT1():
    return render_template('solutionT1.html')

@app.route('/solutionsT2', methods=['POST','GET'])
def solutionT2():
    return render_template('solutionT2.html')

@app.route('/solutionsT3', methods=['POST','GET'])
def solutionT3():
    return render_template('solutionT3.html')

@app.route('/solutionsT4', methods=['POST','GET'])
def solutionT4():
    return render_template('solutionT4.html')

@app.route('/solutionsT5', methods=['POST','GET'])
def solutionT5():
    return render_template('solutionT5.html')

@app.route('/solutionsT6', methods=['POST','GET'])
def solutionT6():
    return render_template('solutionT6.html')

@app.route('/solutionsT7', methods=['POST','GET'])
def solutionT7():
    return render_template('solutionT7.html')

@app.route('/solutionsT8', methods=['POST','GET'])
def solutionT8():
    return render_template('solutionT8.html')

@app.route('/solutionsT9', methods=['POST','GET'])
def solutionT9():
    return render_template('solutionT9.html')

@app.route('/solutionsT10', methods=['POST','GET'])
def solutionT10():
    return render_template('solutionT10.html')

if __name__ == "__main__":
    app.run(debug=True)
