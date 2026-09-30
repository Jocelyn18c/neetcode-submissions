class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_counts ={}
            t_counts ={}
            for i in range(len(s)):
                if s[i] in s_counts:
                    s_counts[s[i]] += 1
                else:
                    s_counts[s[i]] = 1
                
                if t[i] in t_counts:
                    t_counts[t[i]] += 1
                else:
                    t_counts[t[i]] = 1
            if s_counts == t_counts:
                return True
        return False

        