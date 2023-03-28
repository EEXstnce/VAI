import os

def get_files_with_extensions(current_dir, extensions, exclude_files=[]):
    return [file for file in os.listdir(current_dir) if file.endswith(extensions) and file not in exclude_files]

def main():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    script_name = os.path.basename(__file__)
    prompt_file_name = "prompt.txt"
    file_extensions = (".py", ".json")
    ignore_files = ["ignore.txt", "skip.txt", "results.json", "prompt_templates.json"]  # Add your ignore files here

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
                            ignore_start = content.find(f"# {ignore_content.strip()}")  # Look for the ignore content
                            if ignore_start != -1:  # Ignore content found, update first_section_end
                                first_section_end = ignore_start
                                prompt_file.write(f"...\n# {ignore_content.strip()} \n...\n")
                                break  # Only skip the first occurrence of ignore content
                prompt_file.write(content[first_section_end:])
                prompt_file.write("\n\n")

            print(f"Content from {file} has been written to {prompt_file_name}")

if __name__ == "__main__":
    main()
