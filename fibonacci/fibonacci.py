def fibonacci(num):
    if num < 1:
        return 1
    nums = [1, 2]
    for i in range(1, num):
        nums.append(i + nums[i - 1])
    return nums.pop()


print(fibonacci(3))
