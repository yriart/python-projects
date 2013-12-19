def quicksort(unsorted_list):
    if len(unsorted_list)==0:
        return unsorted_list
    midpoint = unsorted_list[0]
    less = quicksort([item for item in unsorted_list[1:] if item <= midpoint])
    more = quicksort([item for item in unsorted_list[1:] if item > midpoint])

    return less+[midpoint]+more

my_numbers = [7,1,3,4,0,9,6,5,2,8]

print quicksort(my_numbers)
