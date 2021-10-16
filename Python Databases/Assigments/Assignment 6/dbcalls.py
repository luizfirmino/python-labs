import sqlite3 as sql
import os 
from os import path

CONST_CURRENT_DIR = os.path.abspath(__file__)
CONST_DB_DIR = os.path.join(os.path.dirname(CONST_CURRENT_DIR), "roster.db")

def db_connect(dbfile):
   return sql.connect(dbfile)

def execSQL(conn, sql, params):
    try:
        cur = conn.cursor()
        return cur.execute(sql, params)
    except:
        conn.close()
        quit()

def getStudents():
    conn = db_connect(CONST_DB_DIR)
    result = execSQL(conn, "SELECT * FROM students","")
    rows = result.fetchall()
    conn.close()
    return rows

def updateStudent(request):

    nm = request.form['nm']
    addr = request.form['add']
    city = request.form['city']
    id = request.form['id']

    conn = db_connect(CONST_DB_DIR)

    # Verify if ID already exists
    result = execSQL(conn, "SELECT * FROM students WHERE id = ? ", [id])
    row = result.fetchone()

    # if Exists - UPDATE the register
    if row:
        conn.execute("UPDATE students SET name = ?, addr = ?, city = ? WHERE id = ?", [nm, addr, city, id])
        msg = "Record with id = " + id + " successfully updated"

    # Otherwise - ADD
    else:
        conn.execute("INSERT INTO students(name, addr, city, id) VALUES(?,?,?,?)", [nm, addr, city, id])
        msg = "Record with " + nm + " " + addr + " " + city + " " + id + " successfully added"

    conn.commit()
    conn.close()

    return msg


def findStudents(request):

    nm = request.form['nm']
    addr = request.form['add']
    city = request.form['city']

    args = []
    sql = "SELECT * FROM students WHERE 1=1 "

    if len(nm) > 0:
        sql = sql + " AND name LIKE ? "
        args.append("%" + str(nm) + "%")

    if len(addr) > 0:
        sql = sql + " AND addr LIKE ? "
        args.append("%" + str(addr) + "%")

    if len(city) > 0:
        sql = sql + " AND city LIKE ? "
        args.append("%" + str(city) + "%")

    conn = db_connect(CONST_DB_DIR)
    result = execSQL(conn, sql, args)
    rows = result.fetchall()
    conn.close()

    return rows


def deleteStudent(name):
    
    if len(name) > 0:
        
        conn = db_connect(CONST_DB_DIR)
        result = execSQL(conn, "SELECT * FROM students WHERE UPPER(name) = ? ", [name.upper()])
        row = result.fetchone()
        if row:
            conn.execute("DELETE FROM students WHERE id = ?", [row[3]])
            conn.commit()
            msg = [(row[0], row[1], row[2], row[3])]
        else:
            msg = ["No record found"]
        
        conn.close()
    else:
        msg = "Please enter a name"
    
    return msg