'''
Drowning Jelleyfish: Jing Feng, Emily Ortiz, Lauren Lee
SoftDev
K08 -- Putting it Together
2022-10-06
time spent: 1.5
'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()
#no print statement in terminal/shell
