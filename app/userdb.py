import sqlite3   #enable control of an sqlite database

DB_FILE="users.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

# PRIMARY KEY UNIQUE
command = '''CREATE TABLE IF NOT EXISTS logins(
    username TEXT NOT NULL,
    password TEXT NOT NULL)'''
c.execute(command)

# PRIMARY KEY UNIQUE
command2 = '''CREATE TABLE IF NOT EXISTS blogs(
    username TEXT NOT NULL,
    blogKey TEXT NOT NULL,
    blogText TEXT NOT NULL)'''
c.execute(command2)

db.commit()
db.close()

def addUser(username, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO logins VALUES(?, ?)", (username, password))
    db.commit()
    db.close()


def addBlog(username, blogKey, text):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO blogs VALUES(?, ?)", (username, blogKey))
    db.commit()
    db.close()

def makeLoginsDict():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM logins")
    logininfo = c.fetchall()

    loginsinfo = {} # create a dictionary for all the login information

    for login in logininfo:
        loginsinfo[login[0]] = login[1]

    return loginsinfo
    db.commit()
    db.close()

def checkUser(username):
    loginsinfo = makeLoginsDict()
    return username in loginsinfo.keys()

def checkUserPass(username, password):
    loginsinfo = makeLoginsDict()
    return (username in loginsinfo.keys()) and (loginsinfo[username] == password)

#def findUsername(uName):
#    db = sqlite3.connect(DB_FILE)
#    c = db.cursor()
#    if ((c.execute("SELECT * FROM logins WHERE username =" + uName))) 
# addUser("hello", "123123a")


