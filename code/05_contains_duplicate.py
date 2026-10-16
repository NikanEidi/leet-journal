# Contains Duplicate — does any number repeat in the list? (solved cold,
# no hints). Two versions: counting first, then a faster early-exit one.
# 2026-10-16.

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