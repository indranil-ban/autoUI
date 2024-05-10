import os


def generate_markdown(directory_path, output_dir):
    print("Preprocessing markdown file generation...")
    remove_if_exists(output_dir)

    for foldername in os.listdir(directory_path):
        folder_path = os.path.join(directory_path, foldername)
        if os.path.isdir(folder_path):
            markdown_content = f"## Component: {foldername}\n\n"
            markdown_content += get_vue_content(folder_path)
            markdown_content += get_stories_content(folder_path)
            markdown_content += get_md_content(folder_path)

            output_file = os.path.join(output_dir, f"{foldername}.md")
            with open(output_file, "w") as markdown_file:
                markdown_file.write(markdown_content)

            print(f"New markdown file {output_file} generated successfully.")

    print("Preprocessing finished.")

def read_file(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        return f.read()

def get_vue_content(folder_path):
    vue_files = [file for file in os.listdir(folder_path) if file.endswith(".vue")]
    if not vue_files:
        return ""
    vue_file_path = os.path.join(folder_path, vue_files[0])
    code_content = read_file(vue_file_path)
    return f"### Code of the file:\n```html\n{code_content}\n```\n\n"

def get_stories_content(folder_path):
    stories_files = [file for file in os.listdir(folder_path) if file.endswith(".stories.js")]
    if not stories_files:
        return "No .stories.js file found in this folder.\n\n"
    stories_file_path = os.path.join(folder_path, stories_files[0])
    code_content = read_file(stories_file_path)
    return f"### Example Usage:\n```javascript\n{code_content}\n```\n\n"

def get_md_content(folder_path):
    md_content = ""
    md_files = [file for file in os.listdir(folder_path) if file.endswith(".md")]
    for md_file in md_files:
        md_file_path = os.path.join(folder_path, md_file)
        md_file_content = read_file(md_file_path)
        md_content += f"### Usage of {md_file}:\n{md_file_content}\n\n"
    return md_content

def remove_if_exists(output_dir):
    if os.path.exists(output_dir):
        print(f"Removing existing files in {output_dir}...")
        for filename in os.listdir(output_dir):
            file_path = os.path.join(output_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    else:
        os.makedirs(output_dir)