from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        queue=deque()
        queue.append((beginWord,1))
        while len(queue)!=0:
          curr_word,level=queue.popleft()
          if curr_word==endWord:
            return level
          for i in range(0,len(curr_word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch == curr_word:
                  continue 
                new_word=curr_word[:i]+ ch+ curr_word[i+1:]
                if new_word in wordset:
                    queue.append((new_word,level+1))
                    wordset.remove(new_word)
        return 0  

y=Solution()
r=y.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])
print(r)     
     