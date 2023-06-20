import mysql.connector

"""Context management class which implements Python's context management 
protocol. This class conforms the Context Management Protocol because it 
overrides the following dunder methods: __init__, __enter__, __exit__.
This class can used with the Python's with statement."""
class UseDatabase:
    
    def __init__(self, config: dict) -> None:
        self.configuration = config
    
    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def __exit__(self, exe_type, exe_value, exe_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()