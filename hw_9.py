import csv
import os
import sqlite3

def create_connection(db_file):
    if os.path.exists(db_file):
        os.remove(db_file)        
    conn = sqlite3.connect(db_file)
    print('The new database has been created...')
    return conn
    
def create_table(conn):
    cursor = conn.cursor()
    cursor.executescript("""
                    CREATE TABLE Project
                    (name TEXT PRIMARY KEY,
                     description TEXT,
                     deadline TEXT);
                    
                    CREATE TABLE Tasks
                    (id NUMBER PRIMARY KEY,
                     priority INTEGER,
                     details TEXT,
                     status TEXT,
                     completed DATE,
                     deadline TEXT,
                     project TEXT)""")
    conn.commit()
    print("Table has been created...")
 
def import_data(conn, csv_1, csv_2):
    cursor = conn.cursor()
    with open(csv_1) as data:
               data_to_project = csv.DictReader(data)
               data_to_db_project = [(i['name'], i['description'], i['deadline']) for i in data_to_project]
               for i in data_to_db_project:
                   cursor.execute("INSERT INTO Project (name, description, deadline) VALUES (?,?,?)", i)
                              
    with open(csv_2) as data:
               data_to_tasks = csv.DictReader(data)
               data_to_db_tasks = [(i['id'], i['priority'], i['details'], i['status'], i['completed'], i['deadline'], i['project']) for i in data_to_tasks]
               for j in data_to_db_tasks:
                   cursor.execute("INSERT INTO Tasks (id, priority, details, status, completed, deadline, project) VALUES (?,?,?,?,?,?,?)", j)                
    conn.commit()
                      
def select_project(conn, project_name='first'):
    cursor = conn.cursor()
    cursor.execute("""
            SELECT * FROM Tasks
            WHERE project = ?""", [project_name])    
    result = cursor.fetchall()
    for row in result:
        print('Id:        ', row[0])
        print('Priority:  ', row[1])
        print('Details:   ', row[2])
        print('Status:    ', row[3])
        print('Completed: ', row[4])
        print('Deadline:  ', row[5])
        print('Project:   ', row[6])        
    conn.close()
    
def main():
    database = "./sqlite.db"
    csv_1 = "./csv_1.csv"
    csv_2 = "./csv_2.csv"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        import_data(conn, csv_1, csv_2)
        select_project(conn)
    else:
        print('ERROR! can not create the connection....')
    
if __name__ == '__main__':
    main()