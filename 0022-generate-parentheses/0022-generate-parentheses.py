class Solution(object):
    def generateParenthesis(self, n):
        c=[]
        def stack(empty,open,close):
           if len(empty)==2*n:
            c.append(empty)
            return 
           if open<n:
            stack(empty+"(",open+1,close)
           if close<open:
            stack(empty+")",open,close+1)  
           
        stack("",0,0)
        return c
             

             
               
           
              