from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/depot/home')
def welcome_splash():
    users = User.allusersdisplay()
    return render_template("cornerstone.html", users=users)

@app.route('/addnewuser',methods=['POST'])
def new_user_form():
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email']
    }
    User.add_new_user(data)
    return redirect('/depot/home')

@app.route('/depot/user/<int:id>')
def display_user(id):
    data = {
        'id' : id
    }
    return render_template("user_page.html", user_profile = User.one_user(data))

@app.route('/depot/user/<int:id>/edit')
def edit_page(id):
    data = {
        'id':id
    }
    return render_template("user_edit.html", user_profile = User.one_user(data))

@app.route('/depot/user/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        'id' : id,
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email']
    }
    User.update_user(data)
    return redirect(f'/depot/user/{id}')

@app.route('/depot/user/<int:id>/delete')
def delete_user(id):
    data = {
        'id' : id
    }
    User.delete_account(data)
    return redirect('/depot/home')

@app.route('/depot/adduser')
def form_useradd():
    return render_template("user_form.html")

if __name__=="__main__":
    app.run(debug=True)