def containDuplicate(nums):
    ans = set()
    for i in nums:
        if i in ans:
            return True
        ans.add(i)
    return False

nums = [1,2,3,1]
print(containDuplicate(nums))
    