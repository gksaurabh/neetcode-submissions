class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        result = False

        for char in s: 
            if char in s_hash:
                s_hash[char] += 1
            else:
                s_hash[char] = 1
            

        for char in t:
            if char in t_hash:
                t_hash[char] += 1
            else:
                t_hash[char] = 1
            

       

        s_hash = dict(sorted(s_hash.items()))
        t_hash = dict(sorted(t_hash.items()))

        # print(f'S.keys = {s_hash.keys()}')
        # print(f'S.values = {s_hash.values()}')

        # print(f'T.keys = {t_hash.keys()}')
        # print(f'T.values = {t_hash.values()}')

        if s_hash == t_hash:
            result = True
    

        return result