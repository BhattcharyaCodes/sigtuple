def toffeeTotal(amount):

    if amount < 0:
        print("Invalid amount")
    elif amount == 0:
        wrapper_flag = input("Sorry! you cant buy toffee with no money. Do you have wrapper to exchange with? Enter Y for *YES* and any other character for *NO* ")
        if wrapper_flag == "Y":
            wrapper = int(input("How many wrappers do you have?"))
            toffee_counter = wrapper / 5
            print("Total number of toffees that can be bought is:", toffee_counter)
        else:
            print("This is the end of the road for you. Bye!")

    else:
        toffee_counter = amount + (amount/5)
        print("Total number of toffees that can be bought is:", toffee_counter)


if __name__ == "__main__":
    price = int(input("Enter the money I have for buying the toffee: "))
    toffeeTotal(price)
