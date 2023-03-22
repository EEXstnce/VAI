import os
import requests
import base64

def download_github_repo_content(repo_url):
    api_base_url = "https://api.github.com/repos/"
    raw_base_url = "https://raw.githubusercontent.com/"

    repo_parts = repo_url.split("/")
    username, repo_name = repo_parts[-2], repo_parts[-1]

    api_url = f"{api_base_url}{username}/{repo_name}/contents"

    headers = {
        "Accept": "application/vnd.github+json",
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        print("Error fetching repository content. Please check the URL and try again.")
        return None, None, None, None

    repo_content = response.json()

    if not isinstance(repo_content, list):
        print("Unexpected response format. Please check the URL and try again.")
        return None, None, None, None

    return raw_base_url, username, repo_name, repo_content

def main():
    repo_url = input("Enter the GitHub repository URL: ")

    raw_base_url, username, repo_name, repo_content = download_github_repo_content(repo_url)

    if repo_content is None:
        return

    project_file_name = f"{repo_name}.txt"

    with open(project_file_name, "w") as project_file:
        for item in repo_content:
            if item["type"] == "file" and item["name"].endswith(".py"):
                file_url = f"{raw_base_url}{username}/{repo_name}/main/{item['path']}"
                response = requests.get(file_url)

                if response.status_code == 200:
                    code = response.text
                    project_file.write(f"=== {item['name']} ===\n")
                    project_file.write(code)
                    project_file.write("\n\n")

                    print(f"Code from {item['name']} has been written to {project_file_name}")
                else:
                    print(f"Error downloading {item['name']}")

if __name__ == "__main__":
    main()
