class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        return len(set(arr))==len(set(freq.values()))
    
y=Solution()
r=y.uniqueOccurrences([1,2])    
print(r)