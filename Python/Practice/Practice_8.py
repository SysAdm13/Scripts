def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
            print(sum)
            continue
        else:
            continue
    return sum

print(positive_sum([-1,-2,-3,-4,-5]))