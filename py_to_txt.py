import os

def get_files_with_extensions(current_dir, extensions, exclude_files=[]):
    files_with_extensions = []
    allowed_dirs = [current_dir, os.path.join(current_dir, 'utils')]
    for root, _, files in os.walk(current_dir):
        if root in allowed_dirs:
            for file in files:
                if file.endswith(extensions) and file not in exclude_files:
                    files_with_extensions.append(os.path.join(root, file))
    return files_with_extensions

def main():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    script_name = os.path.basename(__file__)
    prompt_file_name = "prompt.txt"
    file_extensions = (".py", ".json")
    ignore_files = ["history.json", "skip.txt", "results.json", "prompt_templates.json"]

    with open(prompt_file_name, "w") as prompt_file:
        for file in get_files_with_extensions(current_dir, file_extensions, exclude_files=[script_name] + ignore_files):
            with open(file, "r") as target_file:
                content = target_file.read()

                prompt_file.write(f"=== {file} ===\n")
                first_section_end = content.find("#")
                prompt_file.write(content[:first_section_end])
                
                for ignore_file in ignore_files:
                    if os.path.exists(ignore_file):
                        with open(ignore_file, "r") as ignore:
                            ignore_content = ignore.read()
                            ignore_start = content.find(f"# {ignore_content.strip()}")
                            if ignore_start != -1:
                                first_section_end = ignore_start
                                prompt_file.write(f"...\n# {ignore_content.strip()} \n...\n")
                                break
                prompt_file.write(content[first_section_end:])
                prompt_file.write("\n\n")

            print(f"Content from {file} has been written to {prompt_file_name}")

if __name__ == "__main__":
    main()
