import subprocess

input_file = "resume.tex"
output_file = "resume.md"

try:
    subprocess.run(["pandoc", input_file, "-o", output_file], check=True)
    print(f"Successfully converted {input_file} to {output_file}")
except subprocess.CalledProcessError as e:
    print(f"Conversion failed: {e}")
except FileNotFoundError:
    print("Pandoc not found. Please ensure Pandoc is installed and in your system's PATH.")
