from flask import Flask, render_template, url_for, redirect, request

app1=Flask(__name__)
@app1.route("/")
def welcome():
    return render_template('index2.html')

@app1.route("/yes/<float:score>")
def yes(score):
    if score>3:
        res="You Have High Risk Of Stroke"
    else:
        res="You Have Low Risk Of Stroke"

    return render_template('result.html', result=res)


@app1.route('/submit', methods=["POST", "GET"])

def submit():
    total=0
    if request.method=="POST":
        Name=request.form['Name']
        Diabetes=float(request.form ['Diabetes'])
        Cholesterol=float(request.form['Cholesterol'])
        Alcohol=float(request.form['Alcohol'])
        Smoking=float(request.form['Smoking'])
        total=Diabetes+Cholesterol+Alcohol+Smoking
    res="yes"

    return redirect(url_for(res, score=total))





if __name__=='__main__':
    app1.run(debug=True)