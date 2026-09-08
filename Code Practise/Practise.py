from collections import Counter
counter = Counter("tigeranalytics");

def first_non_repeating(s):
  count = Counter(s)
  for i, val in enumerate(s):
    if count[val] == 1:
      return i
  return -1

def find_duplicate(n):
  count = Counter(n)
  duplicates = []
  for key, val in count.items():
    if count[val] > 1:
      duplicates.append(key)
  return duplicates

print(first_non_repeating("aabbcc"))
print(find_duplicate([1,2,3,3,4,5,2]))

dict =  {1:1, 2:3, "a": 1, "a":1, 1:1}
print(dict)

def move_zeros(nums):
  zeros_count = 0
  for i in nums:
    if i == 0:
      zeros_count += 1
      nums.remove(i)
  if(zeros_count > 0):
    for i in range(zeros_count):
      nums.append(0)
  return nums
       
print(move_zeros([1,0,3,0,5,9]))

def ind_missing_log_ids(logs):
  missing = []
  for i in range(logs[0],logs[-1]):
    if i not in logs:
      missing.append(i)
  return missing

print(ind_missing_log_ids([1,3,4,5,6,10]))

# finding palinedrome without using built-in function
def is_palindrome(str):
  s = str.lower().replace(" ", "")
  def reverse(s):
    string = ""
    for i in range(len(s)-1, -1, -1):
      string += s[i]
    return string
  print("reverse",reverse(s))
  return s == reverse(s)

print(is_palindrome("Race car"))


def palindrome(txt):
  s = txt.replace(" ", "").lower()
  print(s)
  left, right = 0, len(s) - 1
  while left < right:
    print(s[left] , s[right])
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True
print(palindrome("Race car"))
