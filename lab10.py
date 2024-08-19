def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

def count_digit_occurrences(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Initialize a dictionary to count occurrences of each digit
    digit_count = {}
    
    # Count occurrences of each digit
    for digit in num_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
    
    return digit_count

# Input number
number = input("Enter a number: ")

# Check if the number is a palindrome
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

# Count and print occurrences of each digit
digit_count = count_digit_occurrences(number)
print("Digit occurrences:")
for digit, count in digit_count.items():
    print(f"{digit}: {count} times")
