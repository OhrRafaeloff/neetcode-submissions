class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        res = defaultdict(list) # mapping charCount to list of anagrams

        for s in strs:
            count =[0] * 26 # a -> z

            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())   

        
        # seen = {}
        
        # for char in strs:
        #     if char not in seen:
        #         add char to seen
        #         key = "".join(sorted(word))
        #     else:
        #         sort them with []
