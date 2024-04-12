import mysql.connector

class Connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None
        self.connect()
        
    def connect(self):
        self.cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)

    def close(self):
        self.cnx.close()

    def execute_query(self, query, params):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        self.cnx.commit()
        cursor.close()
        return cursor

    def execute_read_query(self, query, params):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result

class DaoCity:
    def __init__(self, connection):
        self.connection = connection

    def get_all(self):
        query = 'SELECT * FROM cities'
        return self.connection.execute_read_query(query, ())

    def get_by_id(self, id):
        query = 'SELECT * FROM cities WHERE id = %s'
        return self.connection.execute_read_query(query, (id,))

    def __init__(self, connection):
        self.connection = connection

    def insert(self, cities):
        query = 'INSERT INTO cities (name, status) VALUES (%s, %s)'
        return self.connection.execute_query(query, (cities.name, cities.status))
    
    def buscar(self, nombre):
        query = 'select * from cities where name = %s'
        return self.connection.execute_read_query(query, (nombre,))


    def update(self, cities):
        query = 'UPDATE cities SET name = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (cities.name, cities.status, cities.id))

    def delete(self, id):
        query = 'DELETE FROM cities WHERE id = %s'
        return self.connection.execute_query(query, (id,))


class Daojob:
    def __init__(self, connection):
        self.connection = connection

    def get_all(self):
        query = 'SELECT * FROM job'
        return self.connection.execute_read_query(query, ())

    def get_by_id(self, id):
        query = 'SELECT * FROM job WHERE id = %s'
        return self.connection.execute_read_query(query, (id,))

    def __init__(self, connection):
        self.connection = connection

    def insert(self, job):
        query = 'INSERT INTO job (name, status) VALUES (%s, %s)'
        return self.connection.execute_query(query, (job.name, job.status))
    
    def buscar(self, nombre):
        query = 'select * from job where name = %s'
        return self.connection.execute_read_query(query, (nombre,))


    def update(self, job):
        query = 'UPDATE job SET name = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (job.name, job.status, job.id))

    def delete(self, id):
        query = 'DELETE FROM job WHERE id = %s'
        return self.connection.execute_query(query, (id,))



class DaoEmployee :
    def __init__(self, connection):
        self.connection = connection

    def get_all(self):
        query = 'SELECT * FROM Employee'
        return self.connection.execute_read_query(query, ())

    def get_by_id(self, id):
        query = 'SELECT * FROM Employee WHERE id = %s'
        return self.connection.execute_read_query(query, (id,))

    def __init__(self, connection):
        self.connection = connection

    def insert(self, Employee):
        query = 'INSERT INTO Employee (name, ciudad_id, job_id, salary, status) VALUES (%s,%s,%s,%s, %s)'
        return self.connection.execute_query(query, (Employee.name, Employee.ciudad_id, Employee.job_id, Employee.salary, Employee.status))
     
    def buscar(self, Employee):
        query = 'select * from Employee where name = %s'
        return self.connection.execute_read_query(query, (Employee.name, Employee.ciudad_id, Employee.job_id, Employee.salary, Employee.status))


    def update(self, Employee):
       query = 'update employee set (name,ciudad_id, job_id, salary, status) VALUES (%s,%s,%s,%s, %s)where id=%s'
       return self.connection.execute_query(query, (Employee.name, Employee.ciudad_id, Employee.job_id, Employee.salary, Employee.status))

    def delete(self, Employee):
        query = 'DELETE FROM Employee WHERE ciudad_id = %s'
        return self.connection.execute_query(query, (Employee.name, Employee.ciudad_id, Employee.job_id, Employee.salary, Employee.status,))
