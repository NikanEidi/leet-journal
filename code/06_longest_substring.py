# Longest Substring Without Repeating Characters — sliding window + hashmap.
# Given a string, return the length of the longest substring with no
# repeating characters. "abcabcbb" -> 3 (e.g. "abc").

s = "abcabcbb"
m_last_seen = {}
p_start = 0
longest_path = 0

for p_end, value in enumerate(s):
    
    if value in m_last_seen and m_last_seen[value] >= p_start:
       
        p_start = m_last_seen[value] + 1
        
   
    m_last_seen[value] = p_end
    
    
    longest_path = max(longest_path, p_end - p_start + 1)

print(longest_path)