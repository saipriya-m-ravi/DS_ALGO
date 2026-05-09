from collections import defaultdict


class FreqStack:
    def __init__(self):
        # freq[x] = current frequency of element x
        self.freq = defaultdict(int)

        # group[f] = stack (list) of elements with frequency f
        self.group = defaultdict(list)

        # maximum frequency present in the stack
        self.maxFreq = 0

    def push(self, x: int) -> int:
        # increase frequency
        self.freq[x] += 1
        f = self.freq[x]

        # update max frequency
        if f > self.maxFreq:
            self.maxFreq = f

        # push into corresponding frequency stack
        self.group[f].append(x)

        return -1

    def pop(self) -> int:
        # pop from the stack with maximum frequency
        x = self.group[self.maxFreq].pop()

        # decrease frequency
        self.freq[x] -= 1

        # if no elements left with this frequency
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1

        return x


class Solution:
    def solve(A):
        fs = FreqStack()
        result = []

        for op, val in A:
            if op == 1:
                result.append(fs.push(val))
            else:
                result.append(fs.pop())

        return result
