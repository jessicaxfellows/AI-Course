#load the data set + library
library(caret)
data(iris)

#set seed
set.seed(123)

#split into testing and training sets
train_index <- createDataPartition(iris$Species, p = 0.7,
                                   list = FALSE,
                                   times = 1)
data_train <- iris[train_index, ]
data_test <- iris[-train_index, ]

#create model
model <- lm(Sepal.Length ~ Sepal.Width + Petal.Length + Petal.Width,
            data = data_train)

#make predictions with model
predictions <- predict(model, newdata = data_test)

#evaluate model
mse <- mean((predictions - data_test$Sepal.Length)^2) #mean square error
print(paste("Mean Squared Error:", mse))

#use trained model for predictions on new data
#select first 5 rows as new data for prediction
new_data <- iris[1:5, ]
new_predictions <- predict(model, newdata = new_data)