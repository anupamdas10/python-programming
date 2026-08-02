class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        indices=0
        result=[]
        total=0
        brackets=[""]*(2*n)
        def backtrack(indices,brackets,total,result):
            if indices>=len(brackets):
                if total ==0:
                    result.append("".join(brackets))
                return result
            if total>len(brackets)//2:
                return 
            if total <0:
                return
            brackets[indices]="("
            backtrack(indices + 1, brackets, total + 1, result)
            brackets[indices]=")"
            backtrack(indices + 1, brackets, total - 1, result)

        backtrack(0,brackets,0,result)
        return result

y=Solution()
r=y.generateParenthesis(6)
print(r)