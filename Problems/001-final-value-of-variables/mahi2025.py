def valueAfterOperations(operations):
    value = 0
    for operation in operations:
        if operation == "++X" or operation == "X++":
            value += 1
        else:
            value -= 1
            
    return value

print(valueAfterOperations(["++X", "++X"])) # Output: 2