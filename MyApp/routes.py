from MyApp import hello
from flask import url_for, render_template, request, redirect
from getpass import getpass
from mysql.connector import connect, Error, errorcode


try:
    connection = connect(user='root', password=getpass("Enter root's password: "),
                         host='127.0.0.1',
                         database='mydb',)
except Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


def num_of_times():
    return 3


@hello.route('/index')
def sayHello():
    a = "<p> under construction </p>"
    return a * num_of_times()


@hello.route('/nice/<name>')
def sayNiceDay(name):
    a = 'have a nice day, ' + name
    return a


@hello.route('/day')
@hello.route('/today')
def sayDay():
    a = "today is Thu"
    return a


@hello.route('/consume/<food>')
@hello.route('/eat/<food>')
def eat(food):
    a = 'i want to eat ' + food
    return a


@hello.route('/mypage')
def testHTML():
    pageName = "Welcome to my Home"
    cssName = url_for('static', filename='mystyle.css')
    person = {"username": "roy"}
    aurora_img = url_for('static', filename='images/Aurora.jpg')
    myList = [
        {
            'author': {'username': 'John'},
            'body': 'What a beautiful day!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'That was a great movie'

        }
    ]
    page = render_template('test.html', title=pageName, user=person, picName=aurora_img, posts=myList, mycssname=cssName)
    return page


# @hello.route('/mypage')
# def testHTML():
#     aurora_img = url_for('static', filename="images/Aurora.jpg")
#     page = '''
#     <html>
#         <head>
#             <title>My Home Page</title>
#         </head>
#         <br/>
#             <body>
#             <h1>Hello!</h1>
#             <hr/>
#             <p>This is a <b>paragraph</b></p>
#             <a href="/today"><img src = ''' + aurora_img + ''' alt = "aurora image" title = "aurora" width="112" height="160"/></a>
#         </body>
#     </html>'''
#     return page


# just for fun...
# @hello.route('/hello/')
# @hello.route('/hello/<name>')
# def hello(name=None):
#     # berry_image = url_for('static', filename='images/image001.jpg')
#     imageURL = url_for('static', filename='images/')  # interesting can use filename as file path to images
#     page = render_template('hello.html', name=name, imageURL=imageURL)
#     return page


@hello.route('/viewproduct/<jewel>/')
def viewproduct(jewel):
    jewel_image = url_for('static', filename='images/' + jewel + '.jpg')
    page = '''
    <html>
        <head>
            <title>''' + jewel + '''</title>
        </head>
        <h1>''' + jewel + '''</h1>
        <hr>
        <p>
        <a href = ''' + jewel_image + ''' target = "_blank">
        <img src = ''' + jewel_image + '''/ width="112" height="160"/></a></p>
    </html>
    '''
    return page


@hello.route('/addEmployee')
def addEmployee():
    pageName = "Add Employee"
    cssName = url_for('static', filename='addEmployee.css')
    page = render_template('addEmployee.html', title=pageName, cssStyleName=cssName)
    return page


# working
@hello.route('/viewEmployee')
def viewEmployee():
    view_table_sql = "SELECT * FROM employeeb;"
    cursor = connection.cursor()
    cursor.execute(view_table_sql)
    results = cursor.fetchall()
    page = render_template('viewEmployee.html', employees=results)
    return page


@hello.route('/form', methods=["POST"])
def form_handling():
    employee = (request.form.get('employeeName'),
                request.form.get('employeeEmail'),
                request.form.get('employeeMobile'),
                request.form.get('employeeDept'),
                request.form.get('employeeSalary'),
                request.form.get('employeeInsurance'))
    insert_record_to_table_sql = f"INSERT INTO employeeb (name, email, mobile, department, salary, insurance_policy_no) VALUES {employee};"
    cursor = connection.cursor()
    cursor.execute(insert_record_to_table_sql)
    connection.commit()
    cursor.close()
    return redirect(url_for('viewEmployee'))


@hello.route('/edit_employee/<employee_id>/', methods=['POST'])
def editEmployee(employee_id):
    view_employee_sql = f"SELECT * FROM employeeb WHERE employee_id = {employee_id};"
    cursor = connection.cursor()
    cursor.execute(view_employee_sql)
    results = cursor.fetchall()
    name = results[0][1]
    email = results[0][2]
    mobile = results[0][3]
    dept = results[0][4]
    salary = results[0][5]
    insure = results[0][6]
    page = render_template('editEmployee.html', emp_id=employee_id, emp_name=name, emp_email=email, emp_mobile=mobile, emp_dept=dept, emp_salary=salary, emp_insure=insure)
    return page


@hello.route('/update_employee/<employee_id>/', methods=['POST'])
def submitEmployeeUpdate(employee_id):
    name = request.form.get('employeeName')
    email = request.form.get('employeeEmail')
    mobile = request.form.get('employeeMobile')
    dept = request.form.get('employeeDept')
    salary = request.form.get('employeeSalary')
    insure = request.form.get('employeeInsurance')
    update_employee_sql = f"UPDATE employeeb SET name='{name}', email='{email}', mobile={mobile}, department='{dept}', salary={salary}, insurance_policy_no='{insure}' \
                            WHERE employee_id={employee_id};"
    cursor = connection.cursor()
    cursor.execute(update_employee_sql)
    connection.commit()
    cursor.close()
    return redirect(url_for('viewEmployee'))


@hello.route('/delete_employee/<employee_id>/', methods=['POST'])
def deleteEmployee(employee_id):
    delete_record_sql = f"DELETE FROM employeeb WHERE employee_id={employee_id};"
    cursor = connection.cursor()
    cursor.execute(delete_record_sql)
    connection.commit()
    cursor.close()
    return redirect(url_for('viewEmployee'))
