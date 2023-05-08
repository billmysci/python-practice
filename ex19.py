# defines the function with 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints the first argument
    print(f"You have {cheese_count} cheeses!")
    # prints the second argument
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # prints filler text
    print(f"Man that's enough for a party!")
    # prints filler with newline
    print(f"Get a blanket.\n")


print("We can just give the function numbers directly:")
# calls the function with 2 numbers
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
# defines a first variable
amount_of_cheese = 10
# defines a second variable
amount_of_crackers = 50

# calls the function with the 2 variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# calls the function with both arguments having math done
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# calls the function with math, adding numbers to the variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)