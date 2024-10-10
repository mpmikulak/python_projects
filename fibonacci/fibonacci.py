# Numbers are cool, right?
# I think so, so let's make some
def fibonacci(num):
    int_num = int(num)
    if int_num < 1:
        return 1
    elif int_num == 1 or int_num == 2:
        return 1

    nums = [0, 1]
    for i in range(2, int_num + 1):
        nth = nums[i - 1] + nums[i - 2]
        nums.append(nth)
    return nums.pop()


def parse(target_num):
    if target_num.isnumeric():
        return target_num
    else:
        print("Enter a number, please.")


target_num = input("Which Fibonacci number do you want?")
print(fibonacci(parse(target_num)))
