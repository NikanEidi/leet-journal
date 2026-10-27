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