import mysql.connector


class ConnectionError(Exception):
    pass


class CredentialsError(Exception):
    pass


class SQLError(Exception):
    pass


"""Context management class which implements Python's context management 
protocol. This class conforms the Context Management Protocol because it 
overrides the following dunder methods: __init__, __enter__, __exit__.
This class can used with the Python's with statement."""
class UseDatabase:
    
    def __init__(self, config: dict) -> None:
        self.configuration = config
    
    def __enter__(self) -> 'cursor':
        """If an exception is raised while __enter__ is executiong, the with 
        statement terminates, and any subsequent processing of __exit__ 
        is CANCELLED."""
        try:
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsError(err)
        except mysql.connector.errors.DatabaseError as err:
            raise ConnectionError(err)
    
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        """__exit__ is guaranteed to execute whenever the with's sute
        terminates"""
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)