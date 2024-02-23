from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
# def fetch_jobs_from_database():
#   conn = sqlite3.connect('jobs.db')
#   cursor = conn.cursor()
#   cursor.execute('SELECT * FROM jobs')
#   jobs = cursor.fetchall()
#   conn.close()
#   return jobs
JOBS = [
    {
        'id': 1,
        'title': 'Iron man',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Dr.Strange',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'captain America',
        'location': 'Remote',
        # 'salary': 'Rs. 12,00,000'
    },
    {
        'id': 4,
        'title': 'Thor',
        'location': 'San Francisco, USA',
        'salary': '$120,000'
    }
]


@app.route("/")

def hello():
  # jobs=fetch_jobs_from_database()
  return render_template("index.html", jobs=JOBS, c_name='afzal')


@app.route("/api/jobs")
def list_jobs():
  # jobs = fetch_jobs_from_database()
  return jsonify(jobs)


if __name__ == "__main__":
  # print("i am inside if")
  app.run(host="0.0.0.0", debug=True)
