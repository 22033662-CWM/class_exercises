from MyApp import hello


@hello.route('/monkey')
def sayHello():
    a = "under construction"
    return a


@hello.route('/day')
def sayDay():
    a = "today is Thu"
    return a
    