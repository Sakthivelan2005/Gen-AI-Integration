# Training data

#Sample input
input = [[0,0],[0,1],[1,0],[1,1]]

# Expected output
output = [0,1,1,1] # OR operation
weights = [0,0] # Initial value of the input
bias = 0
learning_rate = 0.1

#Activation Function
def activation(x):
    if x>0:
        return 1
    else:
        return 0
    
# Training Phase in perceptron
for i in range(20):
    for j in range(len(input)):
        x1, x2 = input[j]
        target = output[j]
        linear_output = (weights[0] * x1) + (weights[1] * x2) + bias
        prediction = activation(linear_output)
        error = target - prediction
        weights[0] = weights[0] + learning_rate * error * x1 
        weights[1] = weights[1] + learning_rate * error * x2
        bias = bias + learning_rate * error
        print("Prediction is ", prediction)
        print("Error: ", error)
print("Trained wieghts: ", weights)
print("Trained Bias: ", bias)

print("-------Testing----------")
# Testing the model
for i in input:
    linear_output = (weights[0] * i[0]) + (weights[1] * i[1]) + bias
    prediction = activation(linear_output)
    print("Input: ", i)
    print("Prediction: ",prediction)
