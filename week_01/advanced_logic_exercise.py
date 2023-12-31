# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_ints = []
for number in numbers:
    if number % 2 == 0:
        even_ints.append(number)
                
print(even_ints)

# 2. Print the difference between the largest and smallest value:
sorted_numbers = sorted(numbers)
difference_of_numbers = sorted_numbers[9] - sorted_numbers[0]

print(difference_of_numbers)
# 3. Print True if the list contains a 2 next to a 2 somewhere.

status = False
index_1 = 0
index_2 = 1

for number in numbers:
    if numbers[index_1] == numbers[index_2]:
        status = True
        break
    else:
        index_1 = index_1 + 1
        index_2 = index_2 + 1

print(status)
    

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

def list_count(numbers):
    sum = 0
    stop = False
    for number in numbers:
        if number == 6:
            stop = True
        elif number == 7:
            stop = False
        elif stop == False:
            sum = sum + number
    return sum

print(list_count(numbers))

# ATTEMPT ONE
# for number in numbers:
#     total_sum = total_sum + number
#     if number in numbers == 6:
#         break
#     if number in numbers == 7:
#         continue

# print(total_sum)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

previous_number = None
index = 0
total = 0
for number in numbers:
    if number == 13 or previous_number == 13:
        previous_number = number
        pass
    else:
        total += number

    previous_number = number

print(total)






