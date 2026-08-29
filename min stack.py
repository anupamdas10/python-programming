class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.stack.append([val,val])
        else:
            mini=min(self.stack[-1][1],val) 
            self.stack.append([val,mini])   
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        if len(self.stack)==0:
            return 0
        return self.stack[-1][1]      

    