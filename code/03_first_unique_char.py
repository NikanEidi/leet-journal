# Python Fundamentals — First Non-Repeating Character (COLD, no steps given)
# Session: learn-from-zero, 2026-10-12
# Write your own code below. Run with: python3 03_first_unique_char.py

# Problem: given a string, return the first character that appears exactly
# once in the whole string. Return None if there isn't one.
# Example: "swiss" -> "w"

p_string = "swiss"
count = {}

for word in p_string:
    if word in count:  
        count[word] += 1
    else:
        count[word] = 1

p_unique = None
for u_word in p_string:
    if count[u_word] == 1:
        p_unique = u_word
        break  

print(p_unique)