def decorate(func):
    def decorated():
        print "Before"
        func()
        print "After"
    return decorated


@decorate
def a_function():
    print "I'm a function"


a_function()
