from __future__ import division
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def post():
    fname= request.form['fname']
    lname = request.form['lname']

    matched_characters=0

    f_TF = [False] * len(fname)
    l_TF = [False] * len(lname)
    match_distance = (max(len(fname), len(lname)) // 2) - 1
    k = 0
    transpositions = 0

    for i in range(len(fname)):

        x = max(0, i - match_distance)
        y = min(i + match_distance + 1, len(lname))

        for j in range(x, y):
            if l_TF[j]:
                continue
            if fname[i] != lname[j]:
                continue
            f_TF[i] = True
            l_TF[j]= True
            matched_characters+=1
            break

    if matched_characters == 0:
        return render_template("index.html", sonuc=0)

    for i in range(len(fname)):
        if not f_TF[i]:
            continue
        while not l_TF[k]:
            k += 1
        if fname[i] != lname[k]:
            transpositions += 1
        k = k+1

    
    islem=(((matched_characters / len(fname)) +(matched_characters / len(lname)) +((matched_characters - transpositions / 2) / matched_characters)) / 3)*100
    islem=round(islem,2)

    return render_template("index.html", sonuc=islem)

if __name__ == "__main__":
    app.run(debug=True)
