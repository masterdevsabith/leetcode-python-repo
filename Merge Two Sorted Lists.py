# url : https://leetcode.com/problems/merge-two-sorted-lists/description/


# QUESTION#

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing
#  together the nodes of the first two lists.

# Return the head of the merged linked list.


# SOLUTION#

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


list = Solution()
list1 = list.mergeTwoLists([1, 2, 4], [1, 3, 4])
list2 = list.mergeTwoLists([], [])
list3 = list.mergeTwoLists([], [0])
