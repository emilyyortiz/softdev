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
  -Original Assignment (Random element from dictionary of arrays)
    -Start by making a list from the set of keys
    -Pick a random key from the list
    -Get the list that the key refers to
    -Check if that list has any values in it
      -If not, repeat the process of picking a new key until an array with values is addressed
    -Pick a random element from the area
  -Checking that all values are reached
    -Modifying the dictionary to create a dictionary of arrays of arrays
      -Each innermost array contains a boolean followed by the name
    -The function is adapted to handle the changes to the dictionary
      -Making sure appropriate changes were reaching the right index
  -Investigations of the view object
    -Using randrange to get a number, and then using a for loop and a counter to replace indexing
    -using random.shuffle to get random element at front
    -New tester
      -Takes all of the students and turns them into keys to a boolean'
      -If the method reaches that value, it is reassigned to true
      -A way to check true or false of every value, so we don't need to read through the whole list
"""

import random

krewes = {
          2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"], 
          7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"], 
          8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
         }

testKrewes = {2:["Anson", "Efe", "Faiza"], 7:["Ravindra", "Emily", "Sadi"], 8:["Sasha", "Shreya", "Jeffery"]}

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
print("Pre-Testing:")
print("\tSmall Sample Test")
for i in range(10):
  randFromDictOfArr(testKrewes)

#FOR LOOP TO VERIFY THAT RESULTS ARE RANDOM // RUNS HUNDRED TIMES (Also working with empty case)
print("\tTesting with empty arrays in dictionary")
print(testing)
for i in range(100):
  randFromDictOfArr(testing)

#Showing that it works with krewes
print("\nTesting with the krewes dictionary:")
for i in range(10):
  randFromDictOfArr(krewes)

for i in range(100):
  randFromDictOfArr(krewes)


"""
#For proving that the randomizer will hit every person by Ravindra
def fixKrewes(krewes):
  listOfKeys = list(krewes.keys())
  for i in listOfKeys:
    for j in range(len(krewes[i])):
      krewes[i][j] = [False, krewes[i][j]]
  return krewes

def revisedRFDOA (dictionary):
  listOfKeys = list(dictionary.keys())
  #print(ListOfKeys)
  pickingFromKeys= random.choice(listOfKeys)
  #print(pickingFromKeys)
  arrFromDict = dictionary[pickingFromKeys]
  while (len(arrFromDict) <= 0):
    pickingFromKeys= random.choice(listOfKeys)
    arrFromDict = dictionary[pickingFromKeys]
  pickingFromArr = random.choice(arrFromDict)
  pickingFromArr[0] = True

def proof():
  proofKrewes = fixKrewes(krewes)
  for i in range(1000):
    revisedRFDOA(proofKrewes)
  listOfKeys = list(krewes.keys())
  for i in listOfKeys:
    print(i)
    for j in range(len(krewes[i])):
      print(krewes[i][j])

proof()
"""
"""
print(krewes.keys())
for i in krewes.keys():
  print(i)
"""

"""
def remadeFooKrewes():
  choice = -1
  num = random.randrange(0, len(krewes.keys()))
  counter = 0
  for i in krewes.keys():
    if (counter == num):
      choice = i
      break
    counter += 1
  random.shuffle(krewes[choice])
  
  
  return(krewes[choice][0])
  
for i in range(10):
  print(remadeFooKrewes())

def setUp():
  tagCheck = {}
  for i in krewes:
    for j in krewes[i]:
      tagCheck[j] = False
  return(tagCheck)
  
def check():
  tagCheck = setUp()
  for i in range(1000):
    tagCheck[remadeFooKrewes()] = True
  print(tagCheck)
  for i in tagCheck:
    if (not tagCheck[i]):
      print(i)

print(setUp())
print("\n")
check()
"""
