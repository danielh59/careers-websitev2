from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
    job_list = load_jobs_from_db()
    return render_template('home.html', 
                           jobs=job_list,
                           company_name='OneTech')

@app.route("/listings")
def job_listings():
      return render_template('index.html')

@app.route("/api/listings")
def listings():
      return jsonify(JOBS)

print(__name__)
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)