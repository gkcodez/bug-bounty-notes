import re
from pathlib import Path

# Define paths for each file and the README
files_to_check = {
    "Bandit": "practice/ctfs/over-the-wire/01.bandit.md",
    "Natas": "practice/ctfs/over-the-wire/02.natas.md",
    "SQL injection": "/practice/labs/portswigger/01.sql-injection.md"
}
readme_path = Path("README.md")

def count_checked_items(file_path):
    """Count checked items (marked as - [x]) in the given markdown file."""
    with open(file_path, "r") as file:
        content = file.read()
    return len(re.findall(r"- \[x\]", content))

def update_readme():
    # Read the README content
    with open(readme_path, "r") as file:
        readme_content = file.readlines()

    # Update the table in the README
    updated_content = []
    for line in readme_content:
        match = re.match(r"\| \[(.+?)\]\(.+?\) \| (\d+) \| (\d+) \|", line)
        if match:
            name = match.group(1)
            total = match.group(2)
            if name in files_to_check:
                # Count checked items in the corresponding file
                done = count_checked_items(files_to_check[name])
                # Update the line with the new 'Done' count
                line = f"| [{name}]({files_to_check[name]}) | {total} | {done} |\n"
        updated_content.append(line)

    # Write the updated content back to README.md
    with open(readme_path, "w") as file:
        file.writelines(updated_content)

if __name__ == "__main__":
    update_readme()
