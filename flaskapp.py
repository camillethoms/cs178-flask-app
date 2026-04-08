# KEEP BUT change names and shit, duh
# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT

# KEEP
from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *

# KEEP 
app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

# KEEP
@app.route('/')
def home():
    return render_template('home.html')

# ADD SIGHTINGS, instead of users (if display, tag, sighting dynamo, else add)
@app.route('/add-user', methods=['GET', 'POST'])
def add_sighting_route():
    if request.method == 'POST':
        # Extract form data
        display_name = request.form['display_name']
        animal_tag = request.form['animal_tag']
        sighting = request.form['sighting']
        
        # Add to DynamoDB
        add_sighting(display_name, animal_tag, sighting)
        
        flash('Sighting logged successfully!', 'success')
        return redirect(url_for('sightings'))
    else:
        # Render the form page if the request method is GET
        return render_template('add_sighting.html')


# delete sighting 
@app.route('/delete-user',methods=['GET', 'POST'])
def delete_sighting_route():
    if request.method == 'POST':
        # Extract form data
        display_name = request.form['display_name']
        timestamp = request.form['timestamp']
        
        # Delete from DynamoDB
        delete_sighting(display_name, timestamp)
        
        flash('Sighting deleted!', 'warning')
        return redirect(url_for('sightings'))
    else:
        return render_template('sightings.html', sightings=get_all_sightings())

@app.route('/update-sighting', methods=['GET', 'POST'])
def update_sighting_route():
    if request.method == 'POST':
        # Extract form data
        display_name = request.form['display_name']
        timestamp = request.form['timestamp']
        new_sighting = request.form['new_sighting']
        
        # Update in DynamoDB
        update_sighting(display_name, timestamp, new_sighting)
        
        flash('Sighting updated!', 'success')
        return redirect(url_for('sightings'))
    else:
        return render_template('sightings.html', sightings=get_all_sightings())

# save for later 
# @app.route('/display-users')
# def display_users():
    # hard code a value to the users_list;
    # note that this could have been a result from an SQL query :) 
    users_list = (('John','Doe','Comedy'),('Jane', 'Doe','Drama'))
    return render_template('display_users.html', users = users_list)

# KEEP
@app.route('/animals')
def animals():
    data = get_all_animals()
    return render_template('animals.html', animals=data)

# oh my, what to do with you friend? (we're treating the code nicely so it treats me nicely)
# @app.route('sightings', methods=['GET', "POST'"])
# def sightings():
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add':
            display_name = request.form['display_name']
            animal_tag = request.form['animal_tag']
            sighting = request.form['sighting']
            add_sighting(display_name, animal_tag, sighting)
            flash('Sighting logged!', 'success')

        elif action == 'delete':
            display_name = request.form['display_name']
            timestamp = request.form['timestamp']
            delete_sighting(display_name, timestamp)
            flash('Sighting deleted!', 'warning')

        elif action == 'update':
            display_name = request.form['display_name']
            timestamp = request.form['timestamp']
            new_sighting = request.form['new_sighting']
            update_sighting(display_name, timestamp, new_sighting)
            flash('Sighting updated!', 'success')

        return redirect(url_for('sightings'))
    
    data = get_all_sightings()
    return render_template('sightings.html', sightings=data)



# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
