#install pytorch and torchvision
import torch
import torch.nn as nn
import torch.optim as optim

#define a neural network model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(10, 8)
        self.fc2 = nn.Linear(8, 2)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x
    
#create an instance of the neural network
model = NeuralNetwork()

#define the loss function
criterion = nn.CrossEntropyLoss()

#define the optimizer
optimizer = optim.SGD(model.parameters(), lr=0.01)

#sample input data
input_data = torch.randn(1, 10) #reshaped to (1, 10)

#peform the fwd pass
output = model(input_data)

#perform backward pass and update the weights
optimizer.zero_grad()
loss = criterion(output, torch.tensor([1])) #assumung the target class is 1
loss.backward()
optimizer.step()

#print the updated model params
print("Updated model parameters:")
for name, param in model.named_parameters():
    if param.requires_grad:
        print(name, param.data)

#print the loss value
print("Loss:", loss.item())

#new function to calculate accuracy
def calculate_accuracy(output, target):
    _, predicted = torch.max(output, 1)
    accuracy = (predicted == target).sum().item() / target.size(0)
    return accuracy

#calculate and print accuracy
target = torch.tensor([1]) #assuming the target class is 1
accuracy = calculate_accuracy(output, target)
print("Accuracy:", accuracy)