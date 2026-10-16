# Python Fundamentals — Hash Map Pattern (Group Anagrams, COLD — no steps given)
# Session: DSA problem-solving practice, 2026-10-16
# Write your own code below. Run with: python3 04_group_anagrams.py

# Problem: given a list of words, group the ones that are anagrams of each
# other (made from the exact same set of letters). Return a list of groups.
# Example: ["eat", "tea", "tan", "ate", "nat", "bat"]
#       -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
counts = {}

for word in words:
    key = "".join(sorted(word))
    if key in counts:
        counts[key].append(word)
    else:
        counts[key] = [word]
print(counts)