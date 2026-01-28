code = """import json
import re

# Load data
with open(locals()['var_function-call-5680067546526520620'], 'r') as f:
    civic_data = json.load(f)
    
with open(locals()['var_function-call-10418813875074106507'], 'r') as f:
    funding_data = json.load(f)

text = civic_data[0]['text']

# Extract project names from funding data
funding_projects = [r['Project_Name'] for r in funding_data]

# Helper to normalize names for matching (remove punctuation, lower case)
def normalize(s):
    return re.sub(r'[^\w\s]', '', s).lower().strip()

# Find project occurrences in text
found_projects = {}
lines = text.split('\n')

# Iterate lines to find headers and projects
current_section = "Unknown"
section_headers = ["Capital Improvement Projects", "Disaster Recovery Projects"]

project_context = {}

# Simple parser: Look for project names from the funding list in the text
# This might be slow if list is huge, but it's small (approx 70 records).
# However, exact match might fail if text has "Project" suffix or not.
# Let's try to match lines that look like headers/titles.

# Better approach:
# The text has distinct project blocks starting with the name.
# Names are usually distinct lines.
# We can iterate through the text and when we find a line that matches a funding project (fuzzy or partial), we start capturing context.

# Let's map normalized funding names to real names
norm_funding_map = {normalize(n): n for n in funding_projects}

# Also, some funding names have (FEMA Project). The text might not have that suffix in the header.
# e.g. text: "Corral Canyon Road Bridge Repairs"
# funding: "Corral Canyon Road Bridge Repairs (FEMA Project)"
# So we should match the *base* name.

base_names = {}
for name in funding_projects:
    # Remove parens content for base name check
    base = re.sub(r'\s*\(.*?\)', '', name).strip()
    base_names[normalize(base)] = base

# Iterate through lines
matched_projects = []
current_proj = None
current_proj_text = []

for i, line in enumerate(lines):
    line_clean = line.strip()
    if not line_clean: continue
    
    # Check for section headers
    if "Capital Improvement Projects" in line:
        current_section = line_clean
        continue
    if "Disaster Recovery Projects" in line:
        current_section = line_clean
        continue
        
    # Check if line matches a project name
    norm_line = normalize(line_clean)
    
    # Check exact match with base names
    if norm_line in base_names and len(norm_line) > 5:
        # It's a project header
        if current_proj:
            matched_projects.append({
                "name": current_proj,
                "section": current_section,
                "text": "\n".join(current_proj_text)
            })
        current_proj = base_names[norm_line]
        current_proj_text = []
    else:
        if current_proj:
            current_proj_text.append(line_clean)

# Add last project
if current_proj:
    matched_projects.append({
        "name": current_proj,
        "section": current_section,
        "text": "\n".join(current_proj_text)
    })

print("__RESULT__:")
print(json.dumps(matched_projects[:5])) # Print first 5 to check"""

env_args = {'var_function-call-5680067546526520620': 'file_storage/function-call-5680067546526520620.json', 'var_function-call-10418813875074106507': 'file_storage/function-call-10418813875074106507.json'}

exec(code, env_args)
