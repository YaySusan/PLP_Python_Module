# File Read & Write with Error Handling

def read_and_write_changes_to_a_new_file():
    """
    Reads content from a file specified by the user, modifies it by converting
    to uppercase, and writes it to a new file named 'modified_output.txt'.
    Handles errors if the file doesn't exist or can't be read.
    """
    filename = input("Enter the filename you want to read: ")

    try:
        # Open the file in read mode
        with open(filename, "r") as file:
            original_content = file.read()

        # Ask the user for a joke to add to the modified file
        joke = input("Share a joke to add to the file:" )

        # Append the joke to the content
        modified_content = original_content + "\n\n" + "The user's joke: " + joke

        # Write the modified content to a new file
        with open("modified_version_file.txt", "w") as outfile:
            outfile.write(modified_content)
        
        print(f"You have successfully read from '{filename}', made changes, and added your joke to a new file named 'modified_version_file.txt'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Please check the filename and try again.")

    except PermissionError:
        print(f"Error: You don't have permission to read the file '{filename}'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call/run the function
read_and_write_changes_to_a_new_file()
