def f4(*args):
    print(type(args))
    print(args)

def f5(**kwargs):
    print(type(kwargs))
    print(kwargs)

def f6(*,a,b=100):
    return a+b
