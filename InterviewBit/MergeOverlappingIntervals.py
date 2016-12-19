'''
Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):

        # Approach:
        # Go through each interval, keeping track of current start and end
        # If the interval is within this range, update the end to include the intervals end
        # Current will be updated when:
        #   end is within the interval AND start is outside
        #   start is within the interval AND end is outside
        #   start is before AND end is after

        # start = intervals[0].start
        # end = intervals[0].end
        #
        # merged = []
        #
        # for i, interval in enumerate(intervals[1:], 1):
        #
        #     if start <= interval.start and (interval.start <= end <= interval.end):
        #         end = interval.end
        #     elif (interval.start <= start <= interval.end) and end >= interval.end:
        #         start = interval.start
        #     elif start > interval.start and end < interval.end:
        #         start = interval.start
        #         end = interval.end
        #     else:
        #         merged.append(Interval(start, end))
        #         start = interval.start
        #         end = interval.end
        #
        #     # Check when current interval is the last
        #     if i == len(intervals) - 1:
        #         if intervals[-1].end != merged[-1].end:
        #             merged.append(Interval(start, end))
        #
        # return merged

        # Approach 2:
        # Initially assumed these were sorted in a certain way
        # Keep track of the initial start and end
        # If the next interval:
        #   starts within the current interval: Check where the end lies:
        #       If end is within, do nothing
        #       If end is outside, update current end to the intervals end
        #   starts outside the current interval: append the current to the solution
        #   Check if it is the last Interval

        # First sort the intervals by increasing start
        intervals.sort(key=lambda interval: interval.start)

        # Keep track of current start and end
        start = intervals[0].start
        end = intervals[0].end
        # Solution set
        merged = []

        for i, interval in enumerate(intervals):
            # If the interval starts within the current interval
            if start <= interval.start <= end:
                # And it ends after the current interval
                if interval.end > end:
                    end = interval.end
            # If the interval ends within the current interval
            elif start <= interval.end <= end:
                # If it begins before the current interval
                if interval.start < start:
                    start = interval.start
            # If the interval begins after the current
            elif end < interval.start:
                # Store the interval to the solution
                merged.append(Interval(start, end))
                # Reset start and end to the interval
                start = interval.start
                end = interval.end

            # The last interval is appended
            if i == len(intervals) - 1:
                merged.append(Interval(start, end))

        return merged


interval_list_0 = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
# Solution for interval_list_1 is [(1, 10), (11, 20)]
interval_list_1 = [Interval(1, 10), Interval(2, 9), Interval(3, 8), Interval(4, 7), Interval(5, 6), Interval(6, 6),
                   Interval(11, 20), Interval(3, 2)]
soln = Solution()
ans_list = soln.merge(interval_list_1)

print "\nsoln: "
for ans in ans_list:
    print ans.start, ans.end
