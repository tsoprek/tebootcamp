import os.path
from sqlite3 import OperationalError
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os.path

# Definition for GET request to get status of task
def get_task_status(taskID):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    print(cursor.execute("SELECT status FROM tasks WHERE id = ?", (taskID)).fetchall())
    conn.commit()
    cursor.close()
    conn.close()

# Definition for POST request to update status of task
def update_task_status(taskID, status):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = ?  WHERE id = ?', (status, taskID))
    conn.commit()
    cursor.close()
    conn.close()

# Definition for creating tasks
def add_new_task(taskID, status):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks VALUES (?, ?)', (taskID, status))
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
        print(first_run)
        # First run is expected to have ID 1 and status 0
        if first_run == 0:
            print('This is first run')
            conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status INTEGER)
            """)
            cursor=conn.cursor()
            cursor.execute('UPDATE first_run SET status=1 where status=0;')
            cursor.close()
            conn.commit()
            for task_id in range (11):
                task_id=str(task_id)
                add_new_task(task_id,0)
        else:
            print('You have been here before.')
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
        task_id=request.form['id'] #this part os same for class and def
        task_status=request.form['status']
        # Instead below update_task method we can do:
        #  task_status = Task(status=task_status)

        # def way: We update db with status
        update_task_status(task_id,task_status)

        # Class way of passing and committing data to db:
        # try:
        #   db.session.add(new_task)
        #   db.session.commit()

        return redirect('/')
    elif request.method == 'GET':
        task_status=get_task_status(0)
        return render_template('home.html'. )

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
