"""
Emily Ortiz, Sadi Narloy, Ravindra Mangar
SoftDev
TNPG: Wasabi Rain
2022-09-22

DISCO:
  -The existence of the dict.keys() function
    -It does not return a list, but rather a "viewing object" that holds the array
    -This object can be type casted into a list
  -random.choice() takes a random element from a list
  -do while loops do not exist in python

QCC:
  -Super shocked that "do while" does not exist
  
OPS SUMMARY:
  -Start by making a list from the set of keys
  -Pick a random key from the list
  -Get the list that the key refers to
  -Check if that list has any values in it
    -If not, repeat the process of picking a new key until an array with values is addressed
  -Pick a random element from the area 
"""

import random

krewes = {2:["Anson", "Efe", "Faiza"], 7:["Ravindra", "Emily", "Sadi"], 8:["Sasha", "Shreya", "Jeffery"]}

testing = {"A":["A1", "A2", "A3", "A4"], "B":["B1"], "C":["C1", "C2", "C3"], "D":["D1", "D2", "D3", "D4", "D5", "D6", "D7"], "E":[], "F":["F1", "F2"]}

def randFromDictOfArr(dictionary):
  listOfKeys = list(dictionary.keys())
  #print(ListOfKeys)
  pickingFromKeys= random.choice(listOfKeys)
  #print(pickingFromKeys)
  arrFromDict = dictionary[pickingFromKeys]
  while (len(arrFromDict) <= 0):
    pickingFromKeys= random.choice(listOfKeys)
    arrFromDict = dictionary[pickingFromKeys]
  pickingFromArr = random.choice(arrFromDict)
  print(pickingFromArr)

  #print((krewes[list[get_rand_num()]])[get_rand_num()])
  
#FOR LOOP TO VERIFY THAT RESULTS ARE RANDOM // RUNS TEN TIMES
for i in range(10):
  randFromDictOfArr(krewes)

#FOR LOOP TO VERIFY THAT RESULTS ARE RANDOM // RUNS HUNDRED TIMES
for i in range(100):
  randFromDictOfArr(testing)
