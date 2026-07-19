from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        patterns = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                patterns[pattern].append(word)

        queue = deque()
        queue.append(beginWord)
        result = 1
        visit = set()
        visit.add(beginWord)

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result
                for j in range(len(word)):
                    neighbouring_pattern = word[:j] + '*' + word[j+1:]
                    for nei in patterns[neighbouring_pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            queue.append(nei)
            result += 1
        return 0