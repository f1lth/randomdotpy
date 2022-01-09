from os import system

system("Color A")
system('cls')

def get_input(order):
    ''' Gets an integer input from the user 
            Parameters:
                order: str, order in which the number is being asked, i.e first, second
    '''

    is_int = False

    while is_int == False:

        number = input(f"Please enter the {order} number: ")
        try:
            int(number)
            return int(number)
        except ValueError:
            print("Error: Enter integers only!\n")

def get_divisors(num):

    divisors = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def compare_divisors(list_1, list_2):

    common_divisors = []

    for i in range(len(list_1)):
        if list_1[i] in list_2:
            common_divisors.append(list_1[i])

    return common_divisors


def main():

    num1 = int(get_input("first"))
    num2 = int(get_input("second"))
    list_1 = get_divisors(num1)
    list_2 = get_divisors(num2)
    common_divisors = compare_divisors(list_1, list_2)
    
    system('cls')

    print(f"Printing common divisors of ({num1}, {num2})")
    print("...")
    print(common_divisors)


main()
