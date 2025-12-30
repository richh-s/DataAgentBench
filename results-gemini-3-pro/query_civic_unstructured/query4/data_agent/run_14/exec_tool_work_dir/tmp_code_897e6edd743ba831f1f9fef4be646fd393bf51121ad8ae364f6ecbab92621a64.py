code = """import json
import pandas as pd
import re

# Load civic docs
with open(locals()['var_function-call-14257733574021227783'], 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open(locals()['var_function-call-12616807807824493399'], 'r') as f:
    funding_data = json.load(f)
    
funding_df = pd.DataFrame(funding_data)

projects = []

def is_spring_2022(date_str):
    if not date_str:
        return False
    ds = date_str.lower()
    if 'spring 2022' in ds or 'spring, 2022' in ds:
        return True
    # Check for months in 2022
    if '2022' in ds:
        if any(m in ds for m in ['march', 'april', 'may']):
            return True
        # Check numerical dates 03/2022, 04/2022, 05/2022, 3/2022, etc
        # Patterns like 03-22 or 03/22 might be ambiguous, but usually full year is used
        if re.search(r'\b0?3[-/]\d{0,2}2022', ds) or re.search(r'\b0?4[-/]\d{0,2}2022', ds) or re.search(r'\b0?5[-/]\d{0,2}2022', ds):
            return True
    return False

# Parsing logic
extracted_projects = {} # Name -> StartDate

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_project = None
    
    # Simple state machine
    # We look for "Updates:" or "Project Description:"
    # The line before (ignoring empty lines) is the project name
    
    # Iterate lines
    # Keep a buffer of recent non-empty lines to identify project name
    
    recent_lines = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check for Project Name indicator
        if 'Updates:' in line or 'Project Description:' in line:
            # The project name is likely the last non-empty line before this
            # Sometimes there is a bullet point (cid:190) or similar
            # In the sample: "2022 Morning View Resurfacing ... \n\n (cid:190) Updates:"
            # The line containing "Updates:" often starts with (cid:190)
            
            # Get the previous line
            if recent_lines:
                possible_name = recent_lines[-1]
                # Cleanup name
                # Remove common noise if any
                if possible_name.lower().startswith("capital improvement projects"):
                    # This is a section header, look back further?
                    if len(recent_lines) > 1:
                        possible_name = recent_lines[-2]
                
                # Check if it looks like a project name (not a date, not a page number)
                if len(possible_name) > 5 and not possible_name.startswith('Page '):
                    current_project = possible_name
        
        # Check for Start Date
        # "Begin Construction: ..."
        if current_project:
            if 'Begin Construction:' in line:
                val = line.split('Begin Construction:', 1)[1].strip()
                extracted_projects[current_project] = extracted_projects.get(current_project, []) + [val]
            elif 'Start:' in line: # Fallback
                val = line.split('Start:', 1)[1].strip()
                extracted_projects[current_project] = extracted_projects.get(current_project, []) + [val]
            # Also check for "Scheduled Start"
            
        recent_lines.append(line)
        if len(recent_lines) > 5:
            recent_lines.pop(0)

# Now filter for Spring 2022
spring_2022_projects = set()

for proj, dates in extracted_projects.items():
    # Check if any date is Spring 2022
    for d in dates:
        if is_spring_2022(d):
            spring_2022_projects.add(proj)

# Match with funding
# Project names might need fuzzy matching or exact matching
# Let's try exact matching first after normalizing spaces
def normalize(s):
    return " ".join(s.split())

spring_2022_projects_norm = {normalize(p) for p in spring_2022_projects}
funding_df['Project_Name_Norm'] = funding_df['Project_Name'].apply(normalize)

# Check overlap
matched_funding = funding_df[funding_df['Project_Name_Norm'].isin(spring_2022_projects_norm)]

# If overlap is low, try fuzzy or substring
# Let's inspect the found project names and the funding names
print("__RESULT__:")
print(json.dumps({
    "found_projects": list(spring_2022_projects),
    "matched_count": len(matched_funding),
    "total_amount": matched_funding['Amount'].sum(),
    "matched_projects": matched_funding['Project_Name'].tolist()
}))"""

env_args = {'var_function-call-1020154492988582043': 'file_storage/function-call-1020154492988582043.json', 'var_function-call-14257733574021227783': 'file_storage/function-call-14257733574021227783.json', 'var_function-call-12616807807824493399': 'file_storage/function-call-12616807807824493399.json'}

exec(code, env_args)
