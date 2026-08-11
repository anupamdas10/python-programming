class Solution:
    def decodeString(self, s: str) -> str:
        num_stack=[]
        str_stack=[]
        current_num=0
        current_str=""

        for  ch in s:
            if ch.isdigit():
              current_num=current_num*10+int(ch)
            elif ch=="[":
                num_stack.append(current_num)
                str_stack.append(current_str)
                current_num=0
                current_str=""  
            elif ch=="]":
                num=num_stack.pop()
                previous_str=str_stack.pop()
                current_str=previous_str +  current_str * num
            else:
                current_str+=ch
        return current_str
y=Solution()
r=y.decodeString("3[a2[c]]")
print(r)                



