'''
Drowning Jelleyfish: Jing Feng, Emily Ortiz, Lauren Lee
SoftDev
K08 -- 
2022-10-06
time spent: <elapsed time in hours, rounded to nearest tenth>
'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...") #prints string in terminal/shell
    print(__name__)   #where will this go? Right under the previous line
    return "No hablo queso!"

app.run()

