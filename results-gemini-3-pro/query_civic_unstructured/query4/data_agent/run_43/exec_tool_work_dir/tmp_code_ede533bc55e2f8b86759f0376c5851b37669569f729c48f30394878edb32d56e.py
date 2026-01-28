code = """import json
import pandas as pd
import re

# Load civic docs
with open(locals()['var_function-call-12607651032579543164'], 'r') as f:
    civic_docs = json.load(f)

# Load funding
with open(locals()['var_function-call-5868675038188901918'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Helper to check if date is Spring 2022
def is_spring_2022(date_str):
    if not date_str:
        return False
    ds = date_str.lower().strip()
    if "spring 2022" in ds:
        return True
    if "2022" in ds:
        if "march" in ds or "april" in ds or "may" in ds:
            return True
        # Check for 2022-03, 2022-04, 2022-05
        if "2022-03" in ds or "2022-04" in ds or "2022-05" in ds:
            return True
    return False

projects = []

for doc in civic_docs:
    text = doc['text']
    # Split text into lines
    lines = text.split('\n')
    
    current_project = None
    
    # Iterate through lines to find projects and dates
    # We look for lines that look like project names followed by Updates or Description
    # We also assume project names are somewhat short and capitalized
    
    # A simple state machine
    # We look for a line that is followed by "(cid:190) Updates:" or "(cid:190) Project Description:" within a few lines
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line is a project name
        # Look ahead
        is_project = False
        # Look ahead 1-3 lines for the marker
        for offset in range(1, 5):
            if i + offset < len(lines):
                next_line = lines[i+offset].strip()
                if "(cid:190) Updates:" in next_line or "(cid:190) Project Description:" in next_line:
                    is_project = True
                    break
        
        if is_project:
            current_project = line
            # Clean project name
            # Sometimes project name is split on two lines?
            # For simplicity, assume one line or take the line that triggered.
            # But wait, looking at the preview:
            # "2022 Morning View Resurfacing & Storm Drain Improvements"
            # "\n\n(cid:190) Updates:"
            # So the line is correct.
            
            # Check for multi-line name?
            # If the previous line was also text and not empty, maybe it's part of the name.
            # But the preview shows blank lines between projects.
            
            # Store project placeholder
            # We will search for start date in the following lines until next project
            projects.append({'name': current_project, 'start_date': None, 'doc': doc['filename']})
            continue
            
        if current_project:
            # Look for start date
            # "(cid:131) Begin Construction: Fall 2023"
            # "Start Date: ..."
            # "Construction Start: ..."
            
            # Regex for start date
            match = re.search(r"Begin Construction:\s*(.*)", line, re.IGNORECASE)
            if not match:
                match = re.search(r"Start Date:\s*(.*)", line, re.IGNORECASE)
            if not match:
                match = re.search(r"Construction Start:\s*(.*)", line, re.IGNORECASE)
            if not match:
                 # Sometimes it's just "Start: ..."
                match = re.search(r"Start:\s*(.*)", line, re.IGNORECASE)
                
            if match:
                # Update the last project
                projects[-1]['start_date'] = match.group(1).strip()
                # We found a date, but keep looking in case there's a better one or we are in a loop
                # Usually one per project.
                
# Now filter projects
matching_projects = []
for p in projects:
    if is_spring_2022(p['start_date']):
        matching_projects.append(p['name'])

# Remove duplicates if any (same project in multiple agendas)
# If a project appears in multiple docs, we might have duplicates.
# We should probably take the unique set of names.
matching_projects = list(set(matching_projects))

# Join with funding
# Normalize names
def normalize(name):
    return re.sub(r'\s+', ' ', name).strip().lower()

matched_funding = []
total_funding = 0

normalized_funding_map = {normalize(row['Project_Name']): row['Amount'] for row in funding_data}

found_projects = []
missing_projects = []

for mp in matching_projects:
    norm_mp = normalize(mp)
    if norm_mp in normalized_funding_map:
        amount = normalized_funding_map[norm_mp]
        total_funding += amount
        found_projects.append({'name': mp, 'amount': amount})
    else:
        # Try fuzzy match or look for substring?
        # The prompt says they match. Maybe punctuation differences.
        # Let's check keys that contain the name
        found = False
        for k, v in normalized_funding_map.items():
            if norm_mp in k or k in norm_mp:
                # Potential match, but be careful
                # e.g. "Project A" vs "Project A (FEMA)"
                # The description says "Disaster project names often include suffixes..."
                # If the funding table has the suffix and the doc has the short name, or vice versa.
                # "The Project_Name in the Funding SQLite table matches the project names that can be extracted from the civic documents"
                # This suggests exact match or very close.
                # Let's try to match "Project Name" with "Project Name (Suffix)"
                if k.startswith(norm_mp) or norm_mp.startswith(k):
                     amount = v
                     total_funding += amount
                     found_projects.append({'name': mp, 'matched_as': k, 'amount': amount})
                     found = True
                     break
        if not found:
            missing_projects.append(mp)

print("__RESULT__:")
print(json.dumps({
    "count": len(found_projects),
    "total_funding": total_funding,
    "projects": found_projects,
    "missing": missing_projects,
    "all_extracted_with_dates": [p for p in projects if p['start_date']]
}))"""

env_args = {'var_function-call-14853737414132312257': ['Funding'], 'var_function-call-14853737414132313422': 'file_storage/function-call-14853737414132313422.json', 'var_function-call-5868675038188901918': 'file_storage/function-call-5868675038188901918.json', 'var_function-call-12607651032579543164': 'file_storage/function-call-12607651032579543164.json'}

exec(code, env_args)
