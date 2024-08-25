def get_factorial(number):
    answer = 1
    for i in range (number, 0 , -1):
        answer = answer * i
    return answer


# number = int(input("Enter a number "))
# factorial = get_factorial(number)
# print(factorial)




def get_fibonacci_sequence(number):
    previous_number = 0
    current_number = 0
    sequence  = []
    sum1 = 0
    for i in range (number):
        previous_number = current_number
        sequence.append(previous_number + current_number)
        current_number = i

        print(f" previous_number: {previous_number} current_number : {current_number}")
    return sequence
number = int(input("Enter a number "))
sequence =get_fibonacci_sequence(number)
print(sequence)
