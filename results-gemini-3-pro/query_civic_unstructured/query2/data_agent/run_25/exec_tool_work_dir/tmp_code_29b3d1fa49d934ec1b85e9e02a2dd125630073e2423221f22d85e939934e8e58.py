code = """import json
import re

# Load data
with open(locals()['var_function-call-7157939871696024413'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-17433077485285005998'], 'r') as f:
    funding_data = json.load(f)

# Combine text from all docs
full_text = "\n".join([doc['text'] for doc in civic_docs])

# Split into lines
lines = full_text.split('\n')

projects = []
current_project = None
current_block = []

# Heuristic to parse projects
# Look for Project Name followed by (cid:190) or Updates
# However, the structure is a bit loose.
# Let's try to identify headers.

# Pattern for bullet points
bullet_pattern = re.compile(r'^\(cid:\d+\)')

# Iterate lines
for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    
    # Check if this line is likely a project name
    # It shouldn't be a bullet point, shouldn't be "Updates:", shouldn't be "Page X of Y"
    # And the next few lines should contain "Updates" or "Project Description" or bullet points
    
    is_header = False
    if not bullet_pattern.match(line) and "Page" not in line and "Agenda Item" not in line:
        # Check next line
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if "(cid:190)" in next_line or "Updates:" in next_line or "Project Description:" in next_line:
                is_header = True
            elif next_line == "":
                 # Sometimes there is an empty line
                 if i + 2 < len(lines):
                     next_next_line = lines[i+2].strip()
                     if "(cid:190)" in next_next_line or "Updates:" in next_next_line or "Project Description:" in next_next_line:
                         is_header = True

    if is_header:
        # Save previous project
        if current_project:
            projects.append({'name': current_project, 'text': "\n".join(current_block)})
        current_project = line
        current_block = []
    else:
        if current_project:
            current_block.append(line)

# Append last project
if current_project:
    projects.append({'name': current_project, 'text': "\n".join(current_block)})

# Analyze projects
completed_park_projects_2022 = []

for p in projects:
    name = p['name']
    text = p['text'].lower()
    
    # Check if park related
    # Query says "park-related". Hints say "topic" contains keywords like "park".
    # I'll check "park" in name or text.
    if "park" in name.lower() or "park" in text:
        # Check status and date
        # Look for "completed" and "2022" in the same context
        if "completed" in text:
            # Try to find the completion sentence
            # Pattern: "completed" ... "2022"
            # or "complete construction" ... "2022"
            
            # Simple check: is "2022" in the text block?
            # And is it associated with completion?
            
            # Let's look for specific phrases like "completed November 2022" or "completed, January 2023"
            # We want 2022.
            
            # Regex for completed date
            # matches: "completed <month> 2022" or "completed, <month> 2022"
            match = re.search(r'completed.*?([a-zA-Z]+)[\s,]+(202\d)', text)
            if match:
                month, year = match.groups()
                if year == '2022':
                    completed_park_projects_2022.append(name)
            else:
                # Check for "Complete Construction: ... 2022"
                match2 = re.search(r'complete construction:.*?([a-zA-Z]+)[\s,]+(202\d)', text)
                if match2:
                    month, year = match2.groups()
                    if year == '2022':
                        completed_park_projects_2022.append(name)

# Normalize names to match funding data
# Funding data has exact names. Extracted names might have extra spaces or slight diffs.
# I'll try to find matches in funding_data

total_funding = 0
matched_projects = []

for cp in completed_park_projects_2022:
    # Try exact match first
    found = False
    for fund in funding_data:
        if fund['Project_Name'].lower().strip() == cp.lower().strip():
            total_funding += int(fund['Amount'])
            matched_projects.append(fund['Project_Name'])
            found = True
            break # Assume one funding record per project? Or multiple? Table description says "Funding table contains funding records... Project names can be joined". 
            # It's safer to sum all matches if multiple sources exist? 
            # But the loop breaks. Let's assume unique matches or sum all.
            # Usually specific project names are unique keys for extraction, but funding might have multiple entries?
            # Funding_ID is unique.
    
    if not found:
        # fuzzy match? 
        # The text extraction might have included punctuation or artifacts.
        # Let's clean the extracted name
        clean_cp = cp.strip()
        for fund in funding_data:
            if fund['Project_Name'].lower() in clean_cp.lower() or clean_cp.lower() in fund['Project_Name'].lower():
                 # Check if string similarity is high?
                 # Or just simple substring if name is distinct enough.
                 # "Bluffs Park Shade Structure" matches "Bluffs Park Shade Structure"
                 if fund['Project_Name'].lower().strip() == clean_cp.lower().strip():
                     # Already handled by exact match above, but maybe spacing was off
                     total_funding += int(fund['Amount'])
                     matched_projects.append(fund['Project_Name'])
                     found = True
                     break

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_projects, "extracted_projects": completed_park_projects_2022}))"""

env_args = {'var_function-call-7157939871696024413': 'file_storage/function-call-7157939871696024413.json', 'var_function-call-17433077485285005998': 'file_storage/function-call-17433077485285005998.json'}

exec(code, env_args)
