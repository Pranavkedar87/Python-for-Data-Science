def search(nums,t):
    for i in range(0,len(nums)):
        if nums[i] == t:
            return i
    return -1
nums = [1,2,3,4,5]
print(search(nums,8))