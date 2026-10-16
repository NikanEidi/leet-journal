# Anagram check — are two strings made of the exact same letters? 2026-10-12.

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
