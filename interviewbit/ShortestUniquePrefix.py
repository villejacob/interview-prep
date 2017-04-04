'''
Find shortest unique prefix to represent each word in the list.

Example:

    Input: [zebra, dog, duck, dove]
    Output: {z, dog, du, dov}

    where we can see that
    zebra = z
    dog = dog
    duck = du
    dove = dov

Assume that no word is the prefix of another word. In other words, the 
representation is always possible.
'''

class Solution:
    # Create prefix tree as a dictionary for each letter
    def createPrefixTree(self, A):
        """
        :type A: list[str]
        :rtype: dict
        """
        prefixes = {}
        for word in A:
            if word[0] not in prefixes:
                prefixes[word[0]] = {}
            current = prefixes[word[0]]
            for c in word[1:]:
                if c not in current:
                    current[c] = {}
                current = current[c]
        return prefixes

    # Find the minumum prefix for a word, reset when node with >1 child
    def minPrefix(self, root, word, prefix):
        """
        :type root: dict
        :type word: str
        :rtype prefix: str
        """
        current = min_prefix = ""
        for c in word:
            if len(root[c]) > 1: 
                min_prefix = ""
            elif not min_prefix:
                min_prefix = current + c
            current += c
            root = root[c]
        return min_prefix

    # Main function
    def prefix(self, A):
        """
        :type A: list[str]
        :rtype: list[str]
        """
        root = self.createPrefixTree(A)        
        prefixes = []
        for word in A:
            prefixes.append(self.minPrefix(root, word, ""))
        return prefixes


print Solution().prefix(["bearcat", "bert"])
