import os

def generate_markdown(directory_path, output_dir):
    print("Preprocessing markdown file generation...")
    remove_if_exists(output_dir)  # Remove existing files in the output directory

    # Iterate over the subfolders
    for foldername in os.listdir(directory_path):
        folder_path = os.path.join(directory_path, foldername)
        if os.path.isdir(folder_path):
            markdown_content = f"## Component: {foldername}\n\n"

            # Search for .stories.js files
            stories_files = [file for file in os.listdir(folder_path) if file.endswith(".stories.js")]
            if stories_files:
                # Take the content of the first .stories.js file found
                with open(os.path.join(folder_path, stories_files[0]), "r") as f:
                    code_content = f.read()
                markdown_content += "### Example Usage:\n```javascript\n" + code_content + "\n```\n\n"
            else:
                markdown_content += "No .stories.js file found in this folder.\n\n"

            # Search for .md files
            md_files = [file for file in os.listdir(folder_path) if file.endswith(".md")]
            if md_files:
                for md_file in md_files:
                    with open(os.path.join(folder_path, md_file), "r") as f:
                        md_content = f.read()
                    markdown_content += f"### Usage of {md_file}:\n{md_content}\n\n"

            # Save the markdown content to a file for this folder
            output_file = os.path.join(output_dir, f"{foldername}.md")
            with open(output_file, "w") as markdown_file:
                markdown_file.write(markdown_content)

            print(f"New markdown file {output_file} generated successfully.")

    print("Preprocessing finished.")

def remove_if_exists(output_dir):
    if os.path.exists(output_dir):
        print(f"Removing existing files in {output_dir}...")
        for filename in os.listdir(output_dir):
            file_path = os.path.join(output_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    else:
        os.makedirs(output_dir)