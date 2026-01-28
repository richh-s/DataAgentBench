code = """import json
import re

# Load data
with open('var_function-call-5363402596982368323.json') as f:
    funding_data = json.load(f)

with open('var_function-call-5363402596982368440.json') as f:
    docs_data = json.load(f)

# Process funding
funded_projects = set()
for item in funding_data:
    try:
        if float(item['Amount']) > 50000:
            funded_projects.add(item['Project_Name'].strip())
    except:
        pass

# Function to extract
def extract_projects(text):
    found = set()
    # Locate section
    # Case insensitive
    text_lower = text.lower()
    start_marker = "capital improvement projects (design)"
    start_idx = text_lower.find(start_marker)
    
    if start_idx == -1:
        return found
    
    # Locate end
    # Next sections
    next_markers = [
        "capital improvement projects (construction)",
        "capital improvement projects (not started)",
        "disaster recovery projects"
    ]
    
    end_idx = len(text)
    for mk in next_markers:
        idx = text_lower.find(mk, start_idx + len(start_marker))
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx + len(start_marker):end_idx]
    
    # Parse lines
    lines = section_text.split('\n')
    for i, line in enumerate(lines):
        sline = line.strip()
        if not sline:
            continue
            
        # Heuristic: A project name line is followed (eventually) by an 'Updates:' block
        # We check the next non-empty line
        is_proj = False
        for j in range(i+1, len(lines)):
            nline = lines[j].strip()
            if not nline:
                continue
            
            # Check for indicators
            # We see "(cid:190) Updates:" or just "Updates:"
            if "Updates:" in nline or "Project Description:" in nline or nline.startswith("(cid:"):
                is_proj = True
            break # Only check the immediate next non-empty line
            
        if is_proj:
            # Clean up the line
            # Remove potential page numbers or headers if they sneaked in?
            # Usually project names don't have "Page X of Y"
            if "Page" in sline and "of" in sline:
                continue
            if "Agenda Item" in sline:
                continue
            found.add(sline)
            
    return found

# Extract
all_extracted = set()
for doc in docs_data:
    all_extracted.update(extract_projects(doc['text']))

# Intersect
matched = all_extracted.intersection(funded_projects)

print(f"DEBUG: Found {len(all_extracted)} design projects: {list(all_extracted)}")
print(f"DEBUG: Found {len(funded_projects)} funded projects > 50k")
print(f"DEBUG: Matches: {list(matched)}")

print("__RESULT__:")
print(json.dumps(len(matched)))"""

env_args = {'var_function-call-5363402596982368323': 'file_storage/function-call-5363402596982368323.json', 'var_function-call-5363402596982368440': 'file_storage/function-call-5363402596982368440.json'}

exec(code, env_args)
