"""
TNPG: Wasabi Rain
Featuring Thinkeren: Emily, Sadi, Ravindra
Software Development, Period 7
September 2022
"""

def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  else:
    return False

#sleep_in(weekday, vacation) returns True if it is not a weekday and/or if it is a vacation day. Otherwise, it returns False.
print(sleep_in(True, False))   #TEST CASE A: sleep_in(True, False) -> False
print(sleep_in(False, False))  #TEST CASE B: sleep_in(False, False) -> True
print(sleep_in(True, True))    #TEST CASE C: sleep_in(True, True) => True

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

#monkey_trouble(a_smile, b_smile) returns True if a_smile is equal to b_smile. Otherwise, it returns False.
print(monkey_trouble(True, True))   #TEST CASE A: monkey_trouble(True, True) -> True
print(monkey_trouble(False, False)) #TEST CASE B: monkey_trouble(False, False) -> False
print(monkey_trouble(True, False))  #TEST CASE C: monkey_trouble(True, False) -> False

def sum_double(a, b):
  if a == b:
    return 2*(a+b)
  return a+b  

#sum_double(a, b) returns the sum of inputs a and b, unless a is equal to b, where the function instead turns double the sum of a and b.
print(sum_double(2, 3))   #TEST CASE A: sum_double(2, 3) -> 5
print(sum_double(3, 6))   #TEST CASE B: sum_double(3, 6) -> 9
print(sum_double(6, 6))   #TEST CASE C: sum_double(6, 6) -> 24

def diff21(n):
  if n > 21:
    return 2 * abs(n - 21)
  else:
    return abs(n - 21)
    
#diff21(n) returns the absolute value of the input n minus 21 to find the difference between n and 21. If input n is greater than 21, the function returns two times the difference between the absolute value of n and 21.
print(diff21(14))   #TEST CASE A: diff21(14) -> 7
print(diff21(18))   #TEST CASE B: diff21(18) -> 3
print(diff21(22))   #TEST CASE C: diff21(22) -> 2

def parrot_trouble(talking, hour):
  if talking == True and (hour < 7 or hour > 20):
    return True
  else:
    return False

#parrot_trouble(talking, hour) returns True if input talking is True, and the input hour is less than 7 or greater than 20, thus representing before 7:00AM or after 8:00PM. Else, this function returns False.
print(parrot_trouble(False, 19))   #TEST CASE A: parrot_trouble(False, 19) -> False
print(parrot_trouble(True, 8))     #TEST CASE B: parrot_trouble(True, 8) -> True
print(parrot_trouble(True, 23))    #TEST CASE C: parrot_trouble(True, 23) -> False

def makes10(a, b):
  if a == 10 or b == 10 or a+b == 10:
    return True
  else:
    return False
    
#makes10(a, b) returns True if input a, b, or the sum of inputs a and b are equal to 10. Otherwise, this function returns False.
print(makes10(2, 10))    #TEST CASE A: makes10(2, 10) -> True
print(makes10(2, 2))     #TEST CASE B: makes10(2, 2) -> False
print(makes10(4, 6))     #TEST CASE C: makes10(4, 6) -> True

def near_hundred(n):
  return abs(n - 100) <= 10 or abs(n - 200) <= 10
  
#near_hundred(n) returns True if n is within 10 numbers between 100 or 200. Else, it returns False.
print(near_hundred(211))   #TEST CASE A: near_hundred(211) -> False
print(near_hundred(94))    #TEST CASE B: near_hundred(94) -> True
print(near_hundred(309))   #TEST CASE C: near_hundred(309) -> False

def pos_neg(a, b, negative):
  if negative == True:
    return a < 0 and b < 0
  else:
    return (a < 0) ^ (b < 0)

#pos_neg(a, b, negative) has two paths based on the value of negative. If input negative is equal to True, the function returns True if and only if both inputs a and b are less than 0. Else, if negative is equal to False, the function returns True if and only if a or b, but not a and b, are less than 0.
print(pos_neg(-1, -3, False))   #TEST CASE A: pos_neg(-1, -3, False) -> False
print(pos_neg(-4, 2, True))     #TEST CASE B: pos_neg(-4, 2, True) -> True
print(pos_neg(-3, -4, True))      #TEST CASE C: pos_neg(-3, -4, True) -> True

def not_string(str):
  if str[:3] == "not":
    return str
  else:
    return "not " + str

#not_string(str) returns input str if the first three characters of the string are equal to "not." Else, the function adds "not" before the str and returns str.
print(not_string("not bread")   #TEST CASE A: not_string("not bread") -> "not bread"
print(not_string("bread")       #TEST CASE B: not_string("bread") -> "not bread"
print(not_string("not not bread")   #TEST CASE C: not_string("not not bread") -> "not not bread"

def missing_char(str, n):
  return str[:n] + str[n + 1:]

#missing_char(str, n) returns input str with the character at index n being removed.
print(missing_char("Psychodynamic", 3))   #TEST CASE A: missing_char("Psychodynamic", 3) -> "Psyhodynamic"
print(missing_char("Biological", 0))   #TEST CASE B: missing_char("Biological", 0) -> "iological"
print(missing_char("Social", 2))   #TEST CASE C: missing_char("Social", 2) -> "Soial"

def front_back(str):
  if len(str) <= 1:
    return str
  else:
    return str[len(str) - 1] + str[1:len(str) - 1] + str[0]

#front_back(str) swaps the first character with the last character of input str.
print(front_back("water")   #TEST CASE A: front_back("water") -> "ratew"
print(front_back("cola")    #TEST CASE B: front_back("cola") -> "aolc"
print(front_back("juice")   #TEST CASE C: front_back("juice") -> "euicj"

def front3(str):
  if len(str) < 3:
    return 3 * str
  else:
    return 3 * str[:3]

#front3 triples the first 3 characters of str three times before returning str. If the length of str is lower than 3, the function returns the entire length of the function three times before returning str.
print(front3("Ma"))   #TEST CASE A: front3("Ma") -> "MaMaMa"
print(front3("Dong")) #TEST CASE B: front3("Dong") -> "DonDonDon"
print(front3("Ortiz"))  #TEST CASE C: front3("Ortiz") -> "OrtOrtOrt"
