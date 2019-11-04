def add(*nums):
    counter = 0
    for value in nums :
        counter += value
    return counter

def multiply(*nums):
    count = 1
    for value in nums :
        count *= value
    return count
