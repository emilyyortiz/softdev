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
  