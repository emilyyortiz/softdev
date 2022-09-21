def first_last6(nums):
    return nums[0] == 6 or nums[len(nums)-1] == 6

def same_first_last(nums):
    if len(nums) == 0:
        return False
    same = nums[0] == nums[len(nums)-1]
    length = len(nums) >= 1
    return same and length

def make_pi():
  return [3, 1, 4]

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]  

def sum3(nums):
  return sum(nums)

def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]
  
def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

def max_end3(nums):
  #finding the larger value
  bigger = max(nums[0], nums[-1])
  #Loop for replacing vals
  for i in range(len(nums)):
    nums[i] = bigger
  return nums

def sum2(nums):
  #special case 0
  if len(nums) == 0: 
    return 0
  #special case 1
  elif len(nums) == 1:
    return nums[0]
  else :
    return nums[0] + nums[1]

def middle_way(a, b):
  # middle element has index 1
  return [a[1], b[1]]

def make_ends(nums):
  # -1 is index of last element
  return [nums[0], nums[-1]]

def has23(nums):
  # in determines if an element is in an array
  return 2 in nums or 3 in nums
