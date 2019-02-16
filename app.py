from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/', methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('index.html',)

    if request.method =='POST':
        city = request.values["city"]
        if city.lower() != "new york city":
            flash("Not availible for your city yet!")
            return render_template("index.html")
        return redirect(url_for("options"))

@app.route('/options', methods=['GET','POST'])
def options():
        return render_template('options.html',)

@app.route('/search', methods=['GET','POST'])
def search()
    if request.method =='GET':
        return render_template('search.html',)

    if request.method =='POST':
        object = request.values["object"]
        if object not in objects:
            flash("Sorry, we can't find that!")
            return render_template("search.html")
        return redirect(url_for("objlist"))

@app.route('/report', methods=['GET','POST'])
def report();
    if request.method =='GET':
        return render_template('report.html',)

    if request.method =='POST':
        zipcode = request.values["zipcode"]
        if #not all fields filled out
            flash("Please fill out all fields!")
        flash("Posted!")
        return redirect(url_for("options"))

@app.route('/objlist', methods=['GET','POST'])
def objlist(zipcode);
    if request.method =='GET':
        return render_template('list.html', content = zipcode)

    if request.method =='POST':
        return redirect(url_for("<some_obj>"))

@app.route('/<some_obj>', methods=['GET','POST'])
def some_obj_page(some_obj);
    return HTML_TEMPLATE.substitute(obj_name=some_obj);

zipcodes = []

@socketio.on('new_report') #append zipcode to array
def send(data):
    objects.append(data)


app.debug = True

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
