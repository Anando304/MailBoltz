## @file app.py
 # @author Anando Zaman
 # @brief Webserver to link front & backend communication
 # @date May 19, 2020
from flask import Flask,render_template,request,redirect,url_for,session, g
from controller import controller
import os

app = Flask(__name__)
app.secret_key = "AAAAAAAAaaaaaaaaaaaa"

@app.route('/', methods=['GET','POST'])
def default():
    return redirect(url_for('home'))

@app.errorhandler(404) # For 404 errors
def page_not_found(e):
    if request.method == 'POST':
        # if login button pressed
        if request.form['submit'] == 'submit': #Login Page is the value associated with the button once clicked sending POST request data
           return redirect(url_for('home')) #Redirects to home page using home function.
    return render_template('404.html')

@app.errorhandler(500)
def page_not_found500(e):
    if request.method == 'POST':
        #if login button pressed
        if request.form['submit'] == 'submit':
           return redirect(url_for('home'))
    return render_template('500.html')

@app.route('/home', methods=['GET','POST'])
def home():
    status = None

    if request.method == 'POST':
        #all buttons have the same name(submit), just diff value(ie: Submit,view,etc)
        if request.form['submit'] == 'Submit':
            #print(request.form)
            # Read input credentials
            user = request.form["email"]
            pass_ = request.form["password"]
            num_emails = int(request.form["num_emails"])
            folder = request.form["folder"]
            output = controller(user,pass_,num_emails,folder)
            status = output[0]
            summary = output[1]

            if status == "Success":
                session.pop('logged_in',None) #lOGOUT of any existing session
                session['logged_in'] = True #Create new session

                #Session to store summary data
                session["summary"] = summary
                return render_template('index.html',error=status)


        elif request.form['submit'] == 'view':
            return redirect(url_for('view'))

        elif request.form['submit'] == 'instructions':
            return redirect(url_for('instructions'))

    return render_template('index.html',error=status)


@app.before_request
def before_request():
    #g is a global variable representing the session
    g.logged_in = None
    if 'logged_in' in session: #If a user exists or is currently logged. logged_in is the key in the session that is associated with True
        g.user = session['logged_in']

# View emails if available
@app.route('/view', methods=['GET','POST'])
def view():

    if request.method == 'POST':
        if request.form['submit'] == 'home':
            return redirect(url_for('home'))

    if request.method == 'GET':

        # If authenticated session not yet created
        #if g.user == None:
            #return redirect(url_for('home'))

        #Extract summary data saved in session
        summary = session.get('summary', None)
        session.pop('logged_in', None)  # Pops the user value from the session dictionary essentially logging them out, when they exit the screen
        print(summary)
        return render_template('EmailSummary.html',summary=summary)


# Instructions page
@app.route('/instructions', methods=['GET','POST'])
def instructions():

    if request.method == 'POST':
        if request.form['submit'] == 'home':
            return redirect(url_for('home'))

    if request.method == 'GET':
        return render_template('instructions.html')
          
if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
