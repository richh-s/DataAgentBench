code = """import json
import re

# Load data
with open(locals()['var_function-call-3018582044476684640'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-3018582044476683837'], 'r') as f:
    civic_docs = json.load(f)

completed_park_projects_2022 = []

def is_park_project(name, text_block):
    # Check if 'park' is in name or text block, case insensitive
    content = (name + " " + text_block).lower()
    return "park" in content

def is_completed_in_2022(text_block):
    # Look for patterns indicating completion in 2022
    # Patterns seen: "Construction was completed November 2022", "completed, November 2022"
    # Also "Complete Construction: [Month] 2022"
    
    text_lower = text_block.lower()
    
    # Simple heuristic: if "completed" and "2022" appear close to each other
    # Or "completion" and "2022"
    
    if "2022" in text_lower:
        if "completed" in text_lower or "completion" in text_lower:
            # Check context more closely if needed, but for now let's see matches
            # Regex for "completed ... 2022"
            if re.search(r"completed.*?2022", text_lower) or re.search(r"completion.*?2022", text_lower):
                return True
    return False

# Basic parsing logic
# The text has multiple projects. We need to split them.
# We can look for project names. They seem to be headers.
# A strong signal for a project block is the "(cid:190) Updates:" line.
# We can regex for that.

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    # Normalize some weird characters if possible, but regex handles it
    # Split by double newlines or similar to find potential headers
    
    # Strategy: Find all indices of "(cid:190)" or "Updates:"
    # Actually, let's use the structure seen in preview:
    # Project Name (newline) (cid:190) Updates: ...
    
    # Let's split by the bullet point `(cid:190)` which often starts a section for a project
    # Wait, `(cid:190)` is used for Updates, Project Schedule, Project Description, etc.
    # But usually a Project starts with the Name, then `(cid:190) Updates` or `(cid:190) Project Description`.
    
    # Let's try to split the text into chunks where each chunk corresponds to a project.
    # It seems projects are distinct.
    
    # Regex to find Project Name followed by `(cid:190)`
    # Pattern: ^(Project Name)\n+(cid:190)
    
    # Let's look for lines that are followed by `(cid:190)` lines.
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if "(cid:190)" in line:
            # The line BEFORE this (ignoring empty lines) might be the Project Name
            # Or the line itself contains the header
            
            # Look backwards for project name
            k = i - 1
            while k >= 0 and not lines[k].strip():
                k -= 1
            
            if k >= 0:
                possible_name = lines[k].strip()
                # Check if this name looks like a project name (not too long, not "Discussion", not "Item 4.B")
                if len(possible_name) < 100 and "Item" not in possible_name and "Page" not in possible_name:
                    # Collect text until the next project start
                    # How to find end of project? Maybe next line that looks like a project name or end of file
                    # Or simpler: Extract text associated with this project name in this vicinity
                    
                    # Let's grab a chunk of lines starting from i until we hit a new project name or end
                    # This is tricky without a perfect parser.
                    # Alternative: Sliding window.
                    
                    # Let's aggregate all text belonging to `possible_name`
                    # We can assume the text following the name until the next name is the description.
                    
                    # We need a list of all start indices of projects.
                    pass

# Better approach:
# Regex to find all starts: `\n([^\n]+)\n+\(cid:190\)`
# This matches a line (Group 1) followed by newlines and then the bullet.
# We iterate over these matches.

    matches = list(re.finditer(r'\n([^\n]+)\n+(?=\(cid:190\))', text))
    
    for j, match in enumerate(matches):
        name = match.group(1).strip()
        start_idx = match.end()
        
        if j < len(matches) - 1:
            end_idx = matches[j+1].start()
            block = text[start_idx:end_idx]
        else:
            block = text[start_idx:]
            
        # Clean name
        # Sometimes name might be "Updates:" if logic fails.
        # But the regex `(?=\(cid:190\))` ensures we are looking at something followed by the bullet.
        # The bullet line usually starts with `(cid:190) Updates` or `(cid:190) Project Description`.
        
        # Filter out common false positives if any
        if name.lower() in ["updates", "project schedule", "discussion", "recommended action"]:
            continue
            
        # Check extraction
        extracted_projects.append({
            "name": name,
            "text": block
        })

# Now filter and sum
relevant_names = []
for p in extracted_projects:
    if is_park_project(p['name'], p['text']):
        if is_completed_in_2022(p['text']):
            relevant_names.append(p['name'])

# Match with funding
total_amount = 0
matched_projects = []

for record in funding_data:
    p_name = record['Project_Name']
    amt = int(record['Amount'])
    
    # Exact match?
    if p_name in relevant_names:
        total_amount += amt
        matched_projects.append(p_name)
    else:
        # Try stripping whitespace or partial match if needed
        # The prompt says names match.
        pass

# Remove duplicates from relevant_names if same project appears in multiple docs?
# Or funding is per project? Funding table has unique funding records?
# "This table contains funding records for various projects."
# Funding_ID is unique.
# If a project is listed multiple times in docs, we just identify it as completed in 2022.
# We should only sum the funding for that project once?
# Or sum all funding records for that project name.
# The `funding_data` might have multiple entries for the same project?
# Let's check if project names are unique in funding or if we should sum all matching rows.
# "This table contains funding records... Fields: Funding_ID, Project_Name..."
# A project might have multiple funding sources. So we sum all records matching the name.

# So we need a set of unique target project names.
unique_target_names = set(relevant_names)

final_sum = 0
found_projects = []

for record in funding_data:
    if record['Project_Name'] in unique_target_names:
        final_sum += int(record['Amount'])
        found_projects.append(record['Project_Name'])

print("__RESULT__:")
print(json.dumps({"total_funding": final_sum, "projects": list(set(found_projects))}))"""

env_args = {'var_function-call-3018582044476684640': 'file_storage/function-call-3018582044476684640.json', 'var_function-call-3018582044476683837': 'file_storage/function-call-3018582044476683837.json'}

exec(code, env_args)
