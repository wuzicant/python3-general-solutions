import sys
import heapq
import random
sys.path.append(r'E:\python3-general-solutions\builtin_lab')


class MinHeap(object):
    pass


class MaxHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = [None] * maxsize
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)  # heapify

    def _siftup(self, ndx):
        if ndx > 0:
            parent = int((ndx - 1) / 2)
            if self._elements[ndx] > self._elements[parent]:    # if ndx is gt parent, swap and sift up again
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)    # recursive

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]    # save the root
        self._count -= 1
        self._elements[0] = self._elements[self._count]    # take the most bot_right ele as root and sift_down
        self._siftdown(0)    # heapify
        return value

    def _siftdown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        # determine which node contains the larger value
        largest = ndx
        if (left < self._count and     # has left
                self._elements[left] >= self._elements[largest] and
                self._elements[left] >= self._elements[right]):  # find the largest (not necessary)
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)

# a little bit tdd
def test_maxheap():
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    for i in reversed(range(n)):
        ext_v = h.extract()
        print(ext_v)
        assert i == ext_v

# a little bit tdd
def test_maxheap2():
    h = []
    l = [x for x in range(1, 11)]
    random.shuffle(l)
    for i in l:
        heapq.heappush(h, i)  # minheap
    print(h)
    while len(h):
        print(heapq.heappop(h))

# return list in DESC order
def top_k_element(l, k) -> list:
    pass

#TDD
def test_top_k_element(l, k):
    l1 = top_k_element(l, k)
    l2 = l.sort()
    l2 = l2[0:k]
    assert l1 == l2


if __name__ == '__main__':
    test_maxheap()

    #print_all([1,2,3])
    #test_maxheap()