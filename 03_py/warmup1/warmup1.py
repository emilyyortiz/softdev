def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  else:
    return False

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  if a == b:
    return 2*(a+b)
  return a+b  

def diff21(n):
  if n > 21:
    return 2 * abs(n - 21)
  else:
    return abs(n - 21)
    
def parrot_trouble(talking, hour):
  if talking == True and (hour < 7 or hour > 20):
    return True
  else:
    return False

def makes10(a, b):
  if a == 10 or b == 10 or a+b == 10:
    return True
  else:
    return False
    
def near_hundred(n):
  return abs(n - 100) <= 10 or abs(n - 200) <= 10
  
def pos_neg(a, b, negative):
  if negative == True:
    return a < 0 and b < 0
  else:
    return (a < 0) ^ (b < 0)

def not_string(str):
  if str[:3] == "not":
    return str
  else:
    return "not " + str

def missing_char(str, n):
  return str[:n] + str[n + 1:]

def front_back(str):
  if len(str) <= 1:
    return str
  else:
    return str[len(str) - 1] + str[1:len(str) - 1] + str[0]

def front3(str):
  if len(str) < 3:
    return 3 * str
  else:
    return 3 * str[:3]
