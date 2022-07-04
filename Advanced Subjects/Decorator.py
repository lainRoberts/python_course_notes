#Decorator
def my_decorator(func):
    def wrap_func(x):
        print('********decoration********')
        func(x)
        print('********decoration********')
    return wrap_func

@my_decorator
def hello(greetings):
    print(greetings)
hello('hi')



#hello2 = my_decorator(hello)()  # or... my_decorator(hello)()
#hello2()