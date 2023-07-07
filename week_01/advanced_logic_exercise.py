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
    else:
        index_1 = index_1 + 1
        index_2 = index_2 + 1

print(status)
    

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

total_sum = 0

for number in numbers:
    total_sum = total_sum + number
    
# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 







