code = """import json
import sqlite3
import pandas as pd
import re

# Load funding data
with open(locals()['var_function-call-1023604252681241279'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

# Load civic docs
with open(locals()['var_function-call-1023604252681243206'], 'r') as f:
    civic_docs = json.load(f)

# Get all known project names to help with parsing
known_projects = set(funding_df['Project_Name'].unique())

# Helper to check if a line looks like a project header
def is_project_header(line, projects):
    line = line.strip()
    # Check exact match or close match
    if line in projects:
        return line
    # Sometimes names in text might differ slightly (case, spaces), but usually they match well in these datasets.
    return None

# Helper to categorize type
def get_project_type(name, section_header):
    name_lower = name.lower()
    if any(x in name_lower for x in ['fema', 'caloes', 'caljpia', 'woolsey', 'disaster']):
        return 'disaster'
    if section_header and 'disaster' in section_header.lower():
        return 'disaster'
    return 'capital'

# Parse docs
project_info = {} # Name -> {st: ..., type: ...}

current_section = ""
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for Section Headers
        if "Capital Improvement Projects" in line:
            current_section = "capital"
        elif "Disaster Recovery Projects" in line:
            current_section = "disaster"
        
        # Check for Project Name
        # We check if the line matches a known project name
        # We need to be careful not to match substrings inside a sentence.
        # Usually project headers are standalone lines.
        
        # Exact match check
        found_project = None
        if line in known_projects:
            found_project = line
        else:
            # Check if line contains a project name and is short (likely a header)
            # but usually exact match is safer with the provided hints.
            pass
            
        if found_project:
            current_project = found_project
            # Initialize info if not exists
            if current_project not in project_info:
                project_info[current_project] = {
                    'type': get_project_type(current_project, current_section),
                    'st': None
                }
            else:
                # Update type if we found a better indicator (e.g. section header)
                if project_info[current_project]['type'] == 'capital' and get_project_type(current_project, current_section) == 'disaster':
                     project_info[current_project]['type'] = 'disaster'
            continue
            
        # If we are inside a project block, look for details
        if current_project:
            # Look for Start Date
            # Patterns: "Begin Construction:", "Construction Start:", "Start Date:", "Estimated Schedule:", "Project Schedule:" followed by "Begin Construction"
            # The preview shows: "(cid:131) Begin Construction: Fall 2023"
            # We can just look for "Begin Construction" or "Start" and then a date.
            
            lower_line = line.lower()
            if "begin construction" in lower_line or "construction start" in lower_line or "start date" in lower_line:
                # Extract date
                # Simple extraction: take the rest of the line
                # or look for year
                match = re.search(r'(20\d\d)', line)
                if match:
                    year = match.group(1)
                    # We store the full string or just the year. The prompt asks for projects starting in 2022.
                    # So identifying the year is crucial.
                    # But wait, "Begin Construction: Fall 2023" -> 2023.
                    # "Begin Construction: November 2022" -> 2022.
                    project_info[current_project]['st'] = year
            
            # Also sometimes the line is just the date if the previous line was "Begin Construction:" (less likely in this format)

# Now filter and sum
total_funding = 0
disaster_projects_found = []

for index, row in funding_df.iterrows():
    p_name = row['Project_Name']
    amount = row['Amount']
    
    # Check if we have info for this project
    if p_name in project_info:
        info = project_info[p_name]
        p_type = info['type']
        st = info['st']
        
        if p_type == 'disaster' and st == '2022':
            total_funding += int(amount)
            disaster_projects_found.append(p_name)
    else:
        # Fallback: if we didn't find it in text, maybe check name for disaster suffix
        # But we can't determine the start date if it's not in text.
        # The prompt implies we need to join with extracted info.
        # If extracted info is missing, we can't confirm start date.
        pass

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": disaster_projects_found}))"""

env_args = {'var_function-call-1023604252681241279': 'file_storage/function-call-1023604252681241279.json', 'var_function-call-1023604252681243206': 'file_storage/function-call-1023604252681243206.json'}

exec(code, env_args)
