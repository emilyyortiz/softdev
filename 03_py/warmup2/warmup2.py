def string_times(str, n):
  return n * str  

def front_times(str, n):
  if len(str) < 3:
    return n * str
  else:
    return n * str[:3]

def string_bits(str):
  n = 0
  ret_str = ""
  while n < len(str):
    ret_str += str[n]
    n += 2
  return ret_str

def string_splosion(str):
  ret_str = ""
  for i in range(len(str)):
    ret_str += str[:i+1]
  return ret_str

def last2(str):
  ret_ctr = 0
  end_str = str[len(str) - 2:]
  for i in range(len(str)-2):
    if end_str == str[i:i+2]:
      ret_ctr += 1
  return ret_ctr

def array_count9(nums):
  ret_ctr = 0
  for i in nums:
    if i == 9:
      ret_ctr += 1
  return ret_ctr

def array_front9(nums):
  for i in nums[:4]:
    if i == 9:
      return True
  return False

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1:
      if nums[i+1] == 2:
         if nums[i+2] == 3:
           return True
  return False

def string_match(a, b):
  output = 0
  key = ""
  other = ""
  if len(a) < len(b):
    key = a
    other = b
  else:
    key = b
    other = a
  for i in range(len(key)-1):
    if key[i:i+2] == other[i:i+2]:
      output += 1
  return output
