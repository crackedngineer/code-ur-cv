import yaml
import markdown2
from jinja2 import Environment, FileSystemLoader

# Load YAML
with open("resume.yml") as f:
    data = yaml.safe_load(f)
    
# Formatting resume Data
for job in data["work"]:
    job["achievements"] = [
        markdown2.markdown(item) for item in job["achievements"]
    ]

# Load LaTeX template
env = Environment(
    loader=FileSystemLoader("."),
    block_start_string="((*",
    block_end_string="*))",
    variable_start_string="(((",
    variable_end_string=")))",
    comment_start_string="((#",
    comment_end_string="#))",
)
template = env.get_template("template.tex")

# Render
output = template.render(**data)

# Save final LaTeX
with open("output/resume.tex", "w") as f:
    f.write(output)