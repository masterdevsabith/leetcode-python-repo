# url : https://leetcode.com/problems/merge-two-sorted-lists/description/


# QUESTION#

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing
#  together the nodes of the first two lists.

# Return the head of the merged linked list.


# SOLUTION#

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        final_list = []

        for i in range(len(list1)):
            if i == 0:
                final_list.append(list1[i])
        for x in range(len(list2)):
            if x == 0:
                final_list.append(list2[x])
        return final_list


list = Solution()
list1 = list.mergeTwoLists([1, 2, 4], [1, 3, 4])
list2 = list.mergeTwoLists([], [])
list3 = list.mergeTwoLists([], [0])


print(f'result of first array : {list1}')
print(f'result of second array : {list2}')
print(f'result of third array : {list3}')
