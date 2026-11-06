class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs: #for each word
            count = [0]*26 # [0,0,0,0, ....]
            for c in s:
                num = ord(c) - ord('a') #ord() converts into ASCII nums
                count[num]+=1 #eg. [0,0,1,0,0,...]
            res[tuple(count)].append(s)
        return list(res.values())

            

