'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):

        # Find location of the new_interval start
        # Find location of the new_interval end
        # Merge these two ends by taking the start of the first location, and end of the second
        # Remove redundant intervals

        # Approach:
        # Iterate through the list, and check if the start and end are within the list interval
        #   If the start is within the interval, save the start of this interval
        #   If the end is within the interval, save the end of this interval
        #   Delete intervals that lie within both

        # Edge cases:
        # Interval start is not within a range
        # Interval end is not within a range
        # Address by saving index when this is the case

        # start = new_interval.start
        # end = new_interval.end
        # goal_interval = Interval()
        # goal_start_set = False
        # remove_start_index = -1
        # remove_end_index = -1
        #
        # for i, interval in enumerate(intervals):
        #
        #     # Interval begins before selected interval
        #     if start < interval.start and not goal_start_set:
        #         goal_interval.start = start
        #         remove_start_index = i
        #         goal_start_set = True
        #
        #     # Interval begins within selected interval
        #     if interval.start <= start <= interval.end:
        #         goal_interval.start = interval.start
        #         remove_start_index = i
        #         goal_start_set = True
        #
        #     # Interval ends within selected interval
        #     if interval.start <= end <= interval.end:
        #         goal_interval.end = interval.end
        #         remove_end_index = i
        #
        #     # Interval ends after selected interval
        #     if interval.end < end:
        #         goal_interval.end = end
        #         remove_end_index = i
        #
        # del intervals[remove_start_index:remove_end_index+1]
        # intervals.insert(remove_start_index, goal_interval)
        # return intervals

        # Attempt #2:
        # Set booleans to indicate different cases, then address
        # Types:
        #   start before
        #       end before same
        #       end within same
        #       end before another
        #       end within another
        #       end after all
        #   start within
        #       end within same
        #       end before another
        #       end within another
        #       end after all
        #   start after all
        #       end after all
        #

        start = min(new_interval.start, new_interval.end)
        end = max(new_interval.start, new_interval.end)

        start_set = False
        end_set = False

        remove_first = 0
        remove_last = 0

        for i, interval in enumerate(intervals):

            # Start is before the current interval
            if start < interval.start and not start_set:
                start_set = True
                remove_first = i
                # End is also before current interval
                if end < interval.start:
                    # Do not remove any intervals
                    remove_last = i - 1
                    end_set = True
                    break
                    # End is within current interval
                elif interval.start <= end <= interval.end:
                    # Remove this interval
                    remove_last = i
                    end = interval.end
                    end_set = True
                    break
            # Start is within the current interval
            if interval.start <= start <= interval.end:
                start = interval.start
                start_set = True
                remove_first = i
                # End is also within current interval
                if interval.start <= end <= interval.end:
                    end = interval.end
                    # Remove this interval
                    remove_last = i
                    end_set = True
                    break
            # End is within another interval
            if interval.start <= end <= interval.end:
                end = interval.end
                # Remove this interval
                remove_last = i
                end_set = True
                break
            # End is before the current interval
            if end < interval.start:
                # Do not remove this interval
                remove_last = i - 1
                end_set = True
                break

        # End is after all elements
        if not end_set:
            remove_last = len(intervals)
            # Start is also after all elements
            if not start_set:
                remove_first = len(intervals)

        del intervals[remove_first : remove_last + 1]
        intervals.insert(remove_first, Interval(start, end))

        return intervals



interval_list_0 = [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)]
interval_list_1 = [Interval(1, 3), Interval(6, 9)]

soln = Solution()
# ret = soln.insert(interval_list_0, Interval(4, 9))
ret = soln.insert(interval_list_1, Interval(10, 15))

for interval in ret:
    print interval.start, interval.end
