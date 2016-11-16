'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example :
[1,1,2] have the following unique permutations:

[1,1,2]
[1,2,1]
[2,1,1]
 NOTE : No 2 entries in the permutation sequence should be the same.
'''

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):

        # Generator function to determine permutation of elements
        def generate_permutations((elements)):
            # Base case when only one element
            if len(elements) == 1:
                # Return as tuple, trailing comma to indicate single element tuple
                yield (elements[0],)
            else:
                # Eliminate duplicated values
                unique_elements = set(elements)
                # Put each value at the front of the permutation of the rest of the elements
                for first_element in unique_elements:
                    remaining_elements = list(elements)
                    # Remove the current element
                    remaining_elements.remove(first_element)
                    # Find the permutation of the rest of the elements
                    for sub_permutation in generate_permutations(remaining_elements):
                        # Return the first element at the front of the permutation of the rest
                        yield (first_element,) + sub_permutation

        # Uses generator to create a returnable list
        unique_permutations = []
        for permutation in generate_permutations(A):
            unique_permutations.append(permutation)

        return unique_permutations


A1 = [1, 2, 3]
soln = Solution()
print soln.permute(A1)
