import re
from pathlib import Path




# Path to your README file
readme_path = Path("README.md")


def count_checked_items(file_path):
    """Count checked items (marked as - [x]) in the given markdown file."""
    with open(file_path, "r") as file:
        content = file.read()
    checked_items_count = len(re.findall("🟢", content))
    return checked_items_count

def update_readme():
    # Regular expression to match each row in the table
    regex = r"\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|"

    with open(readme_path, "r") as file:
        updated_content = []
        for line in file:
            match = re.match(regex, line)
            if match:
                # Extract relevant information
                name = match.group(1)          # The text in square brackets
                path = match.group(2)          # The link path in parentheses
                total = int(match.group(3))    # Total count
                done = int(match.group(4))     # Done count
                # Count checked items in the corresponding file
                done = count_checked_items(path)
                # Update the line with the new 'Done' count
                line = f"| [{name}]({path}) | {total} | {done} |\n"
                # Store the path with the name as key
            updated_content.append(line)

    # Write the updated content back to README.md
    with open(readme_path, "w") as file:
        file.writelines(updated_content)

if __name__ == "__main__":
    update_readme()
