from functools import wraps
from DBcm import ConnectionError, CredentialsError, SQLError


def try_interact_with_database(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConnectionError as err:
            print('***** Is your database switched on? Error:', str(err))
        except CredentialsError as err:
            print('***** User-id/Password issues. Error:', str(err))
        except SQLError as err:
            print('***** Is your query correct? Error:', str(err))
        except Exception as err:
            print('***** Something went wrong:', str(err))
        return 'Error'
    return wrapper