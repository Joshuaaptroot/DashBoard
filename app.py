from flask import Flask, jsonify, render_template, Response
import sqlite3
import pathlib

app = Flask(__name__)
working_directory = pathlib.Path(__file__).parent.absolute()
DATABASE = working_directory / 'PData.db'

def query_db(query: str, args=()) -> list:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, args).fetchall()
    return result

@app.route('/')
def index() -> str:
    return render_template('main.html')

@app.route("/api/RobotMetrics")
def robot_metrics() -> Response:
    query = """
    SELECT Execution_Time, Assignee
    FROM RobotMetrics
    ORDER BY Assignee;
    """
    result = query_db(query)
    data = [{"Execution_Time": row[0], "Assignee": row[1]} for row in result]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
