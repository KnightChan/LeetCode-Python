class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        ''' There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique. '''
        n = len(gas)
        start = 0
        cur = 0
        curlen = 0
        startcount = 1
        remain = 0
        while curlen < n and startcount <= n:
            remain += gas[cur] - cost[cur]
            while remain < 0:
                remain -= gas[start] - cost[start]
                start = (start + 1) % n
                startcount += 1
                curlen -= 1
            cur = (cur + 1) % n
            curlen += 1
        if cur == start and startcount <= n:
            return start
        else:
            return -1

A = [1, 2, 3, 3, 2, 1, 4, 5, 4]
A1 = [1, 2, 3]
A2 = [2, 1, 4]
so = Solution()
res = so.canCompleteCircuit(A1, A2)
print(res)