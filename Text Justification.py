class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        '''
         Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.
Corner Cases:

    A line other than the last line might contain only one word. What should you do in this case?
    In this case, that line should be left-justified.
        '''
        def processLine(thisLineWords, thisLineWordLen, ans, lastLine = False):
            if lastLine:
                postSpaces = "".join([' '] * (L - thisLineWordLen - len(thisLineWords) + 1))
                ans.append(" ".join(thisLineWords) + postSpaces)
                return
            if len(thisLineWords) == 1:
                postSpaces = "".join([' '] * (L - thisLineWordLen))
                ans.append(thisLineWords[0] + postSpaces)
            elif len(thisLineWords) > 1:
                baseSpacesLen = (L - thisLineWordLen) // (len(thisLineWords) - 1)
                remainSpaces = (L - thisLineWordLen) % (len(thisLineWords) - 1)
                baseSpaces = "".join([" "] * baseSpacesLen)
                thisLine = thisLineWords[0]
                for i in range(1, len(thisLineWords)):
                    if remainSpaces > 0:
                        remainSpaces -= 1
                        thisLine += baseSpaces + " " + thisLineWords[i]
                    else:
                        thisLine += baseSpaces + thisLineWords[i]
                ans.append(thisLine)
        ans = []
        thisLineWords = []
        thisLineWordLen = 0
        for word in words:
            if len(word) + thisLineWordLen + len(thisLineWords) <= L:
                thisLineWordLen += len(word)
                thisLineWords.append(word)
            else:
                processLine(thisLineWords, thisLineWordLen, ans)
                thisLineWordLen = len(word)
                thisLineWords = [word]
        processLine(thisLineWords, thisLineWordLen, ans, True)
        return ans

s1 = [16, ["This", "is", "an", "example", "of", "text", "justification."]]
s2 = [12, ["What","must","be","shall","be."]]
s = s2
print(s[0], s[1])
ans = Solution.fullJustify(Solution(), s[1], s[0])
for line in ans:
    print(line)