# Two Sum — find the two numbers in nums that add up to target, return
# their indices. Using a dict instead of a nested loop. 2026-10-12.

nums = [2,4,6,8,10,12,14]
target = 8 
seen = {}

for i,v in enumerate(nums):
    complement = target - v
    if complement not in seen:
        seen[v] = i
    else:
        print([seen[complement], i])

