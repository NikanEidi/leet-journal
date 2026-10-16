# Pattern: Hashmap (dictionary)

I use this whenever I need to count something, look something up fast, or group things together. The mental model I keep in my head: if I catch myself writing a nested loop just to check "have I seen this before," that's the signal a hashmap would do it in one pass instead. Average O(1) insert, lookup, and delete.

## Second Largest Number — 2026-10-10

Find the second-largest number in a list without using `sort()` or `max()`. I tracked two running values as I went — the current max and the current second-max — updating both in a single pass depending on where the new number landed compared to each. No hashmap here, just the warmup that got me thinking in terms of "keep running state instead of rescanning."

```python
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
    elif item > s_current_max and item < p_current_max:
        s_current_max = item
print(s_current_max)
```

## Two Sum — 2026-10-12

Given a list of numbers and a target, find the two numbers that add up to it. I built a dict as I went: for each number, I check whether its complement (target minus the number) is already in the dict. If it is, I've found my pair. If not, I add the current number to the dict and keep going. One pass, O(n), instead of checking every pair with a nested loop.

```python
nums = [2, 4, 6, 8, 10, 12, 14]
target = 8
seen = {}

for i, v in enumerate(nums):
    complement = target - v
    if complement not in seen:
        seen[v] = i
    else:
        print([seen[complement], i])
```

## Anagram Check — 2026-10-12

Given two strings, check if they're anagrams of each other. I counted every letter of the first string into a dict, then walked the second string subtracting from those same counts. If a letter from the second string isn't in the dict at all, they can't be anagrams. I also check the lengths up front, since two strings of different lengths can never be anagrams no matter what the letters are.

```python
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

print("Anagram" if is_anagram else "Not Anagram")
```

## First Unique Character — 2026-10-12

Solved cold, no hints given beforehand. Given a string, return the first character that appears exactly once. I counted every character first, then walked the string a second time looking for the first one whose count is exactly 1. Two passes, but both are O(n), so it stays linear overall.

```python
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
```

## Group Anagrams — 2026-10-16

Solved cold. Given a list of words, group every set of anagrams together. The insight I needed: if I sort the letters of a word, every anagram of that word sorts to the exact same string — so the sorted letters become a shared key. I loop through the words, build that key for each one, and either append to an existing group in my dict or start a new one.

I got stuck for a second right at the start — I wrote `if words[]`, trying to check against the original list instead of a separate dict I hadn't built yet. Once I separated the two pieces in my head — building the key with `sorted()` + `"".join()`, then checking that key against my own dict, not the input list — the rest came together on the first try and matched the expected output exactly.

```python
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
counts = {}

for word in words:
    key = "".join(sorted(word))
    if key in counts:
        counts[key].append(word)
    else:
        counts[key] = [word]

print(counts)
# {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
```

## Contains Duplicate — 2026-10-16

Solved cold. Given a list of numbers, return whether any value repeats. I wrote two versions.

The first one counts every number into a dict, then does a second pass checking whether any count is 2 or more. It works, but it always does two full passes even if a duplicate shows up in the first two elements.

```python
nums = [1, 2, 3, 1]
m_counter = {}
found_duplicate = False

for i in nums:
    if i in m_counter:
        m_counter[i] += 1
    else:
        m_counter[i] = 1

for i in m_counter:
    if m_counter[i] >= 2:
        found_duplicate = True
        break

print(found_duplicate)
```

The second one checks and inserts in the same single pass — the moment I see a number that's already in my dict, I know the answer and can stop right there without reading the rest of the list.

```python
m_seen = {}
found_duplicate = False

for number in nums:
    if number in m_seen:
        found_duplicate = True
        break
    else:
        m_seen[number] = True

print(found_duplicate)
```

## Still ahead for this pattern

Longest Substring Without Repeating Characters — a hashmap combined with a sliding window. This is the bridge into the two-pointer pattern.

## Common mistakes I actually hit

- Checking a list of keys I built instead of the dict I'm supposed to be checking.
- Printing or returning something unconditionally, so it fires even when it shouldn't.
- Printing inside a loop when I actually want one final answer for the whole input, not one per item.
- Using a flag variable inside a loop without initializing it before the loop, in case the loop never sets it.

## When I would NOT reach for a hashmap

- When the order of things actually matters and I need that order preserved as-is — a dict in Python 3.7+ keeps insertion order, but if I'm doing index math, a plain list is still the right tool.
- When I'm only ever comparing two or three fixed elements — a hashmap is overkill for that.
