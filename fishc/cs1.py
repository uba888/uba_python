class Hello(object):
    def __init__(self):
        print("Test")
 
@classmethod
def print_hello(cls):
    print("Hello")
Hello.print_hello()

