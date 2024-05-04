import os
from constants import EMBED

def generate_markdown(directory_path):
    print("Preprocessing markdown file generation...")
    remove_if_exists()
    markdown_content = ""

    # Iterate over the subfolders
    for foldername in os.listdir(directory_path):
        folder_path = os.path.join(directory_path, foldername)
        if os.path.isdir(folder_path):
            markdown_content += f"## Component: {foldername}\n\n"

            # Search for .stories.js files
            stories_files = [
                file for file in os.listdir(folder_path) if file.endswith(".stories.js")
            ]

            if stories_files:
                # Take the content of the first .stories.js file found
                with open(os.path.join(folder_path, stories_files[0]), "r") as f:
                    code_content = f.read()

                # Add the content to the markdown
                markdown_content += (
                    "### Example Usage:\n```javascript\n" + code_content + "\n```\n\n"
                )
            else:
                markdown_content += "No .stories.js file found in this folder.\n\n"

            # Search for .md files
            md_files = [
                file for file in os.listdir(folder_path) if file.endswith(".md")
            ]

            if md_files:
                for md_file in md_files:
                    with open(os.path.join(folder_path, md_file), "r") as f:
                        md_content = f.read()

                    # Add the content to the markdown
                    markdown_content += f"### Usage of {md_file}:\n{md_content}\n\n"

    # Write the markdown content to a file
    with open(EMBED.CONSTANTS.DOCUMENT_FILE_NAME, "w") as markdown_file:
        markdown_file.write(markdown_content)
        print(f"New markdown file {EMBED.CONSTANTS.DOCUMENT_FILE_NAME} generated successfully.")
        print("Preprocessing finished.")


def remove_if_exists():
    normalized_path = os.path.expanduser(os.path.abspath(EMBED.CONSTANTS.DOCUMENT_FILE_NAME))

    if os.path.exists(normalized_path):
        print(f"Older version found of markdown file {EMBED.CONSTANTS.DOCUMENT_FILE_NAME}. Upgrading...")
        # Delete the generated markdown file
        os.remove(EMBED.CONSTANTS.DOCUMENT_FILE_NAME)
    else:
        return
