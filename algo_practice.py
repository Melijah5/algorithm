# python code below!

# bubble sort
# sort the array in ascending order
arr =[8,9,4,7,25,1,5,2,1,6]

def bubblesort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1]= arr[i+1],arr[i]
    return arr
print(bubblesort(arr))




# selection sort

arr =[8,9,4,7,25,1,5,2,1,6]

def selectionsort(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i+1, len(arr)):
            if arr[min_value] > arr[j]:
                min_value = j
        arr[i], arr[min_value] = arr[min_value],arr[i]
    return arr
print(selectionsort(arr))


# final countdown
# just like flexible countdown, add an extra parameter so that if mult is equal to para4, skip that number using a while loop
def final_countdown(mult,low, high, para4):
    while low < high:
        low = low + 1
        if low % mult == 0 and low != para4:
            print low