from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Jakarta, Indonesia',
    'salary': 'Rp. 1.000.000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Jakarta, Indonesia',
    'salary': 'Rp. 1.500.000'
  },
  {
    'id': 3,
    'title': 'Data Engineer',
    'location': 'Bandung, Indonesia'
  },
  {
    'id': 4,
    'title': 'Data Munger',
    'location': 'Tegal, Indonesia',
    'salary': 'Rp. 1.000.000'
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs = JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)