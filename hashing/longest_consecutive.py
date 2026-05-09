def longestConsecutive(nums):
    mp = {}
    longest = 0
    
    for num in nums:
        
        # skip duplicates
        if num in mp:
            continue
        
        left = mp.get(num-1, 0)
        right = mp.get(num+1, 0)
        
        length = left + 1 + right
        
        mp[num] = length
        
        # update boundaries
        mp[num-left] = length
        mp[num+right] = length
        
        longest = max(longest, length)
    
    return longest