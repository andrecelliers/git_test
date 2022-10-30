import sqlite3
from sqlite3 import Error
import function1 as f

sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                begin_date text,
                                end_date text
                                ); """

sql_create_tasks_table = """ CREATE TABLE IF NOT EXISTS tasks (
                            id integer PRIMARY KEY,
                            name text NOT NULL,
                            priority integer,
                            status_id integer NOT NULL,
                            project_id integer NOT NULL,
                            begin_date text NOT NULL,
                            end_date text NOT NULL,
                            FOREIGN KEY (project_id) REFERENCES projects (id)
                            );"""

def main():
    database = r"sqlitepython.db"
    # create a database connection
    conn = f.create_connection(database)
    # create tables
    if conn is not None:
        f.create_table(conn, sql_create_projects_table)
        f.create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")
    
    with conn:
        #tasks
        task_1 = ('Analyze the requirements of the app',1,1, 6, '2015-01-01','2015-01-02')
        task_2 = ('Confirm with user about the top requirements', 1,1, 6, '2015-01-03','2015-01-05')

        #create tasks, 
        f.create_task(conn, task_1)
        f.create_task(conn, task_2)

if __name__ == '__main__':
    main()