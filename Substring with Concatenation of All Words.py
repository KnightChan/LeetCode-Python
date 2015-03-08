class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        return self.findSubstring_usingDic(S, L)

    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    # using dictionary 1700ms, O(len(S) * len(L))
    def findSubstring_usingDic(self, S, L):
        '''
         You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter). 
        '''
        n = len(L)
        if n == 0:
            return []
        word_len = len(L[0])
        allWordsDic = {}
        for s in L:
            if s not in allWordsDic:
                allWordsDic[s] = 1
            else:
                allWordsDic[s] += 1
        res = []
        for i in range(len(S) - n * word_len + 1):
            t_dic = allWordsDic.copy()
            flag = True
            for j in range(i, i + n * word_len, word_len):
                if S[j:j+word_len] not in t_dic:
                    flag = False
                    break
                t_dic[S[j:j+word_len]] -= 1
                if t_dic[S[j:j+word_len]] == 0:
                    del t_dic[S[j:j+word_len]]
            if flag:
                res.append(i)
        return res

    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    # using dictionary 1700ms, O(len(S)), but can not pass the OJ because of the false positive
    def findSubstring_usingHash(self, S, L):
        '''
         You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
        '''
        n = len(L)
        if n == 0:
            return []
        word_len = len(L[0])
        hashsum = sum([hash(s) for s in L])
        res = []
        hs = [0] * (len(S) + 1)
        for i in range(word_len, len(S) + 1):
            hs[i] += hs[i - word_len] + hash(S[i - word_len:i])
            print(S[i - word_len:i], hash(S[i - word_len:i]))
        return [i - n * word_len for i in range(n * word_len, len(S) + 1) \
                if hs[i] - hs[i - n * word_len] == hashsum]

s2 = ['a', ['a']]
s0 = ["barfoothefoobarman", ["foo","bar"]]
s1 = ["lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]]
s3 = ["abbbbbacbc", ["bc","ac"]]
s = s3
print(s)
print(len(s[0]), len(s[1]))
print(Solution.findSubstring_usingDic(Solution(), s[0], s[1]))
print(Solution.findSubstring_usingHash(Solution(), s[0], s[1]))