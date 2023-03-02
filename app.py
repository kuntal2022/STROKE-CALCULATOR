from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')

def welcome():
    return render_template('index2.html')

@app.route("/yes/<float:score>")
def yes(score):
    if score>3:
        res="You Have Stroke"
    else:
        res="You Don't Have Stroke"

    return render_template('result.html', result=res)






@app.route("/submit", methods=['POST', "GET"])

def submit():
    total=0
    if request.method=="POST":
        # diab=float(request.form['diab'])
        # heartd=float(request.form['heartd'])
        # smoking=float(request.form['smoking'])
        # alcho=float(request.form['alcho'])
        # total=(diab+heartd+smoking+alcho)
        
       Diabetes=float(request.form ['Diabetes'])
       Cholesterol=float(request.form['Cholesterol'])
       Alcohol=float(request.form['Alcohol'])
       Smoking=float(request.form['Smoking'])
       total=Diabetes+Cholesterol+Alcohol+Smoking
    res="yes"

    return(redirect(url_for(res, score=total)))









if __name__== "__main__":
    app.run(debug=True)