"""list1=[1,5,6,8,3]
list2=[2,4,7,9]
list3=list1+list2
print(list3)
list4=sorted(list3,reverse=True)
print(list4)"""

# Sorting list
nums=[8,5,4,6,2,1,7]
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]<nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
print(nums)