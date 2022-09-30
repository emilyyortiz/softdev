# Vivian Teo, Emily Ortiz
# SoftDev
# 
# 2022-__-__
# time spent:

# DISCO:
# 
# QCC:

import random

# what krewes should end up as
# note: the periods are strings, not integers
krewes0 = {'2':{"devoA":"duckyA", "devoB":"duckyB", "devo":"ducky"},
          '7':{"vivian":"froggy", "emily":"rain"},
          '8':{"devoC":"duckyC", "devoD":"duckyD"}
          }

# opening krewes.txt file
file = open("krewes.txt", "r")
# content has krewes.txt as a string
content = file.read()

# tuples is formatted as ["pd$$$devo$$$ducky", ...]
tuples = content.split("@@@")
# print("tuples:")
# print(tuples)
# print()

# empty dictionary
krewes = {}

for trio in tuples:
    # splitting each element/trio in tuples into a list of [pd, devo, ducky]
    temp = trio.split("$$$")
    #print(temp)
    
    pd = temp[0]
    devo = temp[1]
    ducky = temp[2]
    
    if not (pd in krewes): # if there is no dictionary for that period yet
        # add an empty dictionary for that period
        krewes[pd] = {}
    # adds devo as key, and ducky as value
    krewes[pd][devo] = ducky

# print("krewes dictionary after being populated:")
# print(krewes)
# print()

def random_dev(krewes):
    # pick a random key/pd from a list of keys in krewes
    key = random.choice(list(dict.keys(krewes)))
    # access dictionary for that key/pd
    pd_dict = krewes[key]
    # pick a random key/devo from a list of keys in that pd
    devo = random.choice(list(dict.keys(pd_dict)))
    # ducky is value for devo key
    ducky = pd_dict[devo]
    print(key+", "+devo+", "+ducky)

# print("random_dev test:")
# random_dev(krewes)

print("Pick 10 random devos:")
for i in range(10):
    random_dev(krewes)

# print()
# print("Was krewes populated properly?")
# print(krewes0 == krewes)