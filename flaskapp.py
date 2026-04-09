# author: Camille Thoms
# description: Alveus Sanctuary Flask app with MySQL and DynamoDB
# credit: base structure from T. Urness and M. Moore; AI assistance used for DynamoDB routes

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *
from dynamoCode import *

# makes site and hides the user data safely. taken from lab work
app = Flask(__name__)
app.secret_key = 'your_secret_key' # required for flash messages

# home function - makes the home page
@app.route('/')
def home():
    return render_template('home.html')

# animals function - displays the animals data from RDS/SQL in HTML  
@app.route('/animals')
def animals():
    # Read all animals from RDS and display them
    data = get_all_animals()
    return render_template('animals.html', animals=data)

# sightings function - displays the sightings data from DynamoDB/nosql in HTML
@app.route('/sightings')
def sightings():
    # Read all sightings from DynamoDB and display them
    data = get_all_sightings()
    return render_template('sightings.html', sightings=data)

# add sighting function (should i start calling these routes? is that just semantics?) - displays and submits the sighting form
@app.route('/add-sighting', methods=['GET', 'POST'])
def add_sighting_route():
    if request.method == 'POST':
        # gets form data
        display_name = request.form['display_name']
        animal_tag = request.form['animal_tag']
        sighting = request.form['sighting']
        
        # Add to DynamoDB
        add_sighting(display_name, animal_tag, sighting)
        
        # submit and success message of submission
        flash('Sighting logged successfully!', 'success')
        return redirect(url_for('sightings'))
    # GET - display that shit 
    else:
        return render_template('add_sighting.html')

# delete sightings function - gets command, deletes record, displays 
@app.route('/delete-sighting', methods=['GET', 'POST'])
def delete_sighting_route():
    if request.method == 'POST':
        # gets form data
        display_name = request.form['display_name']
        timestamp = request.form['timestamp']
        
        # Delete from DynamoDB
        delete_sighting(display_name, timestamp)
        
        # submit and success message of deletion 
        flash('Sighting deleted!', 'warning')
        return redirect(url_for('sightings'))
    # GET - display that shit 
    else:
        return render_template('sightings.html', sightings=get_all_sightings())

# update sighting template - gets command, deletes record, displays
@app.route('/update-sighting', methods=['GET', 'POST'])
def update_sighting_route():
    if request.method == 'POST':
        # Extract form data
        display_name = request.form['display_name']
        timestamp = request.form['timestamp']
        new_sighting = request.form['new_sighting']
        
        # Update in DynamoDB
        update_sighting(display_name, timestamp, new_sighting)
        
        # submit and success message of updation 
        flash('Sighting updated!', 'success')
        return redirect(url_for('sightings'))
    # GET - display that shit
    else:
        return render_template('sightings.html', sightings=get_all_sightings())

# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)