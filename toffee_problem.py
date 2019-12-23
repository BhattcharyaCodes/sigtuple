def toffeeTotal(amount):

    if amount < 0:
        print("Invalid amount")

    else:
        toffee_counter = amount + (amount/5);
        print("Total number of toffees that can be bought is:{}", toffee_counter)


if __name__ == "__main__":
    price = input("Enter the money I have for buying the toffee");
    toffeeTotal(price)
