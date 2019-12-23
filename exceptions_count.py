# Python Program for log file analysis & exception capture.

def exceptionscapture:
    fileName = input("Enter the name of the file")
    logs = open(fileName)

    dict = {}
    table = []

    for line in logs:
        contents = line.strip().split(':')
        table.append(contents)

    for line in table:
        for exception in line:
            if exception in dict:
                dict[exception] += 1
            else:
                dict[exception] = 1
        for exceptions, occurences in dict.item():
            print(exceptions, ':', occurences )


