#Team Bord: Austin Ngan (Gerald), Thomas Yu (Perry), Mark Zhu (Bob the Third Jr), Roshani Shrestha (Pete)
#SoftDev
#P00

#from flask import Flask             #facilitate flask webserving
#from flask import render_template   #facilitate jinja templating
#from flask import request           #facilitate form submission
#from flask import session           #facilitate session

from flask import Flask, render_template, request, session

app = Flask(__name__)    #create Flask object
app.secret_key="asdf123" #secret key for flask to work

teamBord = "Team Bord: Austin Ngan, Roshani Shrestha, Thomas Yu, Mark Zhu" #TNPG + roster for both landing and response pages
username = "Username"
password = "Password123"

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    '''For the landing page where the user will login with a username. If there is already a session, the repsonse page will be generated'''
    if 'u' in session and session['u'] == username:
        greet = "TEST"
        return render_template('response.html', heading = teamBord, greeting = greet, username = session['u'], password = password, request = request.method)
    else:
        return render_template( 'login.html' , heading = teamBord) #Only thing that is added to login page is the heading


@app.route("/auth")#	, methods=['GET', 'POST'])
def authenticate():
    '''The response page that will display a greeting, the username, and the request method used'''
    greet = "" #Greeting to be displayed on the response page
    if (request.method == 'GET'): #getting user and pass for GET
        tempUser = request.args['username']
        tempPass = request.args['password']
    elif (request.method == 'POST'): #getting user and pass for POST
        tempUser = request.form['username']
        tempPass = request.form['password']
    if (tempUser != username): #wrong username
        greet += "Error: Username is incorrect. "
    if (tempPass != password): #wrong password
        greet += "Error: Password is incorrect. "
    if (tempUser == username and tempPass == password):
        greet += "Hullo humon, Bord appreciates your visit. Enjoy your stay. "
        session['u'] = tempUser
    return render_template('response.html', heading = teamBord, greeting = greet, username = tempUser, password = tempPass, request = request.method)  #uses response template to create the webpage

@app.route("/logOut")
def logOut():
    '''For when the user logs out of the session'''
    session.pop('u',None)
    return render_template('login.html',warning="You have successfully logged out.")

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
