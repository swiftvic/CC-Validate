'''
Drop the last digit from the number. The last digit is what we want to check against
Reverse the numbers
Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
Add all the numbers together
The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10 (Modulo 10)
'''

'''
Created Feb 1
by Victor Au Yeung
Capstone project 1
'''

def validate(number):
    # Turn number into a list
    '''
    # Original way of doing it without list comprehension
    num_list = []

    for num in str(number):
        num_list.append(int(num))

    print(num_list)
    '''
    # Using list comprehension (will always append list) 
    # below to convert integer number to a string, iterate through it 
    # then store it back into num_list as an integer.
    
    num_list = [int(num) for num in str(number)]

    last_num = num_list.pop()                       # Drop last digit
    num_list.reverse()                              # Reverse the numbers in place of num_list

    # List comprehension to check if the index is odd or 0 and multiply
    # the value at index location by 2, or else just leave it.
    # Divisble by 2 because human readable index start at 1 not 0, so index 2 for python is actually
    # index 1 for humans to read.
    mult_num_list = [num_list[odd_index] * 2 if odd_index % 2 == 0 else num_list[odd_index] for odd_index in range(len(num_list))]

    '''
    # Built above expression using for loop
    mult_num_list = []

    for odd_index in range(len(num_list)):
        if odd_index % 2 == 0 or odd_index == 0:
            mult_num_list.append(num_list[odd_index] * 2)
        else:
            mult_num_list.append(num_list[odd_index])
    '''

    # Subtract all numbers above 9 by 9
    sub_num_list = [mult_num_list[index] - 9 if mult_num_list[index] > 9 else mult_num_list[index] for index in range(len(mult_num_list))]

    '''
    # Just to see what's going on
    print(num_list)
    print(mult_num_list)
    print(sub_num_list)
    print("last number: " + str(last_num))
    print(sum(sub_num_list))
    print(sum(sub_num_list) % 10)
    '''
    # Adds all numbers in list plus last digit, if divislbe by 10, number is valid.
    return((sum(sub_num_list) + last_num) % 10 == 0)

if __name__ == '__main__':

    import os

    check_another = True

    while check_another:

        invalid = True

        os.system('cls')               # clears screen on Windows
        #os.system('clear')            # clears screen on Linux

        while invalid:
            try: 
                user_number = int(input("Enter a number you want to verify: "))

                if user_number < 0:
                    print("Try again, please enter a valid card number.")
                    invalid = True
                else:
                    print("Analyzing " + str(user_number) + ".......")
                    invalid = False
            
            except ValueError:
                print("Try again.")
                print("Please enter a valid number.")

        is_valid = validate(user_number)

        if is_valid:
            print("Credit Card number: " + str(user_number) + " is real.")
        else:
            print("Credit Card number: " + str(user_number) + " is fake.")

        user_input = input("\nCheck another? y/n: ")

        if user_input[0].lower() == 'y':
            check_another = True
        else:
            print("Goodbye")
            check_another = False