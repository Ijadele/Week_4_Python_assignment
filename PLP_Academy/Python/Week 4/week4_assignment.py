import os

# File Read & Write Program

def read_and_write_file(input_filename, output_filename):
    try:
        # Check if the input file exists
        if not os.path.exists(input_filename):
            print(f"Error: The file '{input_filename}' does not exist. Creating the file with sample content...")
            # Create the input file with some sample content
            with open(input_filename, 'w') as infile:
                infile.write("Hello, this is a test file.\nThis content will be modified.")
        
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            # Read the content of the input file
            content = infile.read()
            
        # Modify the content (example: converting all text to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")
    
    except IOError:
        print("Error: There was an issue reading or writing to the file.")

# Example Usage
input_filename = "input.txt"
output_filename = "output.txt"
read_and_write_file(input_filename, output_filename)


def open_file():
    filename = input("Please enter the filename: ")

    # Check if the file exists
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        
        # Ask if the user wants to create the file
        create_new = input("Do you want to create this file? (y/n): ").strip().lower()
        
        if create_new == 'y':
            # Create a new file with some sample content
            with open(filename, 'w') as new_file:
                new_file.write("This is a new file created with sample content.")
            print(f"File '{filename}' has been created with some sample content.")
        else:
            print("File not created. Exiting the program.")
            return
    else:
        try:
            # Open the file in read mode
            with open(filename, 'r') as file:
                content = file.read()
                print(f"File content:\n{content}")
        except IOError:
            print(f"Error: The file '{filename}' can't be read.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example Usage
open_file()
