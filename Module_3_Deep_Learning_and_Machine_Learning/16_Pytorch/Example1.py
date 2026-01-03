# importing libraries
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms

# defining the neural network module
class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.fc1=nn.Linear(784, 64)
        self.fc2=nn.Linear(64, 64)
        self.fc3=nn.Linear(64, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    
# define transforms to apply to mnist data set
transform=transforms.ToTensor()

# load the mnist data set
trainset=torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader=torch.utils.data.DataLoader(trainset, batch_size=32, shuffle=True)

# create an instance
model = NeuralNet()

# defining loss function
criterion = nn.CrossEntropyLoss()
optimizer=optim.Adam(model.parameters(), lr=0.001)

# train the model
for epoch in range(5):
    running_loss = 0.0
    for inputs, labels in trainloader:
        optimizer.zero_grad()
        
        outputs = model(inputs.view(-1, 28*28))
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
    print(f"Epoch {epoch+1} - Loss: {running_loss/len(trainloader):.4f}")

# make predictions
testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=5, shuffle=False)

# make prediction
with torch.no_grad():
    for inputs, labels in testloader:
        outputs = model(inputs.view(-1, 28*28))
        _, predicted = torch.max(outputs.data,1)

print(predicted) 


# https://docs.pytorch.org/docs/stable/index.html