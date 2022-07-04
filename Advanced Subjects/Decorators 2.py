#Decorator
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('********decoration********')
        func(*args, **kwargs)
        print('********decoration********')
    return wrap_func

@my_decorator
def hello(greetings, emoji=':D'):
    print(greetings, emoji 
    )
hello('hi')



#hello2 = my_decorator(hello)()  # or... my_decorator(hello)()
#hello2()