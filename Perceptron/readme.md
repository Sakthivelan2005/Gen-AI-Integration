# Perceptron
- Single-layer neutral network model.
- It is used for binary classification (The computer knows only 0s and 1s)
- It is only working for linear data.


**Example of Linear Data:**
|hours studies| Exam Result |
|---------|----------------|
|1| fail|
|2| fail|
|3| fail|
|4| pass|
|5| pass|
|6| pass|

- means if X-axis increase the Y-axis also increase

# Architecture

Inputs -> Weights -> Summation + Bias -> Activation -> Output

<img width="1312" height="590" alt="image" src="https://github.com/user-attachments/assets/45ab437d-98bf-42d1-82a6-6a4f28a2dee7" />


## Components of Perceptron
1. **`Weights`**- Access input values
2. **`Bias`** - Shifts the decision boundary. **Formula:** `(Weights * inputs) + bias`. The `default value - 0`
3. **`Activation function`** - convert output `either 1 or 0` 
```python
if(x > 0):
    return 1 
else:
    return 0
```
4. **`Learning rate`** - control how fast model learns the data.
**Rate**: `either 0.1 or 0.01 0r 0.001`

# Learning Algorithm
1. Initialize Weights
2. Predict Output
3. Compute Error
4. Update Weights
5. Repeat

## Advantages
- Simple
- Fast
- Easy to implement

## Limitations
- Solves only linearly separable problems.
- Cannot solve XOR ^ 

## Real Time using Applications
- Spam Filtering
- Pattern recognition


# Practical Example for this:
| `Input A` | `Input B` | **AND** | **OR** | **XOR**  |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

- To do this using perceptron concept in python:

### Training data For **`AND`** Operation
```python

#Sample input
input = [[0,0],[0,1],[1,0],[1,1]]

# Expected output
output = [0,0,0,1] # AND operation
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
for i in range(100):
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

# Testing the model
for i in input:
    linear_output = (weights[0] * i[0]) + (weights[1] * i[1]) + bias
    prediction = activation(linear_output)
    print("Input: ", i)
    print("Prediction: ",prediction)

```

### Training data For **`OR`** Operation
```python

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
for i in range(100):
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

# Testing the model
for i in input:
    linear_output = (weights[0] * i[0]) + (weights[1] * i[1]) + bias
    prediction = activation(linear_output)
    print("Input: ", i)
    print("Prediction: ",prediction)

```

### **`XOR`** Operation is not possible because it is non-linear data