
def format_2d_array(arr):
    if not all(isinstance(row, list) and all(isinstance(val, int) and val >= 0 for val in row) for row in arr):
        raise ValueError("Input array should contain only positive integers in lists.")

    max_width = max(len(str(max(row)) + '0') for row in arr)
    formatted_output = ''

    for row in arr:
        for value in row:
            padding = max_width - len(str(value))
            formatted_output += ' ' * padding + str(value) + ' '

        formatted_output += '\n'

    return formatted_output

# User input for the number of rows and columns
try:
    num_rows = int(input("Enter the number of rows: "))
    num_cols = int(input("Enter the number of columns: "))
except ValueError:
    print("Invalid input. Please enter positive integers for rows and columns.")
    exit()

if num_rows <= 0 or num_cols <= 0:
    print("Number of rows and columns should be positive integers.")
    exit()

# Initialize an empty 2D array and populate it with user input
array_2d = []
for i in range(num_rows):
    row = []
    for j in range(num_cols):
        try:
            value = int(input(f"Enter the value for element ({i+1}, {j+1}): "))
            if value < 0:
                print("Please enter positive integers only.")
                exit()
            row.append(value)
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
            exit()
    array_2d.append(row)

formatted_array = format_2d_array(array_2d)
print("\nFormatted Array:")
print(formatted_array)
