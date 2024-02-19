# Create the alphabet string
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# 1. The first half of the string using starting and ending indices
first_half_start_end = alphabet[:len(alphabet)//2]

# 2. The first half of the string using only the ending index
first_half_end = alphabet[:len(alphabet)//2]

# 3. The second half of the string using starting and ending indices
second_half_start_end = alphabet[len(alphabet)//2:]

# 4. The second half of the string using only the starting index
second_half_start = alphabet[len(alphabet)//2:]

# 5. Every second letter in the string starting with 'a'
every_second_letter = alphabet[::2]

# 6. The entire string in reverse
reverse_alphabet = alphabet[::-1]

# 7. Every third letter of the string in reverse starting with 'z'
every_third_letter_reverse = alphabet[::-3]

# Print the results
print("1. First half (using starting and ending indices):", first_half_start_end)
print("2. First half (using only the ending index):", first_half_end)
print("3. Second half (using starting and ending indices):", second_half_start_end)
print("4. Second half (using only the starting index):", second_half_start)
print("5. Every second letter starting with 'a':", every_second_letter)
print("6. Entire string in reverse:", reverse_alphabet)
print("7. Every third letter in reverse starting with 'z':", every_third_letter_reverse)