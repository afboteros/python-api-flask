from flask import Flask, jsonify, request
import student_controller
from db import create_tables

app = Flask(__name__)


@app.route('/students', methods=["GET"])
def get_students():
    students = student_controller.get_students()
    return jsonify(students)


@app.route("/student", methods=["POST"])
def insert_student():
    student_details = request.get_json()
    name = student_details["name"]
    lastname = student_details["lastname"]
    result = student_controller.insert_student(name, lastname)
    return jsonify(result)


@app.route("/student", methods=["PUT"])
def update_student():
    student_details = request.get_json()
    id = student_details["id"]
    name = student_details["name"]
    lastname = student_details["lastname"]
    result = student_controller.update_student(id, name, lastname)
    return jsonify(result)


@app.route("/student/<id>", methods=["DELETE"])
def delete_student(id):
    result = student_controller.delete_student(id)
    return jsonify(result)


@app.route("/student/<id>", methods=["GET"])
def get_student_by_id(id):
    student = student_controller.get_by_id(id)
    return jsonify(student)

"""
Enable CORS. Disable it if you don't need CORS
"""
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)