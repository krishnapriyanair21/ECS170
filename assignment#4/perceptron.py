def perceptron(threshold, adjustment, weights, examples, passNum):
    # initial print
    print("Starting weights:", weights)
    print("Threshold:",threshold, "Adjustment:",adjustment)

    for currPass in range(passNum): # loop for passNum
        print("\nPass", currPass + 1)
        print()
        for example in examples:
            answer = example[0] # pull actual answer
            input = example[1] # pull input list
            print("inputs:", input)
            prediction = checkExample(threshold, input, weights) # returns bool prediction
            print("prediction:",prediction,"answer:", answer) 
            if (prediction != answer):
                if (answer): # if should be true but actually false
                    weightsUp = adjustUp(adjustment, input, weights)
                    weights = weightsUp
                else: # if should be false but actually true
                    weightsDown = adjustDown(adjustment, input, weights)
                    weights = weightsDown
            print("adjusted weights:",weights)
    return

# input: threshold, input list, weight list; finds sum and returns true if greater than threshold, returns false otherwise
def checkExample(threshold, example, weights):
    sum = 0
    for i in range(len(weights)):
        sum += (example[i]*weights[i])
    if sum > threshold:
        return True
    else: 
        return False

# input: adjustment factor, input list, weight list; increases weight element by adjustment for each instance of input == 1
# returns adjusted weight list
def adjustUp(adjustment, example, weights):
    for i in range(len(example)):
        if (example[i] == 1):
            weights[i] += adjustment
    return weights

# input: adjustment factor, input list, weight list; decreases weight element by adjustment for each instance of input == 1 
# returns adjusted weight list
def adjustDown(adjustment, example, weights):
    for i in range(len(example)):
        if (example[i] == 1):
            weights[i] -= adjustment
    return weights