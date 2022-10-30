import sqlite3
from sqlite3 import Error 

#creates a connection to the db file
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

#creates a table in the database
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

#function to insert a new project into projects table.
def create_project(conn, project):


    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id:
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date) VALUES (?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql,project)
    conn.commit()
    return cur.lastrowid

#create a new task
def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return: task_id
    """
    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date) VALUES (?,?,?,?,?,?)
    '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

    return cur.lastrowid


#create a new project
# project = ('Test App with SQLite and Python','2015-01-01','2015-01-15')
# project_id = f.create_project(conn,project)
