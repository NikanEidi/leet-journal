# Group Anagrams — group words made of the same letters (solved cold,
# no hints). ["eat","tea","tan","ate","nat","bat"]
#   -> [["eat","tea","ate"], ["tan","nat"], ["bat"]]. 2026-10-16.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
counts = {}

for word in words:
    key = "".join(sorted(word))
    if key in counts:
        counts[key].append(word)
    else:
        counts[key] = [word]
print(counts)