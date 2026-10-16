# Python Fundamentals — Hash Map Pattern (Two Sum)
# Session: learn-from-zero, 2026-10-12
# Write your own code below each prompt. Run with: python3 01_two_sum.py

# Problem: Given nums and target, return the indices of the two numbers
# that add up to target. Use a dict for O(n), not a nested loop.

nums = [2,4,6,8,10,12,14]
target = 8 
seen = {}

for i,v in enumerate(nums):
    complement = target - v
    if complement not in seen:
        seen[v] = i
    else:
        print([seen[complement], i])

