class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        ''' Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome. '''
        dictset = set()
        for i in range(ord('0'), ord('9') + 1):
            dictset.add(chr(i))
        for i in range(ord('a'), ord('z') + 1):
            dictset.add(chr(i))
        s1 = s.lower()
        l = 0
        r = len(s1) - 1
        while l < r:
            while l < r and s1[l] not in dictset:
                l += 1
            while l < r and s1[r] not in dictset:
                r -= 1
            if l < r and s1[l] != s1[r]:
                return False
            l += 1
            r -= 1
        return True


a = 'aa'
so = Solution()
res = so.isPalindrome(a)
print(res)
