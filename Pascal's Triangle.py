# url :

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:


# SOLUTION#
class Solution(object):
    def generate(self, numRows):
        i = 1
        final_list = []
        list_to_append = []
        while i <= numRows:
            list_to_append = [i]*i
            if len(list_to_append) > 2:
                pass
            final_list.append(list_to_append)
            i += 1
        return final_list


case = Solution()
case1 = case.generate(5)
case2 = case.generate(1)

print(f"I'st CASE : {case1}")
print(f"II'nd CASE : {case2}")
