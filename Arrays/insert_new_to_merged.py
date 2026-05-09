class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(intervals, newInterval):
        result = []

        ns, ne = newInterval.start, newInterval.end

        for interval in intervals:
            s, e = interval.start, interval.end

            # Case 1: current interval completely before newInterval
            if e < ns:
                result.append(interval)

            # Case 2: current interval completely after newInterval
            elif s > ne:
                result.append(Interval(ns, ne))
                ns, ne = s, e   # new interval becomes current
            else:
                # Case 3: overlap
                ns = min(ns, s)
                ne = max(ne, e)

        # add the last merged interval
        result.append(Interval(ns, ne))

        return result
