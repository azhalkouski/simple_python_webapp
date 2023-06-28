from functools import wraps


def try_interact_with_file(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            print('***** Failed to write to file:', str(err))
        return 'Error'
    return wrapper