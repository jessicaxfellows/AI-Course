bubble_sort <- function(arr) {
    n <- length(arr)

    #traverse through all array elements
    for (i in 1:(n-1)) {
        #last i elements are already in place
        for (j in 1:(n-i)) {
            #swap if the element found is greater than the next element
            if (arr[j] > arr[j+1]) {
                temp <- arr[j]
                arr[j] <- arr[j+1]
                arr[j+1] <- temp
            }
        }
    }
    print(arr) #display
}

arr <- c(5, 2, 8, 12, 3)
bubble_sort(arr)