'''
Drowning Jelleyfish: Jing Feng, Emily Ortiz, Lauren Lee
SoftDev
K08 -- 
2022-10-06
time spent: <elapsed time in hours, rounded to nearest tenth>
'''

from flask import Flask
app = Flask(__name__) # similar syntax to java

@app.route("/") # where to look to run file "/" used to represent it is going to be at the root page
def hello_world():
    print(__name__) # everytime reload, it prints in terminal
    return "No hablo queso!"  # prints whatever is in return statement on webpage

app.run()  # runs
                
