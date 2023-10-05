def bubble_sort(arr):
    n = len(arr)

    #traverse through all array elements
    for i in range(n):
        #last i elements are already in place
        for j in range(0, n-i-1):
            #swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [5, 2, 8, 12 ,3]
print(bubble_sort(arr))

        