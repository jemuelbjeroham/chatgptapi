import difflib
from pathlib import Path

def generate_html_diff(file1, file2, output_file):
    # Read the contents of the two files
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        file1_lines = f1.readlines()
        file2_lines = f2.readlines()

    # Get the differences using difflib.unified_diff
    diff = difflib.unified_diff(file1_lines, file2_lines, lineterm='', fromfile=file1.name, tofile=file2.name)

    # Start the HTML document
    html_output = "<html><body><pre style='font-family: monospace;'>\n"

    # Iterate through the diff and add HTML formatting
    for line in diff:
        if line.startswith('-'):
            html_output += f"<span style='color: red;'>{line}</span>\n"
        elif line.startswith('+'):
            html_output += f"<span style='color: green;'>{line}</span>\n"
        elif line.startswith('@'):
            html_output += f"<span style='color: blue;'>{line}</span>\n"
        else:
            html_output += f"{line}\n"

    # End the HTML document
    html_output += "</pre></body></html>"

    # Write the HTML to the output file
    with open(output_file, 'w') as f:
        f.write(html_output)

    print(f"Diff HTML file generated: {output_file}")

def main():
    # Use the current directory
    current_directory = Path.cwd()

    # Define the input file names
    file1_path = current_directory / "precheck.txt"
    file2_path = current_directory / "postcheck.txt"
    output_file_path = current_directory / "diff_output.html"

    # Generate the HTML diff
    generate_html_diff(file1_path, file2_path, output_file_path)

if __name__ == "__main__":
    main()
