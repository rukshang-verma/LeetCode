class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
                
        if len(s) != len(t):
            return False
        
        x = sorted(s)
        y = sorted(t)
        
        for i in range(0, len(x)):
            if x[i] != y[i]:
                return False
        return True
            
        '''
        for x in s:
            if x in t:
                return True
        return False
        '''