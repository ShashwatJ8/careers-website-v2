from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOB = [
  {
    'id': 1,
    'Position':'Software Developer',
    'Location':'Banglore, India',
    'Salary':'Rs 20,00,000'
    
  },
  {
    'id': 2,
    'Position':'Frontend Developer',
    'Location':'Indore, India',
    'Salary':'Rs 20,00,000'
    
  },
  {
    'id': 1,
    'Position':'Data Engineer',
    'Location':'California, USA',
    'Salary':'$ 130,000'
    
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs = JOB)

@app.route("/api/jobs")
def return_list():
  return jsonify(JOB)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
