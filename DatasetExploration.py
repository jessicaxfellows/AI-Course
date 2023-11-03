import pickle 
import numpy as np
from sklearn.model_selection import train_test_split
import tarfile
import matplotlib.pyplot as plt

# extract the dataset
tar = tarfile.open(r"C:/Users/jessi/OneDrive/Documents/GitHub/AI-Course/cifar-10-python.tar.gz")
tar.extractall()
tar.close()

# define a function to load the batch file
def unpickle(file):
    with open(file, 'rb') as fo:
        data = pickle.load(fo, encoding='bytes')
    return data

# load dataset batch files
data_batch_1 = unpickle('cifar-10-batches-py/data_batch_1')
data_batch_2 = unpickle('cifar-10-batches-py/data_batch_2')
data_batch_3 = unpickle('cifar-10-batches-py/data_batch_3')
data_batch_4 = unpickle('cifar-10-batches-py/data_batch_4')
data_batch_5 = unpickle('cifar-10-batches-py/data_batch_5')

# combine the loaded batches into a single dataset
X_train = np.concatenate([
    data_batch_1[b'data'],
    data_batch_2[b'data'],
    data_batch_3[b'data'],
    data_batch_4[b'data'],
    data_batch_5[b'data']
])

y_train = np.concatenate([
    data_batch_1[b'labels'],
    data_batch_2[b'labels'],
    data_batch_3[b'labels'],
    data_batch_4[b'labels'],
    data_batch_5[b'labels']
])

# load the test batch
test_batch = unpickle('cifar-10-batches-py/test_batch')
X_test = test_batch[b'data']
y_test = np.array(test_batch[b'labels'])

# reshape the data
X_train = X_train.reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)
X_test = X_test.reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)

# split the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# verify the dataset extraction
print("Dataset extracted successfully!")

# check the dataset shape
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("X_val shape:", X_val.shape)
print("y_val shape:", y_val.shape)
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)

# visualize the images
fig, axes = plt.subplots(3, 5, figsize=(12, 6))
label_names = {
    0: "Airplane",
    1: "Car",
    2: "Bird",
    3: "Cat",
    5: "Dog",
    6: "Frog",
    7: "Horse",
    8: "Boat"
}
for i, ax in enumerate(axes.flat):
    ax.imshow(X_train[i])
    ax.set_title(f"Label: {y_train[i]}\n{label_names[y_train[i]]}")
    ax.axis("off")
plt.tight_layout()
plt.show()

# verify class labels
unique_labels = np.unique(y_train)
print("Unique class labels:", unique_labels)