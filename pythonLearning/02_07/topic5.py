heros = ["bat-man", "super-man", "iron-man", "spider-man"]

# for index in range(0, 4, 1):
#     print(heros[index])

for item in heros:
    print(item)

nums = [1, 2, 3, 4, 5, 10, 4, 5, 2]
for singleNumber in nums:
    print(singleNumber)

for index in range(len(heros)):
    print(heros[index])

for index in range(len(nums) - 1, -1, -1):
    print(nums[index])

for item in reversed(nums):
    print(item)

sum=0
for item in nums:
    sum += item
print(sum)

print("average", int(sum/len(nums)))

sum = 0
for item in nums:
    if item%2 == 0:
        sum += item
print(sum)

max = nums[0]
for item in nums:
    if max < item:
        max = item
print(max)