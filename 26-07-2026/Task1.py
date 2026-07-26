
#Learnings of Perception concept
#training data 
import numpy as np
inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
#expected output
outputs = np.array([0,0,0,1])
weights = np.array([0,0])
bias = 0
learning_rate = 0.1
def activation(x):
    if(x>=0):
        return 1
    else:
        return 0

#Training phase in perceptron 
for i in range(40):
    for j in range(len(inputs)):
        x1,x2 = inputs[j]
        target = outputs[j]
        linear_output = (weights[0]*x1)+(weights[1]*x2) + bias
        prediction = activation(linear_output)
        error = target-prediction
        weights[0] = weights[0] + learning_rate * error * x1 
        weights[1] = weights[1] + learning_rate * error * x2 
        bias = bias + learning_rate * error 
        print("Prediction is: ",prediction)
        print("Error: ",error)

print("Trained weights: ",weights)
print("Trained bias: ",bias)

for x in inputs:
    linear_output = (weights[0]*x[0])+(weights[1]*x[1]) + bias 
    prediction = activation(linear_output)
    print("input value: ",x)
    print("output value: ",prediction)

