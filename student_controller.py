from db import get_db


def insert_student(name, lastname):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO students(name, lastname) VALUES (?, ?)"
    cursor.execute(statement, [name, lastname])
    db.commit()
    return True


def update_student(id, name, lastname):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE students SET name = ?, lastname = ? WHERE id = ?"
    cursor.execute(statement, [name, lastname, id])
    db.commit()
    return True


def delete_student(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM students WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, lastname FROM students WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_students():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, lastname FROM students"
    cursor.execute(query)
    return cursor.fetchall()