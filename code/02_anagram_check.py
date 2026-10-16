# Python Fundamentals — Hash Map Pattern (Anagram Check)
# Session: learn-from-zero, 2026-10-12
# Write your own code below each prompt. Run with: python3 02_anagram_check.py

# Problem: Given two strings, check if one is an anagram of the other

p_str = "Nikan"
s_str = "Hello"
counts = {}
is_anagram = True

if len(p_str) != len(s_str):
    is_anagram = False

for letter in p_str:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1

for letter in s_str:
    if letter in counts:
        counts[letter] -= 1
    else:
        is_anagram = False
if is_anagram == True:
    print("Anagram")
else:
    print("Not Anagram")
