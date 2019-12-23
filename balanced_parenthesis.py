def checker(in_str):
    open_list = ['[', '{', '(']
    close_list = [']', '}', ')']
    stack = []
    for i in in_str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(stack) > 0 and open_list[pos] == stack[(len(stack) - 1)]:
                stack.pop()
            else:
                return "Unbalanced Parentheses"

    if len(stack) == 0:
        return "Balanced Parentheses"


# driver code
if __name__ == "__main__":
    # string = "[{abc}]"
    inputString = input("enter your expression")
    print(checker(inputString))
