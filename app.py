from flask import Flask, jsonify, render_template, Response
import sqlite3
import pathlib

working_directory =  pathlib.Path(__file__).parent.absolute()
DATABASE = working_directory / 'PData.db'

def query_db(query: str, args=()) -> list:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, args).fetchall()

    return result

app =  Flask(__name__)

@app.route('/')
def index() -> str:
    return render_template('main.html')

@app.route("/api/RobotMetrics")

def orders_over_time() -> Response:

    query = """
    SELECT Execution_Time
    FROM RobotMetrics
    GROUP BY Execution_Time
    ORDER BY Assignee;

    """

    result = query_db(query)

    dates = [row[0] for row in result]

    counts = [row[1] for row in result]

    return jsonify({"dates": dates, "counts": counts})

if __name__ == '__main__':
    app.run(debug=True)