from flask import Flask, render_template, request, session, redirect, url_for, flash
from forms import objSearchForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

#array of zipcodes entered through reports
zipcodes = {}
#dict of objects reported lost
objects = {}
#global counter
global_counter = 1;
#object class
class Object:
    def __init__(self, id, email, name, zip, desc):
        self.id = id
        self.name = name
        self.zip = zip
        self.desc = desc
        self.email = email

@app.route('/', methods=['GET','POST'])
def options():
        return render_template('index.html',)

#route for clicking on the search button
@app.route('/search', methods=['GET','POST'])
def search():
    search = objSearchForm(request.form) #search form
    if request.method =='GET':
        return render_template('search.html',)

    if request.method =='POST': #If user clicks "search", return the results
        return search_results(search)

#route for clicking on the report button
@app.route('/report', methods=['GET','POST'])
def report():
    if request.method =='GET':
        return render_template('report.html',)

    if request.method =='POST': #values that are inputted into the form
        global global_counter
        email = request.form.get('user_email')
        name = request.form.get('item_found')
        zipcode = request.form.get('zip_found')
        desc = request.form.get('item_description')
        print(email)
        print(desc)
        new_obj = Object(global_counter, email, name, zipcode, desc)
        objects[str(new_obj.id)] = new_obj
        if new_obj.zip not in zipcodes:
            zipcodes[new_obj.zip] = []
        zipcodes[new_obj.zip].append(new_obj)
        global_counter += 1
        return redirect("/objects/" + str(new_obj.id))


#object list that is generated once the user inputs search parameters
@app.route('/results', methods=['GET','POST'])
def search_results(search):
    results = []
    search_string = search.data['search']

    if search.data['search'] == '': #if no input
        flash('No results found!')
        return redirect(url_for("search.html"))

    if not results:
        flash('No results found!') #if no results found
        return redirect(url_for("search.html"))

    else: # display results
        return render_template('results.html', results=results)

    if request.method =='POST': #user clicks on an item
        return redirect(url_for("<some_obj>"))

#loads the page for a specific object once clicked on
@app.route('/objects/<id>', methods=['GET','POST'])
def objects_page(id):
    return render_template('object.html', obj=objects[id])

app.debug = True

if __name__ == '__main__':
    app.run()
