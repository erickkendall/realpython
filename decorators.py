def do_twice(func):
    def wrapper_do_twice(*args,**kargs):
        func(*args,**kargs)
        return func(*args,**kargs)
    return wrapper_do_twice
