import os.path
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os
import socket
import subprocess
import re

read_lab_config= open ('lab_config', 'r')
dns_server_re= re.findall("^dns_server=.*", read_lab_config.read())
dns_server=(dns_server_re[0])[11:]
print (dns_server)
read_lab_config= open ('lab_config', 'r')
ntp_server_re= re.findall("ntp_server=.*", read_lab_config.read())
ntp_server=(ntp_server_re[0])[11:]
print (ntp_server)


# Definition for GET request to get status of task >>> TO BE DELETED
def get_task_status(table, taskID):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    task_status=cursor.execute('SELECT status FROM {} WHERE id = ?'.format(table), (taskID,)).fetchall()
    cursor.close()
    conn.close()
    return (str(task_status[0][0]))


# Definition for POST request to update status of task
def update_task_status(table, taskID, status):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE {} SET status = ?  WHERE id = ?'.format(table), (status, taskID,))
    conn.commit()
    cursor.close()
    conn.close()


# Definition for creating tasks
def add_new_task(table, taskID, status):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO {} VALUES (?, ?)'.format(table), (taskID, status,))
    conn.commit()
    cursor.close()
    conn.close()


# Definition for creating quiz
def add_new_quiz(qqid, answer):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO quiz VALUES (?, ?)', (qqid, answer,))
    conn.commit()
    cursor.close()
    conn.close()


def enable_all_tasks(table):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE {} SET status = 1  WHERE status = 0'.format(table))
    conn.commit()
    cursor.close()
    conn.close()


def disable_all_tasks(table):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE {} SET status = 0  WHERE status = 1'.format(table))
    conn.commit()
    cursor.close()
    conn.close()


def return_status(table, task_id):
    task_status = get_task_status(table, task_id)
    if task_status == '0':
        status = 'DISABLED'
        return status
    elif task_status == '1':
        status = 'ENABLED'
        return status
    else:
        print('Failed to get task status!')


def task_validation_status(return_status):
    if return_status == '0':
        status = 'RESOLVED'
        return status
    elif return_status == '1':
        status = 'UNRESOLVED'
        return status
    elif return_status == '2':
        status = "PARTIALLY"
        return status
    else:
        print('Failed to get task status!')


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
print(get_ip())

# Flask init
app = Flask(__name__)
tasks_db=('tasks.db') #Flask DB config

# Create tasks table if not exist
conn=sqlite3.connect('tasks.db')
cursor=conn.cursor()
conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status INTEGER)
            """)
cursor.close()
conn.commit()

# Create tasks table if not exist
conn=sqlite3.connect('tasks.db')
cursor=conn.cursor()
conn.execute("""
            CREATE TABLE IF NOT EXISTS quiz ( 
            qid INTEGER PRIMARY KEY AUTOINCREMENT,
            qstatus INTEGER)
            """)
cursor.close()
conn.commit()

total_tasks = 12
tasks_tbl = 'tasks'
quiz_tbl = 'quiz'

master_task = get_task_status(tasks_tbl, '0')
if master_task == '1':
    update_task_status(tasks_tbl, '0', '0')
    for tasks_id in range(total_tasks):
        tasks_id = str(tasks_id)
        add_new_task( tasks_tbl, tasks_id, '1')
    dns_task=get_task_status(tasks_tbl, '3')
    if dns_task == '1':
        enable_all_tasks('tasks')
        os.system('./fixTask3.sh')
        os.system('./breakLab.sh')

quiz_master_task=get_task_status(tasks_tbl, '0')
if quiz_master_task == '1':
    for quiz_question in range(total_tasks):
        quiz_question = str(quiz_question)
        add_new_quiz(quiz_question, '1')

# SQLite flask configuration
# This is redundant as above definitions exist
# Still to decide which style to use

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tasks.db'
db = SQLAlchemy(app)


# Flask routes
@app.route('/', methods=['POST', 'GET'])
def home():
    task_id = '0'
    if request.method == 'POST':
        # We run scrip to clear all tasks as HOME page should have button to clear or enable all tasks.
        # POST should send id and status. Task ID on home page must be 0 and it should be used
        # to 'fix' lab (status 0) or 'break' the lab (status 1)

        # Class way: Alternative method is to assign Tasks class to variable and use db.session to commit.
        # Example inline:
        task_status=(request.form.get("task_status"))
        update_task_status(tasks_tbl, task_id, task_status)
        if task_status == '1':
            enable_all_tasks(tasks_tbl)
            os.system('./breakLab.sh')
        elif task_status == '0':
            disable_all_tasks(tasks_tbl)
            os.system('./fixLab.sh')
        return redirect('/')
    elif request.method == 'GET':
        host=socket.gethostname()
        IPAddr = get_ip()
        sshconn = 'href=ssh://tetraining@' + IPAddr
        status = return_status(tasks_tbl, task_id)
        return render_template('home.html', sshconn=sshconn, status=status, dns_server, ntp_server)


@app.route('/task1/', methods=['POST', 'GET'])
def task1():
    task_id = '1'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        update_task_status(tasks_tbl, task_id, task_status)
        if task_status == '0':
            os.system('./fixTask1.sh')
            master_task = get_task_status(tasks_tbl, '0')
            if master_task == '1':
                update_task_status(tasks_tbl, '0','0')
        elif task_status == '1':
            os.system('./breakTask1.sh')
        return redirect('/task1/')
    elif request.method == 'GET':
        solution_status = subprocess.check_output('./task1Validation.sh')
        solution_status = solution_status.decode('utf-8').strip()
        # print(solution_status)
        status = task_validation_status(solution_status)
        if status == '0':
            update_task_status(tasks_tbl, '0', '0')
        return render_template('task1.html', status=status)


@app.route('/task2/', methods=['POST', 'GET'])
def task2():
    task_id = '2'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(tasks_tbl, task_id, task_status)
        if task_status == '0':
            os.system('./fixTask2.sh')
            master_task=get_task_status(tasks_tbl, '0')
            if master_task == '1':
                update_task_status(tasks_tbl, '0', '0')
        elif task_status == '1':
            os.system('./breakTask2.sh')
        return redirect('/task2/')
    elif request.method == 'GET':
        solution_status = subprocess.check_output('./task2Validation.sh')
        solution_status = solution_status.decode('utf-8').strip()
        # print(solution_status)
        status = task_validation_status(solution_status)
        if status == '0':
            update_task_status(tasks_tbl, '0', '0')
        return render_template('task2.html', status=status)


@app.route('/task3/', methods=['POST', 'GET'])
def task3():
    task_id = '3'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(tasks_tbl, task_id, task_status)
        if task_status == '0':
            os.system('./fixTask3.sh')
            master_task = get_task_status(tasks_tbl, '0')
            if master_task == '1':
                update_task_status(tasks_tbl, '0', '0')
        elif task_status == '1':
            os.system('./breakTask3.sh')
        return redirect('/task3/')
    elif request.method == 'GET':
        solution_status = subprocess.check_output('./task3Validation.sh')
        solution_status = solution_status.decode('utf-8').strip()
        # print(solution_status)
        status = task_validation_status(solution_status)
        if status == '0':
            update_task_status(tasks_tbl, '0', '0')
        return render_template('task3.html', status=status)


@app.route('/task4/', methods=['POST', 'GET'])
def task4():
    task_id = '4'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(tasks_tbl, task_id, task_status)
        if task_status == '0':
            os.system('./fixTask4.sh')
            master_task=get_task_status(tasks_tbl, '0')
            if master_task == '1':
                update_task_status(tasks_tbl, '0','0')
        elif task_status == '1':
            os.system('./breakTask4.sh')
        return redirect('/task4/')
    elif request.method == 'GET':
        solution_status = subprocess.check_output('./task4Validation.sh')
        solution_status = solution_status.decode('utf-8').strip()
        # print(solution_status)
        status = task_validation_status(solution_status)
        if status == '0':
            update_task_status(tasks_tbl, '0', '0')
        return render_template('task4.html', status=status)


@app.route('/task5/', methods=['POST', 'GET'])
def task5():
    task_id = '5'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(tasks_tbl, task_id, task_status)
        if task_status == '0':
            os.system('./fixTask5.sh')
            master_task=get_task_status(tasks_tbl, '0')
            if master_task == '1':
                update_task_status(tasks_tbl, '0', '0')
        elif task_status == '1':
            os.system('./breakTask5.sh')
        return redirect('/task5/')
    elif request.method == 'GET':
        solution_status = subprocess.check_output('./task5Validation.sh')
        solution_status = solution_status.decode('utf-8').strip()
        # print(solution_status)
        status = task_validation_status(solution_status)
        if status == '0':
            update_task_status(tasks_tbl, '0', '0')
        return render_template('task5.html', status=status)


@app.route('/task6/', methods=['POST', 'GET'])
def task6():
    task_id = '6'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(tasks_tbl, task_id, task_status)
        if task_status == '0':
            os.system('./fixTask6.sh')
            master_task=get_task_status(tasks_tbl, '0')
            if master_task == '1':
                update_task_status(tasks_tbl, '0', '0')
        elif task_status == '1':
            os.system('./breakTask6.sh')
        return redirect('/task6/')
    elif request.method == 'GET':
        solution_status = subprocess.check_output('./task6Validation.sh')
        solution_status = solution_status.decode('utf-8').strip()
        # print(solution_status)
        status = task_validation_status(solution_status)
        if status == '0':
            update_task_status(tasks_tbl, '0', '0')
        return render_template('task6.html', status=status)


@app.route('/task7/', methods=['POST', 'GET'])
def task7():
    task_id = '7'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(tasks_tbl, task_id, task_status)
        if task_status == '0':
            os.system('./fixTask7.sh')
            master_task=get_task_status(tasks_tbl, '0')
            if master_task == '1':
                update_task_status(tasks_tbl, '0', '0')
        elif task_status == '1':
            os.system('./breakTask7.sh')
        return redirect('/task7/')
    elif request.method == 'GET':
        solution_status = subprocess.check_output('./task7Validation.sh')
        solution_status = solution_status.decode('utf-8').strip()
        # print(solution_status)
        status = task_validation_status(solution_status)
        if status == '0':
            update_task_status(tasks_tbl, '0', '0')
        return render_template('task7.html', status=status)


@app.route('/task8/', methods=['POST', 'GET'])
def task8():
    task_id = '8'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(tasks_tbl, task_id, task_status)
        if task_status == '0':
            os.system('./fixTask8.sh')
            master_task=get_task_status(tasks_tbl, '0')
            if master_task == '1':
                update_task_status(tasks_tbl, '0', '0')
        elif task_status == '1':
            os.system('./breakTask8.sh')
        return redirect('/task8/')
    elif request.method == 'GET':
        solution_status = subprocess.check_output('./task8Validation.sh')
        solution_status = solution_status.decode('utf-8').strip()
        # print(solution_status)
        status = task_validation_status(solution_status)
        if status == '0':
            update_task_status(tasks_tbl, '0', '0')
        return render_template('task8.html', status=status)


@app.route('/task9/', methods=['POST', 'GET'])
def task9():
    task_id = '9'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(tasks_tbl, task_id, task_status)
        if task_status == '0':
            os.system('./fixTask9.sh')
            master_task=get_task_status(tasks_tbl, '0')
            if master_task == '1':
                update_task_status(tasks_tbl, '0', '0')
        elif task_status == '1':
            os.system('./breakTask9.sh')
        return redirect('/task9/')
    elif request.method == 'GET':
        solution_status = subprocess.check_output('./task9Validation.sh')
        solution_status = solution_status.decode('utf-8').strip()
        # print(solution_status)
        status = task_validation_status(solution_status)
        if status == '0':
            update_task_status(tasks_tbl, '0', '0')
        return render_template('task9.html', status=status)


@app.route('/task10/', methods=['POST', 'GET'])
def task10():
    task_id = '10'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(tasks_tbl, task_id, task_status)
        if task_status == '0':
            os.system('./fixTask10.sh')
            master_task=get_task_status(tasks_tbl, '0')
            if master_task == '1':
                update_task_status(tasks_tbl, '0', '0')
        elif task_status == '1':
            os.system('./breakTask10.sh')
        return redirect('/task10/')
    elif request.method == 'GET':
        solution_status = subprocess.check_output('./task10Validation.sh')
        solution_status = solution_status.decode('utf-8').strip()
        # print(solution_status)
        status = task_validation_status(solution_status)
        if status == '0':
            update_task_status(tasks_tbl, '0', '0')
        return render_template('task10.html', status=status)


@app.route('/task11/', methods=['POST', 'GET'])
def task11():
    task_id = '11'
    if request.method == 'POST':
        task_status = request.form.get('task_status')
        task_status = str(task_status)
        update_task_status(tasks_tbl, task_id, task_status)
        if task_status == '0':
            os.system('./fixTask11.sh')
            master_task=get_task_status(tasks_tbl, '0')
            if master_task == '1':
                update_task_status(tasks_tbl, '0', '0')
        elif task_status == '1':
            os.system('./breakTask11.sh')
        return redirect('/task11/')
    elif request.method == 'GET':
        status = return_status(tasks_tbl, task_id)
        return render_template('task11.html', status=status)


@app.route('/solutionsT1/', methods=['POST', 'GET'])
def solutionT1():
    solution_status=subprocess.check_output('./task1Validation.sh')
    solution_status= solution_status.decode('utf-8').strip()
    # print (solution_status)
    status = task_validation_status(solution_status)
    return render_template('solutionT1.html', status=status)


@app.route('/solutionsT2', methods=['POST', 'GET'])
def solutionT2():
    solution_status=subprocess.check_output('./task2Validation.sh')
    solution_status= solution_status.decode('utf-8').strip()
    # print (solution_status)
    status = task_validation_status(solution_status)
    return render_template('solutionT2.html', status=status)


@app.route('/solutionsT3', methods=['POST', 'GET'])
def solutionT3():
    solution_status=subprocess.check_output('./task3Validation.sh')
    solution_status= solution_status.decode('utf-8').strip()
    # print(solution_status)
    status = task_validation_status(solution_status)
    return render_template('solutionT3.html', status=status)


@app.route('/solutionsT4', methods=['POST', 'GET'])
def solutionT4():
    solution_status = subprocess.check_output('./task4Validation.sh')
    solution_status = solution_status.decode('utf-8').strip()
    # print(solution_status)
    status = task_validation_status(solution_status)
    return render_template('solutionT4.html', status=status)


@app.route('/solutionsT5', methods=['POST', 'GET'])
def solutionT5():
    solution_status = subprocess.check_output('./task5Validation.sh')
    solution_status = solution_status.decode('utf-8').strip()
    # print(solution_status)
    status = task_validation_status(solution_status)
    return render_template('solutionT5.html', status=status)


@app.route('/solutionsT6', methods=['POST', 'GET'])
def solutionT6():
    solution_status = subprocess.check_output('./task6Validation.sh')
    solution_status = solution_status.decode('utf-8').strip()
    # print(solution_status)
    status = task_validation_status(solution_status)
    return render_template('solutionT6.html', status=status)


@app.route('/solutionsT7', methods=['POST','GET'])
def solutionT7():
    solution_status = subprocess.check_output('./task7Validation.sh')
    solution_status = solution_status.decode('utf-8').strip()
    # print(solution_status)
    status = task_validation_status(solution_status)
    return render_template('solutionT7.html', status=status)


@app.route('/solutionsT8', methods=['POST','GET'])
def solutionT8():
    solution_status = subprocess.check_output('./task8Validation.sh')
    solution_status = solution_status.decode('utf-8').strip()
    # print(solution_status)
    status = task_validation_status(solution_status)
    return render_template('solutionT8.html', status=status)


@app.route('/solutionsT9', methods=['POST','GET'])
def solutionT9():
    solution_status = subprocess.check_output('./task9Validation.sh')
    solution_status = solution_status.decode('utf-8').strip()
    # print(solution_status)
    status = task_validation_status(solution_status)
    return render_template('solutionT9.html', status=status)


@app.route('/solutionsT10', methods=['POST','GET'])
def solutionT10():
    solution_status = subprocess.check_output('./task10Validation.sh')
    solution_status = solution_status.decode('utf-8').strip()
    # print(solution_status)
    status = task_validation_status(solution_status)
    return render_template('solutionT10.html', status=status)


@app.route('/solutionsT11', methods=['POST','GET'])
def solutionT11():
    return render_template('solutionT11.html')


if __name__ == "__main__":
    app.run(debug=True, ssl_context='adhoc')
