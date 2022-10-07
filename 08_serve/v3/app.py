'''
Drowning Jelleyfish: Jing Feng, Emily Ortiz, Lauren Lee
SoftDev
K08 -- 
2022-10-06
time spent: <elapsed time in hours, rounded to nearest tenth>
'''
#Error message when running in Firefox when running in thonny
#Firefox can’t establish a connection to the server at 127.0.0.1:5000
#Message in thonny: /usr/bin/python3: No module named thonny.plugins.cpython.app
#thonny stops running program
#website works when running in terminal

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True #prediction: no warnings
#* Restarting with stat
#* Debugger is active!
#* Debugger PIN: 306-490-003

app.run()
