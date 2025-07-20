# url : https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/


# Question#

# Given an array of strings words, return the first palindromic string
#  in the array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward


class Solution(object):
    def firstPalindrome(self, words):
        for string in words:
            reversed_string = string[::-1]
            if reversed_string == string:
                return reversed_string
            else:
                return ""


word = Solution()
word1 = word.firstPalindrome(["abc", "car", "ada", "racecar", "cool"])
word2 = word.firstPalindrome(["notapalindrome", "racecar"])
word3 = word.firstPalindrome(["def", "ghi"])

print(f"I'st LIST : {word1}")
print(f"II'nd LIST : {word2}")
print(f"III'nd LIST : {word3}")
