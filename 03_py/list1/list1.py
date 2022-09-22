"""
TNPG: Wasabi Rain
Featuring Thinkeren: Emily, Sadi, Ravindra
Software Development, Period 7
September 2022
"""

def first_last6(nums):
    #returns True if the first or last elements is 6
    return nums[0] == 6 or nums[len(nums)-1] == 6

print(first_last6([1, 3, 2, 6])) #True
print(first_last6([6, 3, 2, 1])) #True
print(first_last6([3, 2, 1, 1])) #True

def same_first_last(nums):
    #returns True if the first and last characters in the list are equal
    if len(nums) == 0:
        return False
    same = nums[0] == nums[len(nums)-1]
    length = len(nums) >= 1
    return same and length

print(same_first_last([1, 2, 3, 1])) #True
print(same_first_last([1, 2, 3, 4])) #False

def make_pi():
  #returns the first three digits of pi
  return [3, 1, 4]

print(make_pi()) #[3, 1, 4]

def common_end(a, b):
  #returns True if the end characters of two words are the same
  return a[0] == b[0] or a[-1] == b[-1]  

print(common_end("whips", "glowsticks")) #True
print(common_end("stuysquad, sos")) #False

def sum3(nums):
  #returns the sum of 3 numbers
  return sum(nums)

print(sum3([1, 2, 3])) #6

def rotate_left3(nums):
  #rotates the list, as if it was a circular node list
  return [nums[1], nums[2], nums[0]]

print(rotate_left3([2, 3, 1])) #[3, 1, 2]
  
def reverse3(nums):
  #reverses the list
  return [nums[2], nums[1], nums[0]]

print(reverse3([3, 2, 1])) #[1, 2, 3]

def max_end3(nums):
  #finding the larger value
  bigger = max(nums[0], nums[-1])
  #Loop for replacing vals
  for i in range(len(nums)):
    nums[i] = bigger
  return nums

print(max_end3([17, 5, 3])) #[17, 17, 17]

def sum2(nums):
  #special case 0
  if len(nums) == 0: 
    return 0
  #special case 1
  elif len(nums) == 1:
    return nums[0]
  else :
    return nums[0] + nums[1]

print(sum2([2, 4])) #6
print(sum2([3])) #3
print(sum2([])) #0

def middle_way(a, b):
  # middle element has index 1
  return [a[1], b[1]]

print(middle_way([3, 4, 5], [4, 5, 6])) #[4, 5]

def make_ends(nums):
  # -1 is index of last element
  return [nums[0], nums[-1]]

print(make_ends([1, 2, 3, 4, 5])) #[1, 5]

def has23(nums):
  # in determines if an element is in an array
  return 2 in nums or 3 in nums

print(has23([2, 3, 2, 3, 1])) #True
