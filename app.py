from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

#HTML template for report posts
HTML_TEMPLATE=Template("""
<h1>{obj_name}</h1>
<p>{desc}<p>
<p>Contact: {em}<p>
""")

@app.route('/', methods=['GET','POST'])
def login():
#google login

#main page with report and search options
@app.route('/options', methods=['GET','POST'])
def options():
        return render_template('options.html',)

#route for clicking on the search button
@app.route('/search', methods=['GET','POST'])
def search()
    if request.method =='GET':
        return render_template('search.html',)

    if request.method =='POST': #values that the user puts in to find their object
        zipcode = request.values["zipcode"]
        findobj = request.values["findobj"]
        if zipcode not in zipcodes:
            flash("Sorry, nothing reported in this zipcode!")
            return render_template("search.html")
        return redirect(url_for("objlist"))

#route for clicking on the report button
@app.route('/report', methods=['GET','POST'])
def report();
    if request.method =='GET':
        return render_template('report.html',)

    if request.method =='POST': #values that are inputted into the form
        repobj = request.values["repobj"]
        description = request.values["description"]
        email = request.values["email"]
        zipcoderpt = request.values["zipcoderpt"]
        if repobj is None or description is None or email is None
            flash("Please fill out all fields!")
        flash("Posted!")
        return redirect(url_for("options"))

#object list that is generated once the user inputs search parameters
@app.route('/objlist', methods=['GET','POST'])
def objlist(zipcode);
    if request.method =='GET': #generates list
        return render_template('list.html', content = zipcode)

    if request.method =='POST': #user clicks on an item
        return redirect(url_for("<some_obj>"))

#loads the page for a specific object once clicked on
@app.route('/<some_obj>', methods=['GET','POST'])
def some_obj_page(some_obj, obj_desc, obj_email);
    return HTML_TEMPLATE.substitute(obj_name=some_obj, desc=obj_desc, em=obj_email);

#array of zipcodes entered through reports
zipcodes = []
#array of objects reported lost
objects = []


@socketio.on('new_report') #append zipcode and object to array when a new report is created
def send(datazip, dataobj):
    zipcodes.append(datazip)
    objects.append(dataobj)


app.debug = True

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
