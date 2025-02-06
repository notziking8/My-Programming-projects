"""
Zion King
Comp 163-004
3/17/24
in this program, I will be getting the input from the user to create a list of integers.
Determining whether the list contains all multiples of 10, no multiples of 10,
or mix values of 10 and other values.
"""
# Check if all elements in the list are multiples of ten.
def is_list_mult10(my_lst):

    return all(item % 10 == 0 for item in my_lst)

# Check if the list contains no multiples of ten.
def is_list_no_mult10(my_lst):
    return all(item % 10 != 0 for item in my_lst)

def main():
    # Get input from the user.
    num_items = int(input("Enter size of the list: "))
    my_lst = []
    for i in range(num_items):
        # Will add the numbers the user entered into the list.
        item = int(input("Enter the {} item: ".format(i + 1)))
        my_lst.append(item)

    # Check if all integers in the list are multiples of 10, not a multiple or a mixed value.
    if is_list_mult10(my_lst):
        print("all multiples of 10")
    elif is_list_no_mult10(my_lst):
        print("no multiples of 10")
    else:
        print("mixed values")

if __name__ == "__main__":
    main()