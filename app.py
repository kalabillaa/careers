from flask import Flask,render_template

app=Flask(__name__)

JOBS=[
    {
    'id':1,
    'company':"softwarea",
    'title':'sde1',
    'location':'delhi',
    'salary':100000
    },
    {
    'id':2,
    'company':"softwareb",
    'title':'sde2',
    'location':'delhi',
    'salary':150000
    },
    {
    'id':3,
        'company':"softwarec",
    'title':'sde3',
    'location':'delhi',
    'salary':1000000
    },

]

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/jobs")
def jobs():
    return render_template('jobs.html',jobs=JOBS)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)