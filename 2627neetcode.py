# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]

def topk_frequent(nums,k):
    count = {}
    for i in nums:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i]=1
    return sorted(count,key=count.get,reverse=True)[:k]

nums = [1,2,2,3,3,3]
k = 2

print(topk_frequent(nums,k))



# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

def two_sum(nums, target):
    s = {}
    for i, num in enumerate(nums):
        need = target - num 
        if need in s: 
            return [s[need],i]
        else:
            s[num]=i

nums = [3,4,5,6]
target = 7

print(two_sum(nums,target))

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

def has_dupes(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        
        s.add(i)
    return False 

nums = [1, 2, 3, 3]
print(has_dupes(nums))


# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

def group_anagrams(strs):
    out = {}
    for i in strs:
        key = ''.join(sorted(i))
        if key in out:
            out[key].append(i)
        else:
            out[i] = [i]
    return list(out.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(group_anagrams(strs))
