class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        '''
        Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. 
        '''
        s = s.strip()
        if len(s) == 0:
            return False
        if s[0] in set(['+', '-']):
            s = s[1:]
        eposs = [pos for pos in range(len(s)) if s[pos] == 'e' or s[pos] == 'E']
        if len(eposs) > 1:
            return False
        epos = len(s)
        if len(eposs) == 1:
            epos = eposs[0]
        dotposs = [pos for pos in range(epos) if s[pos] == '.']
        if len(dotposs) > 1:
            return False
        dotpos = epos
        if len(dotposs) == 1:
            dotpos = dotposs[0]
        if epos == len(s) - 1 or epos == 0:
            return False
        first = s
        if epos != len(s):
            first = s[:epos]
            second = s[epos + 1:]
            if second[0] == '+' or second[0] == '-':
                second = second[1:]
            if not second.isdigit():
                return False
        if dotpos != epos:
            firstone = first[:dotpos]
            firsttwo = first[dotpos + 1:]
            if not ((firstone.isdigit() or firstone == '')
                    and (firsttwo.isdigit() or firsttwo == '')):
                return False
            if firstone == '' and firsttwo == '':
                return False
        else:
            if not (first == '' or first.isdigit()):
                return False
        return True

s0 = '.e10'
s1 = "-1.e10"
s2 = "0"
s3 = " 0.1 "
s4 = "abc"
s5 = "1 a"
s6 = "2e10"
s = s0
print(s)
print(Solution.isNumber(Solution(), s))
