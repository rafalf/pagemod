def log(f):
    def wrapper(*args, **kwargs):
        print('Method: {} before with args: {}'.format(f.__name__, args[1:]))
        f(*args, **kwargs)
        print('Method: {} after --> OK'.format(f.__name__))

    return wrapper