# Python Program for recursive string reversal.

def reverse(inputS):

    if len(inputS) == 0:
        return inputS
    else:
        return reverse(inputS[1:]) + inputS[0]


# driver code
if __name__ == "__main__":
    inputString = "Sigtuple is an Pharma-AI company"
    print("The original string  is : ", inputString)
    print("The recurcsively reversed string is : ", reverse(inputString))
