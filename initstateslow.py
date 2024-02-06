class Solution:
    def minimumTimeToInitialState(self, w: str, k: int) -> int:

        tic = 1
        n = len(w)
        for i in range(k, n+1, k):
            print (i, k, n+1)
            if w[i:n] == w[:n-i]:
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
        

if __name__== '__main__':
    main()
