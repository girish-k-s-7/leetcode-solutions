class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, level = q.popleft()

            if word == endWord:
                return level

            wordListChars = list(word)

            for i in range(len(word)):
                originalChar = wordListChars[i]

                for ch in "abcdefghijklmnopqrstuvwxyz":
                    wordListChars[i] = ch
                    newWord = "".join(wordListChars)
                    if newWord in wordSet:
                        q.append((newWord, level+1))
                        wordSet.remove(newWord)
                wordListChars[i] = originalChar
        return 0