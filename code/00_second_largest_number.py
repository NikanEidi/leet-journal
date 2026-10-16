# Second largest number in a list, without sort() or max(). 2026-10-10.

m_list = [10, 3, 9]
if m_list[0] > m_list[1]:
    p_current_max = m_list[0]
    s_current_max = m_list[1]
else:
    p_current_max = m_list[1]
    s_current_max = m_list[0]


for item in m_list:
    if item > p_current_max:
        s_current_max = p_current_max
        p_current_max = item
    elif item  > s_current_max and item < p_current_max:
        s_current_max = item
print(s_current_max)