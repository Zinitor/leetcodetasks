class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = {}
        
        for a in ransomNote:
            if a not in hash:
                hash[a] = 0
            hash[a] += 1
        
        for b in magazine:
            if b in hash:
                hash[b] -= 1
                if hash[b] == 0:
                    del hash[b]
                
        if hash == {}:
            return True
        else:
            return False
        
                
print(Solution.canConstruct("note", "bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
        