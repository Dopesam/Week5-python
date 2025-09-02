# Ask the user for a filename
filename = input("Enter the name of the file to read: ")

try:
    # Try to open and read the file
    with open(filename, 'r') as file:
        content = file.read()

    # Modify the content (make it uppercase)
    new_content = content.upper()

    # Write the new content to a different file
    with open('new_file.txt', 'w') as new_file:
        new_file.write(new_content)

    print("✅ Done! Modified content saved to 'new_file.txt'.")

except FileNotFoundError:
    print("❌ File not found. Please check the name and try again.")
