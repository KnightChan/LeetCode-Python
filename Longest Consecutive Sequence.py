class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        ''' Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity. '''
        down = {}
        up = {}
        prenum = set()
        for x in num:
            if x in prenum:
                continue
            flag = 0
            if x + 1 in down:
                r = down.pop(x + 1)
                down[x] = r
                up[r] = x
                if x in up:
                    l = up.pop(x)
                    r = down.pop(x)
                    up[r] = l
                    down[l] = r
                flag += 1
            if x - 1 in up:
                l = up.pop(x - 1)
                up[x] = l
                down[l] = x
                if x in down:
                    l = up.pop(x)
                    r = down.pop(x)
                    up[r] = l
                    down[l] = r
                flag += 1
            if flag == 0:
                down[x] = x
                up[x] = x
            prenum.add(x)
        max_con = 0
        for l in up:
            t = l - up[l] + 1
            max_con = max(max_con, t)
        #print(up)
        #print(down)
        return max_con

num1 = [100, 1, 2, 200, 4, 3, 7, 5, 6]
num2 = [-7, -1, 3, -9, -4, 7, -3, 2, 4, 9, 4, -9, 8, -7, 5, -1, -7]
num0 = [3, 4, 4, 5]
num = num2
print(Solution.longestConsecutive(Solution(), num))
