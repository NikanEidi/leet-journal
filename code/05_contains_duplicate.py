# Python Fundamentals — Hash Map Pattern (Contains Duplicate, COLD — no steps given)
# Session: DSA problem-solving practice, 2026-10-16
# Write your own code below. Run with: python3 05_contains_duplicate.py

# Problem: given an array of numbers, return True if any value appears at
# least twice, otherwise return False.
# Example: [1, 2, 3, 1] -> True
# Example: [1, 2, 3, 4] -> False

nums = [1, 2, 3, 1]
m_counter = {}
found_duplicate  = False


for i in nums:
    m_dup = i
    if m_dup in m_counter:
        m_counter[m_dup] += 1
    else:
        m_counter[m_dup] = 1 

for i in m_counter:
    if m_counter[i] >= 2:
        found_duplicate = True
        break

print(found_duplicate)
    
# Second Version
m_seen = {}
for number in nums:
    if number in m_seen:
        found_duplicate = True
        break
    else:
        m_seen[number] = True

print(found_duplicate)