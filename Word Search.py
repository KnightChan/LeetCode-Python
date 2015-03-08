class Solution:
    dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        '''
         Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
        '''
        def checkValid(flag, x, y, m, n):
            return 0 <= x < m and 0 <= y < n and flag[x][y]
        def dfs(word, board, flag, x, y, m, n):
            if word == '':
                return True
            if word[0] != board[x][y]:
                return False
            if len(word) == 1:
                return True
            flag[x][y] = False
            for i in range(len(self.dirs)):
                newp = [x + self.dirs[i][0], y + self.dirs[i][1]]
                if checkValid(flag, newp[0], newp[1], m, n):
                    if dfs(word[1:], board, flag, newp[0], newp[1], m, n):
                        return True
            flag[x][y] = True
            return False

        m = len(board)
        if m == 0:
            return word == ''
        n = len(board[0])
        flag = [[True] * n for row in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(word, board, flag, i, j, m, n):
                    return True
        return False

a1 = ['ABCCED', [
  ["A", "B", "C", "E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]]
a2 = ['SEE', [
  ["A", "B", "C", "E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]]
a3 = ['ABCB', [
  ["A", "B", "C", "E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]]
a4s = [["gbgptkbnfcxdxdohfcwhyopseabpqsawuinpvqectbfsgtznyxuwolrslukemkagvqxsgcuzfarovsbtqysgjlyvf","izrvbaqrziybczjetxclaxdyrjickfhsebnhdfbcpbeuapatochocmntwvygahagiqplxqonrujuljpzoynqlclhz","lpbtrhbhzpfpfujbdfmowncvaugfipetegmxpqfqhmgmgrplybbuoepqavvikceqksozivqrhyfprucpvdlljbeky","zujdybnrppbkftrfyiyvkpsoaexbkjalelpemcxerboyuifusdrdskttqswacylilamyfmeynsxjcefxixaahtvxn","uxpskxelmesyiqncnwhsbecygefbaeowdeoodubpytpijcnzyutcavagbihdovzszoifklujgmtpogqpajragtiib","plsllkmburlhownaqcqwvhzgabnukxxzipmvbzyvskeiirkywbxrkyxlzmhljeluuzrvaqttcxbkrmjnpiebgdmfq","trzyetufnrgdmbfmepdsaqhiujozxwptnprtknyxegcthhfmziezyoiuzwtwslphcicovdocjqxracfzkjykxigwf","bvzmkjovnfsqtucjrvjvaihjjtjrzfydcapnjgkwlcpezrpsmboojvxupimqqktsklhvtrugulmteblsebgozdkom","wgcjcwvnetivnopackefywkzcayhkovjxzszwpociwxxmpxobdtzzdbddblqsizpkrogieitahqmwqcytvzvbayge","lwwuvleobmzfwsffkteaxewudrvgpekdcgxatdqurpzpjguubyuycsuijsobwyeygbazgrtxiuoscimfhiflbztkr","jlpjrqpsqoajjzsfnkjywqhexsfxosqxfihxyyronsyytsghcrhyiocfgkewcvwjddgdbytqstrllxunqblypqeyc","kwgfspkvwnzuhrmckzojubaxpypfephplpweejbawcwfukkgkyqgzqdoqsvvhemvtizytaasfxzbjjhthxbhnfxgz","vdjzpevzfvthvlmukneuvzdubkkikqhhtsiiydjdycnwpzscpwymwbgzoqhygqhzlpjjtvptzcrpdktsgreeslfgb","mgkfnlqfxzysqtrsliyvbqdsvknipvleevjtjzygawytsrndalabcfwzpljfgulmsugbvejxdhqvaeaapaerfcsxn","bevypiqlqtgucdzluwlawopysjgwddlfjgfyqxjgqpduuehqbuqxiiycreaujlbsugskdbtvsyrocafdvxdffdkwh","ktsyuksdeeifzgzxxncauhvsmcxpowybpqzjcrogvxnvdoucewcygzsscqisogtdzsobjdkhcxcfmwjsvmqbllvpd","dirmdulwkohnyorwswkrgcmuupffkxiqhzckvpigdqvegnczlmqtqepktvsductbexlzowhumfyuuavfonberqqmn","kqhnlktlwuzscvgjtcdtykjllnfegrtqjdfvnyijtjdxflgyojuotdzhtgnbygrhjzezxoksyopdbvbrgxfcdhjwn","yxlgqvsrbrpqbhorzrtuukdsqfxzqtmosawkvocyhtojcccbvvysibmaijzyelmynkiizmjghxrkcunzrnrzqdbym","awqokobvzmwnvevswhwsuwjknlatozfpvyfgmgbnszbpdyibfgtbcflssolgnqxiqcqdjtsdsvtwtdxajtcoapisd","taslybcathlnbpfxkdqpdrywvowmwqsrqkdonhrjocwptdmfjfumyvkvlihiybzqoehdlambcityohfxmalmxvhid","rqdssviwcmkcylhhghxomuaohplcwuhnmmighqfkepodcvmjejxrfzfmotqnpxcblkisdnehetmgqyrvhomoqtceo","srdruhcgpxlebvkuhqlgkgpyugopivgdojuiqzrhwcnxxxufqfnancyjkpytmewaqsjitcqpefpedjjtqytdctmnk","mgwtezlwktqmlhqrwuwhfpxfkcifqxqffoyjnlhzezlshejfahpgwonirxnhufozwmilzslgryyacjidqxlolywew","loqtcsrrcequpwoouoqdwvvvgjhfhndtbvoenhvqllmdiarerjiphdlnpuuwhxrltfpimkaavndfpukgfuymzlcof","wlouczpiqxwaywylzdcvpldjjrjutxbqirmltbvjytkwqkjrpmpfzsqilzefzhxjylwrmtdmnnjfzuyointhhmrtl","vamczwdkuuyoxkbmvgnqecauxibjzwxxyjbzhejcbjqaurnpzchfeizcsdntbkqcusbdynfzwvaqopiprpvwzwarb","nnfadhuxizwxfxwcxotowigofeneehftumtztpzepxbwuxyuorikcoahsolyxtutfpsbftfwqislishwmpioejxyz","lzygvrnklopfvnxgfkoarmmhwcnfbngmoeujviujwlouzlagwqgncuwawjgyzmmnrhxoptxnenhfzhoxxumbplcnu","klvyyjpfggwbdjhtrnuabryxfboqdcnpniontfublqcrckktzetcxtzevovaqksfugvolppziusmeeffiahhwilty","ivqunwpttfhiwisqaewelbooixmtifrtainogejzjsjgaeycivgwwwmhtyaeftxfbkvjphiazuiayhcicleajqhdq","jhvdedgqaqhhyijsqlszpbbafemylpqxymaergurwcbxmkrexkemlhpslbszsjwqxyuogqhfukcguvltfpgsyxnky","hlqqhiphefnupspzwvwsipzxvuwshisotkhcsylweytvtiurfqjoglndhlyotqeodnsvoduuenpxxjocaasgngjur","jknaqddewasbwofjdcimtlmtfuglgcfpmurcxwivxcxtqefthnicawvgrdtzfyotsivseendimxzreuarccuzzcse","vrjwheopziwfyzokypdcjdwohsniuhmpyxlhbczdkvkiwyvvpyzbevpnnewjlkzlimsjorobozllzgiphhqnfhcul","aewlfhtrbegvvhjuswtbekkocxtjbpwctsnybiqdmyahhjdbixcojmcmlvxnlupgmefqmxvavvkegnfomidwwfikd","hzqbqwoudggcbizwsdcijtutwsrdcbgkaylsxbmchufidegxkjftccoaufdzhmjjkuchyqkflrqqxwphhxclzqnvy","rufffqpcuzanjhacxqzwhjfelrfeebcxxjcfzuhwtjjeqjgobhmiqrpckuirxkoxttcunlsiudokmuapdoaugpyql","ghlsyiltmhixasrdgdscghfujzcaztmhcxzchkxtufquxjzdorfubnrkotnoobvtaxvhhtcdauxadxdtqloryhema","tcpuaiuxfdgafkdbjdeggxztnqtuwgxpkmlkwhhdkogryjsjmyquypqlhjierfvcthmrowwbkcuknntbnlylcozmz","jqrontjuhaldwmpbiboxxqliqynexzfgrwwerfbbhogecwhkxviwntffrulrtrzknwqhdrilhorjmyumveilzpqsj","cjevlqkjhrmabzissteqpsotdbssrlevwkqhbbqiufkwgsqzowrdpfxsipmaasxxdqgerxoneylktbjhydkpkhjtz","vvbosatihxbgnpklawgeinclatvjcoizjknemimthqzuflghiolqcpbciynmnwmyibcukpqrhpmmduvlijdmagqje","exrcjqklugxjwosocgtycejnjvnpmytswnuffgszmpllgdbikuhmaqbjnoybnttjgnqltjniyyvgbwpnsybsqcddr","dhewanfqdsjoftpdovhmmugkwacydipipvhpimfoerekmtpdrwrdtyqpyspechmrctjnfqdmjhywdnbumsxhqnypi","ntkwhezbnoidrunyulbkmvyevfxkfmsshfrqjsrwgcbxyqxtbbdpybutitenfyhodygoqamwcovagvtiwyzubtqjo","wytugjagsoxsdvurtwxoshkqhgucydruemrkytqqhpkmnedgcdwumintohypmrjqdcadvtvfkfrxjvfmabimjviac","gppxafcdigadbfnjxnsuugwwrihmqjryagxdnaixiicloqunfphzxdxonfdgquerccurecpomrzajunolwqibnzps","cvlybcafytjckxoezrnveegdwqejpvetqprurtzrpltzijdjatehzkkvbqesmimezfasbajqlepvqvfqojzpujkxc","qpqbdwalxtmxeeklvfbqmrgwrvschrgyiwbmtbzqwlpdpbomipdvijtbhngoemoojpcetbwpolufoiswzvrigkjnz","pefesuniwtdapuocpuqxmmxjghpssfskjxodtdnswqsnlgpachzqvyzbhruawmkhlakfdyxzorobzfdcmdujdwlln","fnltzsezelcckdtbrudwahkdbtixgvmnkxgjrniwakalpvogstesaqxemfdsdqgnnoxhbffcsfphdfqvzwnznkdzr","htuzzioohvrmavgikqlqgipcvqrfwsyfmtendsdkqxysshcdxpvdxmhsezzatyhhtlvwgaiyxiqspvvmksrigzcka","clvcudxgavoadmalesbzppmhhupiyzicmfehidpiydjbrlpxdqzshlbohqwfpgicmolwsafqdqswbhtezuyifzxmr","vuiecmsqxoixtbcjvymeuqdoqnwrkkiiermgfezdsjaokfxffkjzcoqtcokoyvwdokltqkwjuzxggwoliznlofgst","sirpfudrgxisvtowqvcoloxkdkyiqsbkbsaipdzxcjpyceuubzjmngwqqxairbusvuakachcnzcqdzkgytunbsftp","fbjgwbdseosixxvwzlbyyhyrdlvwsonxswfqyjkezdowajtbxuaveaoholdgatgupnmpwwvxzjubtpdslfnrfdztp"], "crzilpvxgu"]

a4 = [a4s[1], []]
for i in range(len(a4s[0])):
    a4[1].append([])
    for c in a4s[0][i]:
        a4[1][i].append(c)
al = [a1, a2, a3, a4]
for k in range(len(al)):
    a = al[k]
    print(a[0], len(a[1]), len(a[1][0]))
    #for i in range(len(a[1])):
    #    print(a[1][i])
    print(Solution.exist(Solution(), a[1], a[0]))