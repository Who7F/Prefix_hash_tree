class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        MOD = 1000000007
        W = len(word)
        prefixHash = [0] * (W+1)
        powers = [1]
        for i in range(W):
            powers.append((powers[i]*7)% MOD)

        for i in range(W):
            prefixHash[i+1] = (prefixHash[i] + ord(word[i]) * powers[i]) % MOD
            
        tic = 1
        for i in range(k, W+1, k):
            C = (W-i)
            currHash = (prefixHash[W] - prefixHash[i]) % MOD
            wordHash = (prefixHash[C] * (powers[i])) % MOD
            if currHash ==wordHash:
                return tic            
            tic += 1
        return tic


def main():
    if Solution().minimumTimeToInitialState('abacaba', 3) == 2:
        print('pass')
    else:
        print('fail')

    if Solution().minimumTimeToInitialState('abacab', 4) == 1:
        print('pass')
    else:
        print('fail')

    if Solution().minimumTimeToInitialState('abcbabcd', 2) == 4:
        print('pass')
    else:
        print('fail')

    if Solution().minimumTimeToInitialState('abcbabce', 2) == 4:
        print('pass')
    else:
        print('fail')

    sup = 'a'
    for i in range(200000):
        sup += 'a'

    sup += 'k'


    if Solution().minimumTimeToInitialState(sup, 1) == 200002:
        print('Speet test pass')
    else:
        print('fail')
        

if __name__== '__main__':
    main()
