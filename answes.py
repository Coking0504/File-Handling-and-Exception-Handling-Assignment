def modify_and_write_file(input_filename, output_filename, modification_function):
    """Reads a file, applies a modification function to each line, and writes the modified content to a new file.

    Args:
        input_filename: The name of the input file.
        output_filename: The name of the output file.
        modification_function: A function that takes a line (string) as input and returns the modified line (string).
    """
    try:
        with open("input_filename.txt", 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                modified_line = modification_function(line)
                outfile.write(modified_line)
        print(f"File '{input_filename}' processed and saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename.txt}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def convert_to_uppercase(line):
    """Example modification function: converts a line to uppercase."""
    return line.upper()



def add_line_numbers(line):
    """Example modification function: adds line numbers to each line."""
    global line_number # Access the global line number
    line_number +=1
    return f"{line_number:4}: {line}"

line_number = 0 # Initialize global line number





# Example usage with different modification functions:

input_file = "input.txt" # Replace with your input filename
output_file_uppercase = "output_uppercase.txt"
output_file_numbered = "output_numbered.txt"




modify_and_write_file(input_file, output_file_uppercase, convert_to_uppercase)



line_number = 0 # Reset line number for the next operation
modify_and_write_file(input_file, output_file_numbered, add_line_numbers)


# question 2
# This function processes a file and handles potential errors such as file not found or permission denied.
def process_file(filename):
    """Processes the file specified by the filename.

    Args:
        filename: The name of the file to process.
    """
    try:
        with open("filename.pdf", 'r') as f:
            # Process the file content here (e.g., read lines, perform calculations, etc.)
            for line in f:
                print(line, end="") # Example: print the file contents
        print(f"\nFile '{filename.pdf}' processed successfully.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to open '{filename}'.")
    except Exception as e: # Catch other potential errors
        print(f"An unexpected error occurred: {e}")



# Get filename input from the user and handle errors
while True:
    try:
        filename = input("Enter the filename: ")
        process_file(filename)
        break # Exit the loop if file processing is successful

    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
        break




