from MyApp import hello
from flask import url_for
from flask import render_template


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
    aurora_img = url_for('static', filename="images/Aurora.jpg")
    page = '''
    <html>
        <head>
            <title>My Home Page</title>
        </head>
        <br/>
            <body>
            <h1>Hello!</h1>
            <hr/>
            <p>This is a <b>paragraph</b></p>
            <a href="/today"><img src = ''' + aurora_img + ''' alt = "aurora image" title = "aurora" width="112" height="160"/></a>
        </body>
    </html>'''
    return page


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


@hello.route('/hello/')
@hello.route('/hello/<name>')
def hello(name=None):
    # berry_image = url_for('static', filename='images/image001.jpg')
    imageURL = url_for('static', filename='images/')  # interesting filename use as file path to images
    return render_template('hello.html', name=name, imageURL=imageURL)
