from flask import Flask, render_template, request, redirect, url_for, flash
from database import display_data,insert

# Create a Flask Instance (Is a must!)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'random key'

@app.route('/')
def home():
    user = display_data()
    return render_template("home.html", user=user)

@app.route('/insert', methods=['GET', 'POST'])
def register():
    if request.method == 'POST': # getting the data from the html form
        id = request.form.get('id')
        number = request.form.get('number')
        name = request.form.get('name')
        
        insert(id, name, number)    # pass the parameter and run the function 'insert' in database.py 

        flash('Inserted!', category='success')  # when insert sucessfully, it will pop up message

        return redirect(url_for('home'))    # after inserting return to home page
    
    return render_template("insert.html")

if __name__ == "__main__":
    app.run(debug=True)