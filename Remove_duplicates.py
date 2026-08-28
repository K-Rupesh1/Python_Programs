'''def RemoveDuplicates(nums):
    num=len(nums)
    if num ==0:
        return False
    i=0
    for j in range(0,num):
        if nums[j] != nums[i]:
            i+=1
            nums[i]=nums[j]
    return nums
nums=[0,0,1,1,1,2,2,3,3,4]
result=RemoveDuplicates(nums)
print(f" removed count: {result}")'''

def RemoveDuplicates(nums):
    n=len(nums)
    arr=[]
    if n==0:
        return False
    for i in range(0,n):
        if nums[i] not in arr:
            arr.append(nums[i])
    return arr
    
nums=[0,0,1,1,1,2,2,3,3,4]
result=RemoveDuplicates(nums)
print(f"final Arr: {result}")

            