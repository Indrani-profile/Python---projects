def unique_sorted_list(input_list):
    # Use set to remove duplicates and then convert back to list
    unique_list = list(set(input_list))

    # Sort the list
    unique_list.sort()

    return unique_list

# Test with a list of numbers
numbers_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result_numbers = unique_sorted_list(numbers_list)
print("Original list of numbers:", numbers_list)
print("Unique sorted list of numbers:", result_numbers)

# Test with a list of strings
strings_list = ["apple", "orange", "banana", "apple", "kiwi", "orange"]
result_strings = unique_sorted_list(strings_list)
print("\nOriginal list of strings:", strings_list)
print("Unique sorted list of strings:", result_strings)
