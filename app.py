from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
      {
            'id': 1,
            'title': 'Data Analyst',
            'location': 'New York,New York',
            'salary': '$210,000'
      },
      {
            'id': 2,
            'title': 'Data Scientist',
            'location': 'Miami, Florida',
            'salary': '$240,000'
      },
      {
            'id': 3,
            'title': 'Backend Engineer',
            'location': 'Malibu,California',
            'salary': '$130,000'
      },
       {
            'id': 4,
            'title': 'Frontend Developer',
            'location': 'Remote',
            'salary': '$123,000'
      }
      
]
@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='OneTech')

@app.route("/listings")
def job_listings():
      return render_template('index.html')

@app.route("/api/listings")
def listings():
      return jsonify(JOBS)

print(__name__)
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)