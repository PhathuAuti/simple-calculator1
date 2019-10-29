def add(*nums):
    list_of_numbers = list(nums)
    counter = 0
    for value in list_of_numbers :
        counter += value
    return counter

def multiply(*nums):
    list_of_numbers = list(nums)
    count = 1
    for value in list_of_numbers :
        count *= value
    return count