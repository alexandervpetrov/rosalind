

class BinaryMinHeap():

    def __init__(self):
        # storage of (key => value) or (object => priority)
        self.objs = {}
        # actual binary heap storage as 2^n array
        self.bheap = []
        # reverse index of keys positions in self.bheap
        self.index = {}

    @staticmethod
    def _parent(i):
        assert i > 0
        return (i - 1) // 2

    @staticmethod
    def _child_first(i):
        return 2 * i + 1

    def _value(self, i):
        return self.objs[self.bheap[i]]

    def _min_child(self, i):
        ci1 = BinaryMinHeap._child_first(i)
        n = len(self.bheap)
        if ci1 >= n:
            return None
        ci2 = ci1 + 1
        if ci2 >= n:
            return ci1
        v1 = self._value(ci1)
        v2 = self._value(ci2)
        if v2 < v1:
            return ci2
        return ci1

    def _swap(self, i, j):
        self.bheap[i], self.bheap[j] = self.bheap[j], self.bheap[i]
        self.index[self.bheap[i]] = i
        self.index[self.bheap[j]] = j

    def _bubble_up(self, i):
        while i > 0:
            pi = BinaryMinHeap._parent(i)
            if self._value(i) < self._value(pi):
                self._swap(i, pi)
                i = pi
            else:
                break

    def _sink_down(self, i):
        while True:
            ci = self._min_child(i)
            if ci is not None and self._value(ci) < self._value(i):
                self._swap(i, ci)
                i = ci
            else:
                break

    def __len__(self):
        return len(self.bheap)

    def __contains__(self, k):
        return k in self.objs

    def __getitem__(self, k):
        return self.objs[k]

    def __setitem__(self, k, v):
        if k in self:
            self.update(k, v)
        else:
            self.insert(k, v)

    def __delitem__(self, k):
        if k not in self:
            raise KeyError("Key not found: {}".format(k))
        i = self.index[k]
        self._swap(i, len(self)-1)
        del self.bheap[-1]
        del self.index[k]
        del self.objs[k]
        self._sink_down(i)
        self._bubble_up(i)

    def find_min_key(self):
        return self.bheap[0] if self.bheap else None

    def extract_min(self):
        if not self.bheap:
            return None
        k_min = self.bheap[0]
        v_min = self.objs[k_min]
        del self[k_min]
        return (k_min, v_min)

    def insert(self, k, v):
        if k in self:
            raise KeyError("Key already in heap: {}".format(k))
        self.objs[k] = v
        self.bheap.append(k)
        self.index[k] = len(self) - 1
        self._bubble_up(len(self.bheap) - 1)

    def update(self, k, v):
        if k not in self:
            raise KeyError("Key not found: {}".format(k))
        old_value = self.objs[k]
        self.objs[k] = v
        i = self.index[k]
        if v < old_value:
            self._bubble_up(i)
        elif v > old_value:
            self._sink_down(i)
