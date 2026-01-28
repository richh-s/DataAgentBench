code = """import json
import re

# Load funding data
with open(locals()['var_function-call-5247396609485473632'], 'r') as f:
    funding_data = json.load(f)

# Create a dictionary of project names to amounts for fast lookup
# Normalize names: strip, lower case for matching
funding_map = {}
for item in funding_data:
    name = item['Project_Name'].strip()
    amount = float(item['Amount'])
    if amount > 50000:
        funding_map[name.lower()] = amount

# Load civic docs
with open(locals()['var_function-call-633765740054289148'], 'r') as f:
    docs = json.load(f)

projects_found = set()

# Helper to normalize text lines
def normalize(text):
    return text.strip().lower()

for doc in docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = None # 'design', 'construction', 'not_started', 'other'
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        # Detect headers
        lower_line = line_clean.lower()
        if "capital improvement projects (design)" in lower_line:
            current_section = 'design'
            continue
        elif "capital improvement projects (construction)" in lower_line:
            current_section = 'construction'
            continue
        elif "capital improvement projects (not started)" in lower_line:
            current_section = 'not_started'
            continue
        elif "disaster recovery projects" in lower_line:
            current_section = 'disaster' # or check specific status
            continue
        
        # If we are in the 'design' section, check if the line is a project name
        if current_section == 'design':
            # Check if this line matches a funded project
            # Simple exact match (case-insensitive)
            # Also consider that the text might be a substring or slightly different
            # But the prompt says "Project_Name in the Funding SQLite table matches the project names that can be extracted"
            
            # Check exact match first
            if lower_line in funding_map:
                projects_found.add(lower_line)
            else:
                # Fuzzy match? Or maybe the line contains the project name?
                # The text output shows "2022 Morning View Resurfacing & Storm Drain Improvements"
                # Let's check if any key in funding_map is in the line
                # But be careful of short matches. Project names seem distinct.
                for funded_name in funding_map.keys():
                    if funded_name == lower_line:
                         projects_found.add(funded_name)
                    # Handle cases where line might have extra chars?
                    # "Project Name" vs "Project Name Project"
                    
print("__RESULT__:")
print(json.dumps(list(projects_found)))"""

env_args = {'var_function-call-5247396609485473632': 'file_storage/function-call-5247396609485473632.json', 'var_function-call-633765740054289148': 'file_storage/function-call-633765740054289148.json'}

exec(code, env_args)
