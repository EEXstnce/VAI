import os

def main():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    script_name = os.path.basename(__file__)
    prompt_file_name = "prompt.txt"

    with open(prompt_file_name, "w") as prompt_file:
        for file in os.listdir(current_dir):
            if file.endswith(".py") and file != script_name:
                with open(file, "r") as py_file:
                    code = py_file.read()

                    prompt_file.write(f"=== {file} ===\n")
                    prompt_file.write(code)
                    prompt_file.write("\n\n")

                print(f"Code from {file} has been written to {prompt_file_name}")

if __name__ == "__main__":
    main()
