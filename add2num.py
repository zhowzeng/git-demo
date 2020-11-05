import time

def timer(func):
    def wrap(*args, **kwargs):
        s = time.time()
        func(*args, **kwargs)
        t = time.time()
        print(f'spend {t - s}')
    return wrap

@timer
def addnum(a,b):
    print(f'{a} + {b} = {a+b}')
    return None

addnum(3,5)
