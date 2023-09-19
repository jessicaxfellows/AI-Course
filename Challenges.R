#Challenge 1
x <- 10 #create a variable x with value 10
cat("The value of x is:", x) #print x

#Challenge 2
sum_result <- 0 #initialize a variable to hold sum
#for loop with 2 increment increase to go up to 100
for (i in seq(2, 100, by=2)) {
  sum_result <- sum_result + i
} 
cat("The value for all even numbers between 2 and 100 is:", sum_result)

#Challenge 3
recur_factorial <- function(n) {
  if(n <=1) {
    return(1) #this is for 1 or 0 which both return 1
  }
  else {
    return (n * recur_factorial(n-1))
    #recursive case, multiply n with factorial of n-1
  }
}
recur_factorial(5) #call recursive function which prints factorial of passed number

#Challenge 4
input_phrase <- "Nami is a bear." #phrase to start with
vowels <- c("a", "e", "i", "o", "u") #create list of vowels
vowel_count <- 0 #initialize variable for count
input_phrase <- tolower(input_phrase) #change input to all lowercase
for(char in strsplit(input_phrase, "")[[1]]) {
  if(char %in% vowels) {
    vowel_count <- vowel_count + 1 #add to the count if vowel is present
    vowels <- vowels[vowels != char] #remove the counted vowel from the list
  }
}
cat("Number of unique vowels is:", vowel_count)

#Challenge 5
#weighted average calculation
numbers <- c(10, 15, 20, 25, 30) #list of numbers
weights <- c(0.1, 0.2, 0.3, 0.20, 0.2) #list of corresponding weights
weighted_sum <- sum(numbers * weights) #calc weighted sum
total_weight <- sum(weights) #calc total weight
weighted_average <- weighted_sum / total_weight #calc weighted average
cat("Weighted average is:", weighted_average)

#Challenge 6
#calculate summary stats of iris data set
summary(iris)
#scatter plot of sepal length and width
plot(iris$Sepal.Length, iris$Sepal.Width, xlab = "Sepal Length", ylab = "Sepal Width", main = "Scatter Plot of Sepal Length vs. Width")

