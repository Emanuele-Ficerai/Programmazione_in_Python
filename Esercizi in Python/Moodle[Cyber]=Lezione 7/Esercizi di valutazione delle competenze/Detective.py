def is_subsequence(s: str, t: str) -> bool:
    if len(s) ==0:
        return True
    if s[0] not in t:
        return False
    prev=0
    for i in range(1, len (s)):
        if s[i] not in t:
            return False
        idx=t.index(s[i])
        if idx < prev:
            return False
            
        prev = idx
        
    return True