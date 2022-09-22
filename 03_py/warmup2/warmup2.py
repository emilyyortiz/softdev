import random

def string_times(str, n):
	#Python has the unique ability to multiply strings, repeating n times
  return n * str

print("Test Cases for StringTimes");
print(string_times("HelpMe ", 5))
print("Checking without eyes");
strTimesTest = "";
Message = "What are the three numbers on the back of your credit card"
for i in range(1200):
    strTimesTest += Message
print((string_times(Message, 1200) == strTimesTest))

print("\n")

def front_times(str, n):
	#First we check for length, because if it has less, we only use the string
  if len(str) < 3:
    return n * str
  else:
    return n * str[:3]
print ("Test Cases for FrontTimes")
print( "For full strings used:")
Message = "No"
print (front_times(Message, 900) == string_times(Message, 900))
print("For slice of string used:")
Message = "Somebody Once Told Me"
print(front_times(Message, 1776) == string_times(Message[:3], 1776))

print("")

print("Testing StringBits")
def string_bits(str):

  n = 0
  ret_str = ""
  while n < len(str):
    ret_str += str[n]
    #By incrementing by 2, we can skip over 1 index each time without checking with %
    n += 2
  return ret_str
def bitsTest (str):
     answerString = ""
     for i in range(len(str)):
         if (i % 2 == 0):
             answerString += str[i]
     return answerString

for times in range(10):
    Message = ""
    for i in range(1000):
        num = random.randrange(1000)
        Message += str(num)
    print(string_bits(Message) == bitsTest(Message))

print("")

print("Testing StringSplosion")
def string_splosion(str):
  ret_str = ""
  #Looping len times
  for i in range(len(str)):
  #Slicing the str up to i, making sure to add 1 to include the index i
    ret_str += str[:i+1]
  return ret_str

Message = "ABCDEFGHI"
print(string_splosion(Message))
print("Empty Test Case: " + string_splosion(""))

print("")

print("Testing Last 2")
def last2(str):
  #Counter of repetitions
  ret_ctr = 0
  #The final substring we need
  end_str = str[len(str) - 2:]
  #looping thorugh everything besides the final substring we already separated
  for i in range(len(str)-2):
    if end_str == str[i:i+2]:
      ret_ctr += 1
  return ret_ctr

for reps in range(10):
    Message = ""
    subMessage = ""
    counter = 0
    for i in range(2):
        subMessage += str(random.randrange(10))
    for i in range (1000000):
        digit = random.randrange(10)
        Message += str(digit)
        if Message[-2:] == subMessage:
            counter += 1
    Message += subMessage
    print(counter == last2(Message))
#print(counter)
#print(last2(Message))
#print(Message)
#print(subMessage)

print("")

print("Testing Array Count 9")
def array_count9(nums):
  ret_ctr = 0
  #A loop that pulls the number out while ignoring index, i is a value in the array
  for i in nums:
    if i == 9:
      ret_ctr += 1
  return ret_ctr

testArr = []

nineCount = 0
for reps in range(10):
    for i in range (1000000):
        num = (random.randrange(100))
        if num == 9:
            nineCount += 1
        testArr.append(num)
    print(nineCount == array_count9(testArr))


print("")

print("Testing Array Front 9")
def array_front9(nums):
	#Using a slice to look at only the first 4. Even if the length is less than 4, there will be no problems b/c i is the value in the array
  for i in nums[:4]:
    if i == 9:
      return True
  return False

for reps in range(10):
    nineCount = 0
    testArr = []
    for i in range (random.randrange(10)):
        num = random.randrange(10)
        if (num == 9 and i < 4):
            nineCount = 1
        testArr.append(num)
    print(nineCount == array_front9(testArr))
    if not nineCount == array_front9(testArr):
        print("\t" + str(testArr) + "\n\tNine Count: " + str(nineCount) + "\n\tFunction Count: "+ str(array_front9(testArr)))

print("")

print("Testing Array123")
def array123(nums):
  for i in range(len(nums)-2):
    #Using a loop to change the slice of the array
    if nums[i: i+3] == [1, 2, 3]:
           return True
  return False

for i in range(10):
    testArr = []
    for j in range(25):
        testArr.append(random.randrange(4))
    print(str(testArr))
    print("\tCount: " + str(array123(testArr)))

print("")

print("Testing StringMatch")
def string_match(a, b):
  output = 0
  key = ""
  other = ""
  #Establishing the shorter array as a key to preven IndexOutOfBounds Errors
  if len(a) < len(b):
    key = a
    other = b
  else:
    key = b
    other = a
  for i in range(len(key)-1):
    #Comparing slices of the strings
    if key[i:i+2] == other[i:i+2]:
      output += 1
  return output

for reps in range(10):
    MessageA = ""
    MessageB = ""
    for i in range(random.randrange(10)):
        MessageA += str(random.randrange(2))
    for i in range(random.randrange(10)):
        MessageB += str(random.randrange(2))
    print(str(string_match(MessageA, MessageB)))
    print("\t" + MessageA)
    print("\t" + MessageB)

#for i in range(100):
#    print(random.randrange(10))
