class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2) - len(s1) + 1):
            set_new = []
            for j in range(i, i + len(s1)):
                set_new.append(s2[j])
            if sorted(set_new) == sorted(list(s1)):
                return True
        return False