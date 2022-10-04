"""
Emily Ortiz, Sadi Nirloy, Ravindra Mangar (Silenced) of Wasabi Rain
K07: teardown
"""

from flask import Flask

randomName= Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@randomName.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    print("NOTICEABLE MESSAGE!!!")
    return "No hablamos queso!"  # Q4: Will this appear anywhere? How u know?
@randomName.route("/")
def more_words():
    print("What up")
    return "HELP! I'm trapped inside the computer. I need you're help if I'm to be free."

randomName.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
-The Flask object does not have to match the file name.
-The .route matches the variable, not the file. 
-Only hello_world is run, while more_words is not even printed, let alone returned.
QCC:
0. Not in other languages, but this looks like a Python class to me, 
	especially with the double underscores ("__")
1. The forward slash is commonly seen in a URL for websites to show the path of pages.
	Similar to a directory's forward slash in the path
2. This should print to the terminal of the IDE or the computer, depending on how it is run. 
	It is printed in the terminal every time the page is loaded/reloaded.
3. \"__main__\" is printed 
4. This is printed onto the website that is outputted by Flask. I know because I put the link outputted
	into my browser.
5. This looks like an invocation of a class's method, like in Java when you call a 
	method from a different file.
...

INVESTIGATIVE APPROACH:
We started out really confused. When running the program on the school computers, it kept telling us that
we were on a developer setting, not a production one. This was really confusing to us, and we thought
that we needed to run this in a different way. That's when the period ended. 
Afterschool, we tried running the program on our home devices, but we didn't have flask on our computers.
So, I went on the Intertrash to figure out how to download and use flask on my home Windows device.
After looking at the piazza, I realized that the output we got at the school was the expected result,
thanks to Ivan Y, Jeffrey Z, Raven T, and you Mr. Mykolyk. From there, it was simple enough to find
test out what parts did what, at least to some degree.
'''