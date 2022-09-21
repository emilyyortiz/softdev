def count_evens(nums):
  # counter for even ints
  ctr = 0
  # go through array
  for i in nums:
    # if number is even
    if i % 2 == 0:
      # add one to the counter
      ctr += 1
  return ctr

print(count_evens([2, 1, 2, 3, 4])) # → 3
count_evens([2, 2, 0]) # → 3
count_evens([1, 3, 5]) # → 0

def big_diff(nums):
    minimum = nums[0]
    maximum = nums[0]
    # go through array
    for i in range(len(nums)):
        # if the current element is bigger or smaller,
        # adjust the minimum and maximum
        minimum = min(minimum, nums[i])
        maximum = max(maximum, nums[i])
    return maximum - minimum

print(big_diff([10, 3, 5, 6])) # → 7
big_diff([7, 2, 10, 9]) # → 8
big_diff([2, 10, 7, 2]) # → 8

def centered_average(nums):
    minimum = nums[0]
    maximum = nums[0]
    total = 0
    # go through array
    for i in range(len(nums)):
        # if the current element is bigger or smaller,
        # adjust the minimum and maximum
        minimum = min(minimum, nums[i])
        maximum = max(maximum, nums[i])
        # add current element total
        total += nums[i]
    # return centered avg (mean w/out max and min)
    return (total - maximum - minimum) / (len(nums) - 2)

print(centered_average([1, 2, 3, 4, 100])) # → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) # → 5
centered_average([-10, -4, -2, -4, -2, 0]) # → -3

def sum13(nums):
  total = 0
  # special case
  if len(nums) == 0:
      return total
  # counter int
  i = 0
  while i < len(nums):
      # if number is 13, ignore it and the next number
      if nums[i] == 13:
          i += 2
      # if number is not 13, add it to the total
      else:
          total += nums[i]
          i += 1
  return total

print(sum13([1, 2, 2, 1])) # → 6
sum13([1, 1]) # → 2
sum13([1, 2, 2, 1, 13]) # → 6

def sum67(nums):
    total = 0
    #special case