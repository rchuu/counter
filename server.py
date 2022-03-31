from flask import Flask, render_template, session, redirect  # added render_template!
app = Flask(__name__)

app.secret_key = "kobibeanc"


@app.route('/')
def index():
    if "count" not in session:  # resets the code
        session["count"] = 0  # count should be in session
    else:
        session['count'] += 1
    return render_template('index.html')


# route is for incrementing sessions, then its going redirect it's index, and display that
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
