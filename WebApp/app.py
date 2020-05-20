
from flask import Flask,render_template,request,redirect,url_for,session, g
from controller import controller
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.before_request #Use of request decorators to check if a session is active before moving onto an authenticated page
def before_request():
    #g is a global variable representing the session
    g.logged_in = None
    if 'logged_in' in session: #If a user exists or is currently logged. logged_in is the key in the session that is associated with True
        g.user = session['logged_in']

@app.route('/home', methods=['GET','POST'])
def home():
    output = None
    if request.method == 'POST':
        #all buttons have the same name(submit), just diff value
        if request.form['submit'] == 'Submit':

            # Read input credentials
            user = request.form["email"]
            pass_ = request.form["password"]
            output = controller(user,pass_)

            session.pop('logged_in',None) #lOGOUT of any existing session
            session['logged_in'] = True #Create new session

        elif request.form['submit'] == 'view':
            return redirect(url_for('view'))

    return render_template('index.html',error=output)


# View emails if available
@app.route('/view', methods=['GET','POST'])
def view():
    if request.method == 'GET':
        return render_template('EmailSummary.html')
          
if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
