import sqlite3
from flask import Flask, render_template, request

HOST_NAME = 'localhost'
HOST_PORT = 80
DBFILE = 'USERS.db'

app = Flask(__name__)

def getusers():
  connection = sqlite3.connect(DBFILE)
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM `USERS`")
  results = cursor.fetchall()
  connection.close()
  return results

@app.route("/")
def index():
  # (C1) GET ALL USERS
  users = getusers()
  # print(users)
  return render_template('temp.html', gifts=users)

if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)