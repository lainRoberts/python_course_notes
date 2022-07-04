from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Function ran for {t2-t1} seconds') #TO SEE HOW LONG A FUNCTION TAKES TO EXECUTE
        return result
    return wrapper

@performance
def long_time():
    for i in range(10000000):
        i*5

long_time()
