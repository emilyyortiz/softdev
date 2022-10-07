# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
import random as rng
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route

def choose():
    occupation = open("occupations.csv").read() #reading the csv file into a string

    occupation = occupation.split("\n") #split each new line 
    occupation.pop(0) #delete the heading
    occupation.pop(len(occupation)-1) #delete the extra empty line
    total = occupation.pop(len(occupation)-1) #delete the total of the values and store value

    #create dictionary
    jobs = {}
    for x in occupation:
        job = x.rsplit(",", 1)
        jobs[job[0]] = job[1]
    
    vals = list(jobs.values())
    #convert the values into floats
    for x in range(0, len(vals)):
        vals[x] = float(vals[x])

    sort_jobs = {}
    sort_jobs = jobs

    #identify the total of all the values         
    sum = total.split(",")
    sum = float(sum[1])
    #generate a random number from 1 to the total
    random = round(rng.uniform(1,sum),1)
    
    #continue to subtract from largest to smallest values from the rand val until <= 0
    #key of the last value to be subtracted is the outputed occupation!
    ret_val  = "Drowning Jelleyfish: Jing Feng, Emily Ortiz, Lauren Lee<br> SoftDev<br> K08 --<br> 2022-10-06<br> time spent: <elapsed time in hours, rounded to nearest tenth><br><br>"
    for key in sort_jobs:
        random = random - float(sort_jobs[key])
        if random <= 0 :
            ret_val = ret_val + "random occupation: " + key + "<br>" +  "<br>All Occupations:<br>"
            break
    for key in sort_jobs:
        ret_val = ret_val + "<br>" + key
    return ret_val

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
