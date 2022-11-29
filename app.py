import os.path
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os

# Definition for GET request to get status of task
def get_task_status(taskID):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    task_status=cursor.execute("SELECT status FROM tasks WHERE id = ?", (taskID,)).fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return task_status

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
    cursor.execute('INSERT INTO tasks VALUES (?, ?)', (taskID, status,))
    conn.commit()
    cursor.close()
    conn.close()

def update_all_tasks_status(new_status, current_status):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = ?  WHERE status = ?', (new_status, current_status))
    conn.commit()
    cursor.close()
    conn.close()

# Flask init
app = Flask(__name__)
tasks_db=('tasks.db') #Flask DB config

# SQLite check if this is first run. If first run create table with tasks.

conn=sqlite3.connect('tasks.db')
first_run=conn.execute("SELECT status FROM first_run WHERE ID=1").fetchall()
for row in first_run:
    for i in row:
        first_run=i
        # print(first_run)
        # First run is expected to have ID 1 and status 0
        if first_run == 0:
            print('This is first run')
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
                tasks_id=str(tasks_id)
                add_new_task(tasks_id,)
        else:
            # print('You have been here before.')
            continue
conn.close()

# SQLite flask configuration
# This is redundant as above definitions exist
# Still to decide which style to use

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tasks.db'
db = SQLAlchemy(app)

class FirstRun(db.Model):
    status= db.Column(db.Integer, primary_key=True, default=0)

    def __init__(self,status):
        self.status = status

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status= db.Column(db.Integer, default=0)

    def __init__(self,id,status):
        self.id = id
        self.status = status

    def __repr__(self):
        return '<status %r>' % self.status


# Flask routes
@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        # We run scrip to clear all tasks as HOME page should have button to clear or enable all tasks.
        # POST should send id and status. Task ID on home page must be 0 and it should be used
        # to 'fix' lab (status 0) or 'break' the lab (status 1)

        # Class way: Alternative method is to assign Tasks class to variable and use db.session to commit.
        # Example inline:
        #task_id=request.form['id'] #this part os same for class and def ## Removing as decision is to HC code per page
        new_status=request.form['status']
        new_status=str(new_status)
        # Instead below update_task method we can do:
        #  task_status = Task(status=task_status)

        # def way: We update db with status and run .sh script
        if new_status == '0':
            current_status='1'
            update_all_tasks_status(new_status, current_status)
            os.system('./fixLab.sh')
        elif new_status == '1':
            current_status = '0'
            update_all_tasks_status(new_status, current_status)
            os.system('./breakLab.sh')
        # Class way of passing and committing data to db:
        # try:
        #   db.session.add(new_task)
        #   db.session.commit()
        return redirect('/')
    elif request.method == 'GET':
        task_status = get_task_status('0')
        return render_template('home.html', task_status=task_status )

@app.route('/task1/', methods=['POST','GET'])
def task1():
    task_id = '1'
    if request.method == 'POST':
        task_status = request.form['status']
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./fixTeServ.sh')
        elif task_status == '1':
            os.system('./breakTeServ.sh')
        return redirect('/task1/')
    elif request.method == 'GET':
        task_status=get_task_status(task_id)
        return render_template('task1.html', task_status=task_status )

@app.route('/task2/', methods=['POST','GET'])
def task2():
    task_id = '2'
    if request.method == 'POST':
        task_status = request.form['status']
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./fixID.sh')
        elif task_status == '1':
            os.system('./fixID.sh')
        return redirect('/task2/')
    elif request.method == 'GET':
        task_status=get_task_status(task_id)
        return render_template('task2.html', task_status=task_status)

@app.route('/task3/', methods=['POST','GET'])
def task3():
    task_id = '3'
    if request.method == 'POST':
        task_status = request.form['status']
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./fixDNS.sh')
        elif task_status == '1':
            os.system('./breakDNS.sh')
        return redirect('/task3/')
    elif request.method == 'GET':
        task_status=get_task_status(task_id)
        return render_template('task3.html', task_status=task_status)

@app.route('/task4/', methods=['POST','GET'])
def task4():
    task_id = '4'
    if request.method == 'POST':
        task_status = request.form['status']
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./registryAccept.sh')
        elif task_status == '1':
            os.system('./registryDrop.sh')
        return redirect('/task4/')
    elif request.method == 'GET':
        task_status=get_task_status(task_id)
        return render_template('task4.html', task_status=task_status)

@app.route('/task5/', methods=['POST','GET'])
def task5():
    task_id = '5'
    if request.method == 'POST':
        task_status = request.form['status']
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./fixCAcert.sh')
        elif task_status == '1':
            os.system('./breakCAcert.sh')
        return redirect('/task5/')
    elif request.method == 'GET':
        task_status=get_task_status(task_id)
        return render_template('task5.html', task_status=task_status)

@app.route('/task6/', methods=['POST','GET'])
def task6():
    task_id = '6'
    if request.method == 'POST':
        task_status = request.form['status']
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./c1Accept.sh')
        elif task_status == '1':
            os.system('./c1Drop.sh')
        return redirect('/task6/')
    elif request.method == 'GET':
        task_status=get_task_status(task_id)
        return render_template('task6.html', task_status=task_status)

@app.route('/task7/', methods=['POST','GET'])
def task7():
    task_id = '7'
    if request.method == 'POST':
        task_status = request.form['status']
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./c1Accept.sh')
        elif task_status == '1':
            os.system('./c1Drop.sh')
        return redirect('/task7/')
    elif request.method == 'GET':
        task_status=get_task_status(task_id)
        return render_template('task7.html', task_status=task_status)

@app.route('/task8/', methods=['POST','GET'])
def task8():
    task_id = '8'
    if request.method == 'POST':
        task_status = request.form['status']
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./c1Accept.sh')
        elif task_status == '1':
            os.system('./c1Drop.sh')
        return redirect('/task8/')
    elif request.method == 'GET':
        task_status=get_task_status(task_id)
        return render_template('task8.html', task_status=task_status)

@app.route('/task9/', methods=['POST','GET'])
def task9():
    task_id = '9'
    if request.method == 'POST':
        task_status = request.form['status']
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./c1Accept.sh')
        elif task_status == '1':
            os.system('./c1Drop.sh')
        return redirect('/task9/')
    elif request.method == 'GET':
        task_status=get_task_status(task_id)
        return render_template('task9.html', task_status=task_status)

@app.route('/task10/', methods=['POST','GET'])
def task10():
    task_id = '10'
    if request.method == 'POST':
        task_status = request.form['status']
        task_status = str(task_status)
        update_task_status(task_id, task_status)
        if task_status == '0':
            os.system('./c1Accept.sh')
        elif task_status == '1':
            os.system('./c1Drop.sh')
        return redirect('/task10/')
    elif request.method == 'GET':
        task_status=get_task_status(task_id)
        return render_template('task10.html', task_status=task_status)

@app.route('/solutionsT1/', methods=['POST','GET'])
def solutionT1():
    task_id = '1'
    task_status=get_task_status(task_id)
    return render_template('solutionT1.html', task_status=task_status)

@app.route('/solutionsT2', methods=['POST','GET'])
def solutionT2():
    task_id = '2'
    task_status=get_task_status(task_id)
    return render_template('solutionT2.html', task_status=task_status)

@app.route('/solutionsT3', methods=['POST','GET'])
def solutionT3():
    task_id = '3'
    task_status=get_task_status(task_id)
    return render_template('solutionT3.html', task_status=task_status)

@app.route('/solutionsT4', methods=['POST','GET'])
def solutionT4():
    task_id = '4'
    task_status=get_task_status(task_id)
    return render_template('solutionT4.html', task_status=task_status)

@app.route('/solutionsT5', methods=['POST','GET'])
def solutionT5():
    task_id = '5'
    task_status=get_task_status(task_id)
    return render_template('solutionT5.html', task_status=task_status)

@app.route('/solutionsT6', methods=['POST','GET'])
def solutionT6():
    task_id = '6'
    task_status=get_task_status(task_id)
    return render_template('solutionT6.html', task_status=task_status)

@app.route('/solutionsT7', methods=['POST','GET'])
def solutionT7():
    task_id = '7'
    task_status=get_task_status(task_id)
    return render_template('solutionT7.html', task_status=task_status)

@app.route('/solutionsT8', methods=['POST','GET'])
def solutionT8():
    task_id = '8'
    task_status=get_task_status(task_id)
    return render_template('solutionT8.html', task_status=task_status)

@app.route('/solutionsT9', methods=['POST','GET'])
def solutionT9():
    task_id = '9'
    task_status=get_task_status(task_id)
    return render_template('solutionT9.html', task_status=task_status)

@app.route('/solutionsT10', methods=['POST','GET'])
def solutionT10():
    task_id = '10'
    task_status=get_task_status(task_id)
    return render_template('solutionT10.html', task_status=task_status)

if __name__ == "__main__":
    app.run(debug=True)
