class Solution:
    '''
    Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    '''
    # @return a string
    def convertToTitle(self, num):
        dic = ['Z']
        for i in range(ord('A'), ord('Z')):
            dic.append(chr(i))
        ans = []
        while num > 0:
            ans.append(dic[num % 26])
            if num % 26 == 0:
                num -= 26
            num //= 26
        return "".join(reversed(ans))