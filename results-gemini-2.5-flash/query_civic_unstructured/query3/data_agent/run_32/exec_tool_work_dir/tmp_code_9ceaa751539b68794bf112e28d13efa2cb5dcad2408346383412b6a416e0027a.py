code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_names_raw = set() # Use a set to store unique raw project names

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for line in lines:
        stripped_line = line.strip()
        if 'emergency' in stripped_line.lower() or 'fema' in stripped_line.lower():
            # Basic heuristic for a project name: starts with a capital letter and is not too short
            # Using a raw string literal to avoid issues with backslashes in the regex
            if re.match(r'^[A-Z][a-zA-Z0-9\s&,-_\\']{5,}', stripped_line): # This is where the syntax error likely occurred, let's simplify
                project_names_raw.add(stripped_line)

# Let's simplify the regex for now to avoid the persistent syntax error.
# We will focus on lines containing keywords that also look like titles.

# New approach for extracting project names to avoid regex complexity issues:
# Iterate through lines and identify project-like lines containing the keywords.
project_like_names = set()
project_name_indicators = ["Project", "Improvements", "Plan", "Study", "Repairs", "System", "Road", "Drain", "Wall", "Park", "Facility", "Lane", "Signals", "Power", "Treatment", "Signs", "Emergency", "FEMA", "Recovery", "Center", "Slopes"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')

    for line in lines:
        stripped_line = line.strip()
        line_lower = stripped_line.lower()
        
        # Check if the line contains 'emergency' or 'FEMA'
        if 'emergency' in line_lower or 'fema' in line_lower:
            # Further check if it looks like a project name (starts with capital, reasonable length, contains an indicator word)
            if re.match(r'^[A-Z][a-zA-Z0-9\s&,-_\']{5,}', stripped_line) and any(indicator.lower() in line_lower for indicator in project_name_indicators):
                project_like_names.add(stripped_line)


unique_project_names_cleaned = []
for name_raw in project_like_names:
    # Clean up unicode and smart quotes, ensuring they are valid Python string replacements
    project_name = name_raw.replace('\ufffd', '')
    project_name = project_name.replace('\u2019', "\'")  # Replace smart single quote with escaped single quote
    project_name = project_name.replace('\u201c', '\"\') # Replace smart left double quote with escaped double quote
    project_name = project_name.replace('\u201d', '\"\') # Replace smart right double quote with escaped double quote
    project_name = project_name.replace('\u2013', '-')
    unique_project_names_cleaned.append(project_name)

# Convert to a list of dictionaries for the next step
project_names_for_funding_query = [{'Project_Name': name} for name in sorted(list(set(unique_project_names_cleaned)))]

print("__RESULT__:")
print(json.dumps(project_names_for_funding_query, ensure_ascii=False))"""

env_args = {'var_function-call-12540492671589378295': 'file_storage/function-call-12540492671589378295.json'}

exec(code, env_args)
