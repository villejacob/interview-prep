'''
Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the
empty string "".

If there are multiple such windows, you are guaranteed that there will
always be only one unique minimum window in S.
'''
from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = Counter(t)
        missing = len(t)
        i = I = J = 0

        for j, c in enumerate(s, 1):

            # Subtract 1 when count of c > 0
            missing -= need[c] > 0      

            # Always subtract from remaining when encountered
            need[c] -= 1

            if not missing:

                # Move start of window i when encountered more than required
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1

                # Update window when smaller than previous
                if not J or j - i <= J - I:
                    I, J = i, j

        return s[I:J]

print Solution().minWindow("ADOBECODEBANC", "ABC")
print Solution().minWindow("ADBEABBCA", "AABBC")

