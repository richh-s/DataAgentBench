code = """import json
import re

# Load funding data
with open(locals()['var_function-call-11382907056012316849'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-11382907056012318432'], 'r') as f:
    civic_docs = json.load(f)

# Extract Capital Projects in Design
capital_design_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Normalize text to handle newlines
    lines = text.split('\n')
    
    # Find section
    in_design_section = False
    
    # We need to capture lines that are project names.
    # Pattern seems to be:
    # Project Name
    # (cid:190) Updates: ...
    # So we look for a line, and check if the next non-empty line starts with (cid:190) or similar.
    # However, scanning line by line is safer.
    
    # Markers for sections
    # Using specific strings from the preview
    design_marker = "Capital Improvement Projects (Design)"
    
    # Stop markers
    stop_markers = [
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Disaster Recovery Projects",
        "Agenda Item"
    ]
    
    # Iterate lines
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if design_marker in line:
            in_design_section = True
            i += 1
            continue
            
        if in_design_section:
            # Check for stop markers
            if any(marker in line for marker in stop_markers):
                in_design_section = False
                break
            
            # Identify project name
            # It shouldn't start with special chars
            if not line:
                i += 1
                continue
            
            # Skip bullet points and metadata
            if line.startswith("(cid:") or line.startswith("Page ") or line.startswith("Agenda") or line.startswith("Subject:") or line.startswith("Date prepared:"):
                i += 1
                continue
            
            # Check if it's a date or something small? Project names are usually substantial.
            # Look ahead to see if "Updates:" follows?
            # In the preview:
            # "2022 Morning View ..."
            # "(cid:190) Updates:"
            # So if we find a line, and the next 'content' line starts with bullet, it's a project.
            
            is_project = False
            # Look ahead
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                if not next_line:
                    j += 1
                    continue
                if next_line.startswith("(cid:") or next_line.startswith("Updates:"):
                    is_project = True
                break
            
            if is_project:
                # This line is likely a project name
                # Clean it
                p_name = line.strip()
                # Remove any trailing colons or weird chars? No, looks clean.
                capital_design_projects.add(p_name)
        
        i += 1

# Filter funding
funded_projects = {}
for item in funding_data:
    try:
        amt = float(item['Amount'])
    except:
        amt = 0
    if amt > 50000:
        funded_projects[item['Project_Name']] = amt

# Find matches
matches = []
# We need to match names.
# DB names vs Extracted names.
# Let's try exact match first.
for proj in capital_design_projects:
    if proj in funded_projects:
        matches.append(proj)
    else:
        # Try fuzzy match?
        # Maybe the DB name is a substring or vice versa?
        # Example: "Westward Beach Road Drainage Improvements Project" vs "Westward Beach Road Drainage Improvements"
        # Let's check if the extracted name is in DB keys (or close)
        pass

# Also check for names in DB that are in extracted (reverse check)
# Because "Clover Heights Storm Drain" (DB) vs "Clover Heights Storm Drainage Improvements" (Text)
# The prompt says "Project_Name in the Funding SQLite table matches the project names that can be extracted".
# This implies exact match or very close.
# Let's start with exact matches and print them.

print("__RESULT__:")
print(json.dumps({
    "extracted_projects": list(capital_design_projects),
    "funded_projects_count": len(funded_projects),
    "matches": matches,
    "match_count": len(matches)
}))"""

env_args = {'var_function-call-11382907056012316849': 'file_storage/function-call-11382907056012316849.json', 'var_function-call-11382907056012318432': 'file_storage/function-call-11382907056012318432.json'}

exec(code, env_args)
