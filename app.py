import os

def print_menu():
    print("========== File Manager ==========")
    print("1. View current directory")
    print("2. Navigate to a directory")
    print("3. Create a new directory")
    print("4. Rename a file")
    print("5. Delete a file")
    print("6. Exit")

def view_directory(directory):
    print(f"Current directory: {directory}")
    files = os.listdir(directory)
    for file in files:
        print(file)

def navigate_directory(directory):
    new_dir = input("Enter the name of the directory: ")
    new_path = os.path.join(directory, new_dir)
    if os.path.isdir(new_path):
        return new_path
    else:
        print("Directory does not exist.")
        return directory

def create_directory(directory):
    new_dir = input("Enter the name of the new directory: ")
    new_path = os.path.join(directory, new_dir)
    try:
        os.mkdir(new_path)
        print("Directory created successfully.")
    except OSError:
        print("Failed to create directory.")

def rename_file(directory):
    file_name = input("Enter the name of the file to rename: ")
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        new_name = input("Enter the new name: ")
        new_path = os.path.join(directory, new_name)
        try:
            os.rename(file_path, new_path)
            print("File renamed successfully.")
        except OSError:
            print("Failed to rename file.")
    else:
        print("File does not exist.")

def delete_file(directory):
    file_name = input("Enter the name of the file to delete: ")
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
            print("File deleted successfully.")
        except OSError:
            print("Failed to delete file.")
    else:
        print("File does not exist.")

def main():
    directory = os.getcwd()
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_directory(directory)
        elif choice == "2":
            directory = navigate_directory(directory)
        elif choice == "3":
            create_directory(directory)
        elif choice == "4":
            rename_file(directory)
        elif choice == "5":
            delete_file(directory)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
