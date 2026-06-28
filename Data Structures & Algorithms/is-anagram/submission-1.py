class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Char_count_s = {}
        Char_count_t = {}
        
        for i in range(0,len(s)):
            if s[i] in list(Char_count_s.keys()):
                Char_count_s[s[i]] += 1
            else:
                Char_count_s[s[i]] = 1

        for i in range(0,len(t)):
            if t[i] in list(Char_count_t.keys()):
                Char_count_t[t[i]] += 1
            else:
                Char_count_t[t[i]] = 1      

        return (Char_count_s == Char_count_t)
        