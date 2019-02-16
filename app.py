from flask import Flask, render_template, request, session, redirect, url_for, flash
from forms import objSearchForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

#array of zipcodes entered through reports
zipcodes = []
#array of objects reported lost
objects = []

@app.route('/', methods=['GET','POST'])
def options():
        return render_template('/templates/index.html',)

#route for clicking on the search button
@app.route('/search', methods=['GET','POST'])
def search():
    search = objSearchForm(request.form) #search form
    if request.method =='GET':
        return render_template('/templates/search.html',)

    if request.method =='POST': #If user clicks "search", return the results
        return search_results(search)

#route for clicking on the report button
@app.route('/report', methods=['GET','POST'])
def report():
    if request.method =='GET':
        return render_template('/templates/report.html',)

    if request.method =='POST': #values that are inputted into the form
        result = request.form['repobj', 'zipcoderpt','description','email']
        if repobj is None or description is None or email is None:
            flash("Please fill out all fields!")
        zipcodes.append(zipcoderpt)
        objects.append(repobj)
        flash("Posted!")
        return render_template("/templates/<some_obj>", result=result)

#object list that is generated once the user inputs search parameters
@app.route('/results', methods=['GET','POST'])
def search_results(search):
    results = []
    search_string = search.data['search']

    if search.data['search'] == '': #if no input
        flash('No results found!')
        return redirect(url_for("/templates/search.html"))

    if not results:
        flash('No results found!') #if no results found
        return redirect(url_for("/templates/search.html"))

    else: # display results
        return render_template('/templates/results.html', results=results)

    if request.method =='POST': #user clicks on an item
        return redirect(url_for("/templates/<some_obj>"))

#loads the page for a specific object once clicked on
@app.route('/<some_obj>', methods=['GET','POST'])
def some_obj_page(some_obj):
    return render_template('/templates/index.html')

app.debug = True

if __name__ == '__main__':
    app.run()
