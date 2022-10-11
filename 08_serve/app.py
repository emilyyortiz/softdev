'''
Drowning Jelleyfish: Jing Feng, Emily Ortiz, Lauren Lee
SoftDev
K08 -- Putting it Together
2022-10-06
time spent: 1.5
'''

from flask import Flask
import random as rng
import csv

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to choose")
    return display()

#just testing
@app.route("/foo")       #will run the function attached to the decorator
def hello_world2():
    print("about to choose you PIKACHU!")
    return display()

with open("occupations.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',') #reads csv
    occupation = []
    for row in csv_reader:
        occupation.append(row) #each row is a list, add each list as an element in a larger list

occupation.pop(0) #delete the heading
total = occupation.pop(len(occupation)-1) #delete the total of the values and store value

#create dictionary
jobs = {}
for x in occupation:
    #imulaneously converting to float, and attaching link
    jobs[x[0].replace("\"", "")] = [float(x[1]), "https://www.google.com/search?q=" + x[0].replace("\"", "")]

def choose():
    #identify the total of all the values         
    sum = total[1]
    sum = float(sum)
    #generate a random number from 1 to the total
    random = round(rng.uniform(1,sum),1)
    
    #continue to subtract from largest to smallest values from the rand val until <= 0
    #key of the last value to be subtracted is the outputed occupation!
    for key in jobs:
        random = random - float(jobs[key][0])
        if random <= 0 :
            return "<a href=" + "\"" + jobs[key][1] + "\">" + key + "</a>"

def display():
    ret_val  = "Drowning Jelleyfish: Jing Feng, Emily Ortiz, Lauren Lee<br> SoftDev<br> K08 --<br> 2022-10-06<br> time spent: <elapsed time in hours, rounded to nearest tenth><br><br>"
    ret_val = ret_val + "random occupation: " + choose() + "<br>" 
    ret_val = ret_val +  "<br>All Occupations:<br>"
    for key in jobs:
        ret_val = ret_val + "<br>" + "<a href=" + "\"" + jobs[key][1] + "\">" + key + "</a>"
    return ret_val

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
