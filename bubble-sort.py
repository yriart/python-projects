# bubble sort
import random

def create_list(x):
    my_list=[]
    while len(my_list)<x:
        my_list.append(random.randint(1,99))
    return my_list

my_list = create_list(50)
print my_list

# ul = unsorted list
def bubble_sort(ul):
    swap = True
    while swap == True:
        swap = False
        i = 0
        while i <= len(ul)-2:
            if ul[i] > ul[i+1]:
                swap = True
                bigger = ul[i]
                smaller = ul[i+1]
                ul[i] = smaller
                ul[i+1] = bigger
            i+=1

bubble_sort(my_list)
print my_list

# x,y = y,x
# ul[i], ul[i+1] = ul[i+1], ul[i]
