import os
import shutil

def get_user_choice(current_path, root_path, prompt_message):
    print(f"Current directory: {os.path.abspath(current_path)}")
    print("Contents:")
    contents = os.listdir(current_path)
    for i, item in enumerate(contents, 1):
        print(f"  {i}. {item}")
    print(f"  {len(contents) + 1}. [Go to parent directory]")
    print(f"  {len(contents) + 2}. [Quit file explorer]")
    
    user_choice = input(f"{prompt_message} Select an option, enter a file name, or type 'q' to quit: ").strip()

    if user_choice == 'q':
        return None
    
    try:
        user_choice = int(user_choice)
        if user_choice == len(contents) + 1:
            # Go to parent directory
            return 'parent'
        elif user_choice == len(contents) + 2:
            # Quit the file explorer
            return None
        else:
            selected_item = contents[user_choice - 1]
            selected_path = os.path.join(current_path, selected_item)
            if os.path.isdir(selected_path):
                return ('subfolder', selected_path)
            else:
                return selected_path
    except ValueError:
        # User entered a file name
        file_path = os.path.join(current_path, user_choice)
        if os.path.isfile(file_path):
            return file_path
        else:
            print("The specified file does not exist.")
    except IndexError:
        print("Invalid option. Please try again.")

def copy_with_option(source_file, destination_file, copy_option):
    if copy_option == 'c':
        # Normal copy
        shutil.copy2(source_file, destination_file)
    elif copy_option == 'a':
        # Append to destination file
        with open(source_file, 'rb') as src, open(destination_file, 'ab') as dest:
            shutil.copyfileobj(src, dest)
    elif copy_option == 'p':
        # Prepend to destination file
        with open(source_file, 'rb') as src, open(destination_file, 'rb+') as dest:
            original_content = dest.read()
            dest.seek(0)
            shutil.copyfileobj(src, dest)
            dest.write(original_content)

def file_explorer(purpose, root_path='.'):
    prompt_message = f"Select a {purpose} file."
    current_path = root_path
    root_path = os.path.abspath(root_path)  # Get absolute path of the root directory
    while True:
        user_choice = get_user_choice(current_path, root_path, prompt_message)
        if user_choice is None:
            # Quit the file explorer
            return None
        elif user_choice == 'parent':
            # Go to parent directory
            parent_path = os.path.dirname(current_path)
            parent_path = parent_path if parent_path else root_path
            if os.path.abspath(parent_path).startswith(root_path):
                current_path = parent_path
            else:
                print("Cannot navigate above the root directory.")
        elif user_choice[0] == 'subfolder':
            current_path = user_choice[1]
        else:
            if purpose == 'destination':
                # Ask for copy option for destination file
                while True:
                    copy_option = input("Choose copy option (c: copy, a: append, p: prepend): ").strip().lower()
                    if copy_option in ('c', 'a', 'p'):
                        break
                    print("Invalid option. Please enter 'c', 'a', or 'p'.")
                return (user_choice, copy_option)
            else:
                return user_choice

if __name__ == '__main__':
    source_file = file_explorer(purpose="source")
    if source_file is None:
        print("Source file selection canceled.")
    else:
        destination_choice = file_explorer(purpose="destination")
        if destination_choice is None:
            print("Destination file selection canceled.")
        else:
            destination_file, copy_option = destination_choice
            copy_with_option(source_file, destination_file, copy_option)