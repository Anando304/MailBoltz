
from flask import Flask,render_template,request,redirect,url_for,session, g
from controller import controller
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET','POST'])
def default():
    return redirect(url_for('home'))

@app.errorhandler(404) # For 404 errors
def page_not_found(e):
    if request.method == 'POST':
        if request.form['LoginRedirect'] == 'Login Page': #Login Page is the value associated with the button once clicked sending POST request data
           return redirect(url_for('home')) #Redirects to login page using login/home function.
    return render_template('404.html')

@app.errorhandler(500)
def page_not_found500(e):
    if request.method == 'POST':
        if request.form['LoginRedirect'] == 'Login Page':
           return redirect(url_for('home'))
    return render_template('500.html')

@app.route('/home', methods=['GET','POST'])
def home():
    output = None

    if request.method == 'POST':
        #all buttons have the same name(submit), just diff value(ie: Submit,view,etc)
        if request.form['submit'] == 'Submit':
            print(request.form)
            # Read input credentials
            user = request.form["email"]
            pass_ = request.form["password"]
            num_emails = int(request.form["num_emails"])
            folder = request.form["folder"]
            output = controller(user,pass_,num_emails,folder)

            if output == "Success":
                session.pop('logged_in',None) #lOGOUT of any existing session
                session['logged_in'] = True #Create new session
                return render_template('index.html',error=output)


        elif request.form['submit'] == 'view':
            return redirect(url_for('view'))

    return render_template('index.html',error=output)


@app.before_request #Use of request decorators to check if a session is active before moving onto an authenticated page
def before_request():
    #g is a global variable representing the session
    g.logged_in = None
    if 'logged_in' in session: #If a user exists or is currently logged. logged_in is the key in the session that is associated with True
        g.user = session['logged_in']

# View emails if available
@app.route('/view', methods=['GET','POST'])
def view():
    if request.method == 'GET':

        # If authenticated session not yet created
        if g.user == None:
            return redirect(url_for('home'))

        session.pop('logged_in', None)  # Pops the user value from the session dictionary essentially logging them out
        return render_template('EmailSummary.html')
          
if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
