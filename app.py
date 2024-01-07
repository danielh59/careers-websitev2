from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)


@app.route("/")
def hello_world():
    job_list = load_jobs_from_db()
    return render_template('home.html', 
                           jobs=job_list,
                           company_name='OneTech')

@app.route("/listings")
def job_listings():
      jobs = load_jobs_from_db()
      return render_template('index.html',
                            jobs=jobs)

@app.route("/api/listings")
def listings():
      jobs = load_jobs_from_db()
      return jsonify(jobs)

@app.route("/listing/<id>")
def show_listing(id):
      job = load_job_from_db(id)
      if not job:
            return "Listing Not Found", 404
      return render_template('listingpage.html', job=job)

@app.route("/listing/<id>/apply", methods=['post'])
def apply_to_listing(id): 
      data = request.form
      job = load_job_from_db(id)  
      add_application_to_db(id, data)
      return render_template('application_submit.html', 
                             application=data, job=job)

print(__name__)
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)