class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedarray = sorted(nums) #nlogn
        if (len(nums)==0):
            return 0
        #[0,1,1,2,]
        longest_seq = 0
        seq=1
        for i in range(1,len(sortedarray)): # n
            if (sortedarray[i]-sortedarray[i-1] == 1):
                seq+=1
                continue
            elif(sortedarray[i] == sortedarray[i-1]):
                continue

            longest_seq = max(seq, longest_seq)
            seq=1
        longest_seq = max(seq, longest_seq) # Why? Because if the last 2 numbers are the same, it will 'continue' without pdating the longest seq
        return longest_seq

    #n + nlogn = n log n