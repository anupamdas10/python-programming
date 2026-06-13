class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = set("aeiou")

        c = 0

        # Count vowels in first window
        for i in range(k):
            if s[i] in vow:
                c += 1

        max_c = c

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vow:      # new character enters
                c += 1

            if s[i-k] in vow:    # old character leaves
                c -= 1

            max_c = max(max_c, c)

        return max_c 
        
y=Solution()
r=y.maxVowels("abciiidef",3)
print(r)