def perceptron(threshold, adjustment, weights, examples, passNum):
    print("Starting weights:", weights)
    print("Threshold:",threshold, "Adjustment:",adjustment)

    for currPass in range(passNum):
        print("\nPass", currPass + 1,"\n")
        for example in examples:
            answer = example[0]
            input = example[1]
            print("inputs: ", input)
            print(answer, "is answer")
            
    # threshold is an int
    # adjustment is an int
    # weights is a list of ints
    # examples is a list of lists: [[ True?False , [0, 0, 0, 0, 0] ] , ...]
    # passNum is int
    return

## function for weight adjustment
## function for looping through examples and return true or false for each
