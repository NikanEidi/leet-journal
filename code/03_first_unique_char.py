# First character that appears exactly once in a string (solved cold,
# no hints). "swiss" -> "w". 2026-10-12.

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