'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
    Did you consider the case where path = "/../"?
    In this case, you should return "/".
    Another corner case is the path might contain multiple slashes '/' together,
    such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".
'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ret, pwd, cwd = [], [], []
        i = 0

        # Parse list for elements separated by /
        while i < len(path):
            while i < len(path) and path[i] == '/':
                i += 1
            while i < len(path) and path[i] != '/':
                cwd.append(path[i])
                i += 1
            if cwd:
                pwd.append(''.join(cwd))
                cwd = []

        # Push to stack if dir, pop if '..'
        for dir in pwd:
            if dir == '..':
                if ret:
                    ret.pop()
            elif dir != '.':
                ret.append(dir)

        # Join elements with / and insert / at front
        return '/' + '/'.join(ret)
        


print Solution().simplifyPath("/a/./b/../../c/")
print Solution().simplifyPath("/a////./b//../c/")
print Solution().simplifyPath("/")
print Solution().simplifyPath("/../")
print Solution().simplifyPath("/...")
