# Pattern: Greedy + Heap (Priority Queue)

I reach for this when I need to repeatedly grab the "best" (smallest or largest) item out of a changing set, act on it, and put a new result back in — not just sort once and walk through, but sort *as things change*. A `heapq` keeps the smallest item always accessible in O(log n) per insert/remove, instead of re-sorting a list every time something changes.

## Huffman Coding — 2026-10-26

Learned from zero, not solved cold — walked through the concept by hand first (drawing the tree on paper for `mississippi`, checking my own tree against a second hand-built one) before writing any code, then implemented it.

**The idea:** compress text by giving frequent characters short binary codes and rare characters longer ones (same idea as Morse code — `E` is one dot, `Q` is four symbols). Built greedily: repeatedly take the two lowest-frequency nodes, merge them into a parent node (sum of their counts), and push the merged node back in. Do this until one node (the root) is left. Reading left=0/right=1 from root to each leaf gives that character's code.

```python
from collections import Counter
import heapq

text = "mississippi"
freq = Counter(text)

heap = [[count, char] for char, count in freq.items()]
heapq.heapify(heap)

while len(heap) > 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    new_node = [first[0] + second[0], first, second]
    heapq.heappush(heap, new_node)

def get_codes(node, path="", codes={}):
    if len(node) == 2:
        char = node[1]
        codes[char] = path
        return codes

    count, left, right = node
    get_codes(left, path + "0", codes)
    get_codes(right, path + "1", codes)
    return codes

root = heap[0]
codes = get_codes(root)
print(codes)
```

Output: `{'s': '0', 'm': '100', 'p': '101', 'i': '11'}`

Checked it against my hand-drawn tree by multiplying each code's length by its character's frequency: `s`(1×4) + `i`(2×4) + `m`(3×1) + `p`(3×2) = 4 + 8 + 3 + 6 = 21 bits total — matched my hand-drawn tree exactly, even though the two trees put `i`/`s`/`m`/`p` in different spots. That's expected: `i` and `s` are tied at frequency 4, so either one can be merged first, and the total compressed size comes out the same either way — only which specific character gets which exact code changes.


## Two things I had to untangle to actually get this

**Heap order vs. tree shape are not the same thing.** The heap always keeps the *smallest* value easiest to pop — that's about processing order. But in the final tree, a merged node (always *larger* than the two it came from) ends up *closer to the root* (shallower), while the original small leaves end up *deeper*. Smaller in the heap's pop-order ≠ deeper in the tree; they're two separate structures doing two separate jobs.

**Step count vs. bit value.** The number of steps from root to a leaf equals the code's length in bits — but the *value* of each bit (0 or 1) comes from the direction of that specific step (left or right), not from which step number it is. A 3-step path isn't automatically `"123"` or anything tied to the step numbers; it's three separate left/right choices, each contributing its own 0 or 1.

## One-line interview answer

> "Huffman coding is a greedy algorithm: repeatedly merge the two lowest-frequency nodes into a parent until one tree remains, then read 0/1 down each root-to-leaf path as that symbol's code. It's provably optimal for prefix-free binary codes, and ties in frequency don't change the total compressed size — only which exact bit pattern a tied symbol gets."
