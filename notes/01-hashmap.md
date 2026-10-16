# 🗂️ Pattern 01 — Hashmap (Dictionary)

**When to use:**
- Counting things
- Fast lookup ("have I seen this before?")
- Grouping (anagrams, categories)
- Two-sum style (complement lookup)

**Big O:** average O(1) insert, lookup, delete. Space O(n).

**The mental model:** whenever you catch yourself doing nested loops to check something, ask: *"can I trade space for time with a hashmap?"* — usually yes.

---

## 🎯 The 5 core problems (solve in this order)

### 1. Word Frequency (warmup)

**Problem:** given an array of words, return a dictionary of word → count.

```javascript
function wordFrequency(words) {
  const counts = {};
  for (const word of words) {
    counts[word] = (counts[word] || 0) + 1;
  }
  return counts;
}
```

**Key trick:** `counts[word] || 0` handles the missing key case.

**Test:**
```javascript
wordFrequency(['apple', 'banana', 'apple']);
// { apple: 2, banana: 1 }
```

**Narration to say out loud:**
> "I'll use a dictionary to count. For each word, if it's already there I add one. Otherwise I start at zero plus one, which is one. Return the dict."

---

### 2. Two Sum

**Problem:** given an array `nums` and a target, return indices of two numbers that add to target.

**Brute force (O(n²) — DON'T ship this in an interview, but MENTION it first):**
```javascript
function twoSumBrute(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }
  return null;
}
```

**Hashmap solution (O(n)):**
```javascript
function twoSum(nums, target) {
  const seen = {};
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (complement in seen) {
      return [seen[complement], i];
    }
    seen[nums[i]] = i;
  }
  return null;
}
```

**Narration:**
> "For each number, I check if its complement is in the seen dict. If yes, return the two indices. Otherwise add current to the dict. This trades space for time — O(n) instead of O(n²)."

**Trap:** add to dict AFTER checking, not before. Otherwise duplicate values fail.

---

### 3. Contains Duplicate

**Problem:** return true if any value appears twice.

**Simple:**
```javascript
function hasDup(arr) {
  return new Set(arr).size !== arr.length;
}
```

**Early-exit (better for huge inputs):**
```javascript
function hasDup(arr) {
  const seen = new Set();
  for (const x of arr) {
    if (seen.has(x)) return true;
    seen.add(x);
  }
  return false;
}
```

**My actual session (2026-10-16, Python, `05_contains_duplicate.py`) — real bugs hit, not the clean version above:**
1. Solved it the "counting" way first (dict of value → count, then a second loop checking for any count ≥ 2) — works, but two passes and a full dict even if the first two elements are already a duplicate.
2. First real bug: wrote `return True` / `return False` at the top level of the file, outside any function → `SyntaxError: 'return' outside function`. `return` only means something inside a `def`.
3. Fixed it to `print(...)`, but then wrote `print(False)` **unconditionally**, outside the `if` — so it printed both `True` (from inside the loop, when found) and `False` (always, right after) on every run. Looked like a logic bug but was really an indentation/placement bug: the unconditional line needs to be the *only* line that decides the final answer, not a leftover default sitting next to the real one.
4. Next attempt put the print inside `if`/`else` of the counting loop — ran, but printed once *per key* in the dict (`True`, `False`, `False` for 3 keys) instead of one final answer for the whole array. The fix (flag + `break`) is the actual bridge from "checking every element independently" to "stopping as soon as the array-level question is answered."
5. Wrote the flag version (`found_duplicate = True; break`) but forgot to initialize `found_duplicate = False` before the loop — worked fine on `[1,2,3,1]` (duplicate exists, gets set), but on a no-duplicate input like `[1,2,3,4]` it crashed with `NameError: name 'found_duplicate' is not defined`, because the variable is only ever created inside the `if` branch that never ran. Lesson: a flag that might never get set inside a loop has to be initialized *before* the loop, every time — this is the single most common hashmap/loop bug in this whole session.
6. Then wrote the real early-exit version (single loop, `set`-style dict, `break` on first repeat) — correct in one try once the counting version's bugs were already worked out.

---

### 4. Group Anagrams

**Problem:** group words that are anagrams of each other.

```javascript
function groupAnagrams(words) {
  const groups = {};
  for (const word of words) {
    const key = word.split('').sort().join('');
    if (!groups[key]) groups[key] = [];
    groups[key].push(word);
  }
  return Object.values(groups);
}
```

**Key insight:** sorted letters = canonical key. Anagrams share the key.

**Narration:**
> "For each word, sort its letters to make a key. All anagrams share that key. Group them in a dict, return the values."

**My actual session (2026-10-16, Python, `04_group_anagrams.py`) — solved COLD, no steps given:**
Got stuck for a moment at the very start (`for word in words: if words[]`) — reached for indexing into the original array before realizing the thing that needs checking is a *separate* dict being built up, not `words` itself. Once talked through two pieces separately — (1) `sorted(word)` returns a list of characters, (2) `"".join(...)` turns that list back into a string key — assembled the full three-line loop body correctly on the first try: build key, `if key in counts: append`, `else: start a new list`. Ran clean, matched the expected grouping exactly on the first run.

### 5. Longest Substring Without Repeating Characters (harder)

**Problem:** given a string, return length of the longest substring without repeating chars.

```javascript
function longestUnique(s) {
  const lastSeen = {};
  let start = 0;
  let best = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] in lastSeen && lastSeen[s[i]] >= start) {
      start = lastSeen[s[i]] + 1;
    }
    lastSeen[s[i]] = i;
    best = Math.max(best, i - start + 1);
  }
  return best;
}
```

**Combined pattern:** sliding window + hashmap. This bridges into the two-pointer pattern.

---

## 🚨 Common Mistakes

- `counts[word] += 1` without initializing → NaN + 1 → NaN. Use `(counts[word] || 0) + 1`.
- Using `hasOwnProperty` when a simple `in` check works
- Forgetting that JS object keys are strings — numbers get coerced. If you need real numeric keys, use `Map`.
- Nested loops when a hashmap would work — the sign you're missing this pattern

---

## 💡 When NOT to use hashmap

- When order matters strictly (use array)
- When memory is really tight (hashmaps are big)
- When you only have 2 elements to compare (overkill)

---

## 🎤 Interview soundbites

- *"I'll trade space for time with a hashmap — O(n) instead of O(n²)."*
- *"For lookup problems, hashmap is usually my first tool."*
- *"I'll check if we've seen it before, and if not, add it to the dict."*
