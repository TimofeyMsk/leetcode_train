# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
from typing import List
import random


class Master:
    # secret_word = 'vftnkr'
    # secret_word = "hbaczn"
    secret_word = "azzzzz"

    def guess(self, word: str) -> int:
        ans = 0
        for (i, c) in enumerate(word):
            ans += 1 if c == Master.secret_word[i] else 0
        print("Guess: ", word, ' with dist = ', 6 - ans)
        if ans == 6:
            print("YOU GUESSED!")
        return ans


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def hamming_distance(w1: str, w2: str) -> int:
            return sum(1 for k in range(6) if w1[k] != w2[k])

        current_guess = wordlist[0]
        curr_distance = 6 - Master.guess(master, current_guess)
        # guess_no = 2
        while curr_distance != 0:
            #  delete all words except ones have distance not equal curr_distance
            wordlist = [w for w in wordlist if hamming_distance(current_guess, w) == curr_distance]
            # print('current lenght wordlist: ', len(wordlist))
            # print('-----------------------------------------')
            # current_guess = wordlist.pop(random.randint(0, len(wordlist) - 1))
            current_guess = wordlist.pop()
            # print('guess No: ', guess_no)
            curr_distance = 6 - Master.guess(master, current_guess)
            # guess_no += 1



# lst = ["mjpsce","giwiyk","slbnia","pullbr","ezvczd","dwkrmt","qgzebh","wvhhlm","kqbmny","zpvrkz","pdwxvy","gilywa","gmrrdc","vvqvla","rmjirt","qmvykq","mhbmuq","unplzn","qkcied","eignxg","fbfgng","xpizga","twubzr","nnfaxr","skknhe","twautl","nglrst","mibyks","qrbmpx","ukgjkq","mhxxfb","deggal","bwpvsp","uirtak","tqkzfk","hfzawa","jahjgn","mteyut","jzbqbv","ttddtf","auuwgn","untihn","gbhnog","zowaol","feitjl","omtiur","kwdsgx","tggcqq","qachdn","dixtat","hcsvbw","chduyy","gpdtft","bjxzky","uvvvko","jzcpiv","gtyjau","unsmok","vfcmhc","hvxnut","orlwku","ejllrv","jbrskt","xnxxdi","rfreiv","njbvwj","pkydxy","jksiwj","iaembk","pyqdip","exkykx","uxgecc","khzqgy","dehkbu","ahplng","jomiik","nmcsfe","bclcbp","xfiefi","soiwde","tcjkjp","wervlz","dcthgv","hwwghe","hdlkll","dpzoxb","mpiviy","cprcwo","molttv","dwjtdp","qiilsr","dbnaxs","dbozaw","webcyp","vftnkr","iurlzf","giqcfc","pcghoi","zupyzn","xckegy"]
# lst = ["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"]
lst = ["abcdef","acdefg","adefgh","aefghi","afghij","aghijk","ahijkl","aijklm","ajklmn","aklmno","almnoz","anopqr","azzzzz"]
Solution.findSecretWord(None, lst, Master())