#!/usr/bin/env python3

"""
https://leetcode.com/problems/simplify-path

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory, so it can be ignored in a simplified path. Additionally, a double period ("..") moves up a directory, so it cancels out whatever the last directory was. For more information, look here: https://en.wikipedia.org/wiki/Path_(computing)#Unix_style

Corner Cases:
- Did you consider the case where path = "/../"?
- In this case, you should return "/".
- Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
- In this case, you should ignore redundant slashes and return "/home/foo".


- Runs in O(n) time.
- Uses O(n) space.

- Felt too simple to be a Medium - maybe it's harder without the Python built-ins.
- The examples seemed potentially confusing at first, but once the possible cases have been identified, it's quite straightforward.
- Good idea to have a basic implementation working before tackling the edge cases.
"""


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        tokens = path.split('/')
        result = []

        for t in tokens:
            if t == '' or t == '.':
                # Stay put.
                continue
            elif t == '..':
                # Go back.
                if len(result) > 0:
                    result.pop()
            else:
                # We have a filename.
                result.append(t)

        # Construct result string.
        return '/' + '/'.join(result)

    def test(self):
        assert self.simplifyPath('/home/') == '/home'
        assert self.simplifyPath('/a/./b/../../c/') == '/c'
        assert self.simplifyPath('/a/../../b/../c//.//') == '/c'
        assert self.simplifyPath('/a//b////c/d//././/..') == '/a/b/c'

        print('All tests passed!')


sol = Solution()
sol.test()
