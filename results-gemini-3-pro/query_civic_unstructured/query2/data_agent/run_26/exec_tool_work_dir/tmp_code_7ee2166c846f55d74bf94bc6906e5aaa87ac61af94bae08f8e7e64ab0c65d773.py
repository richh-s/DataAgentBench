code = """import json
import sqlite3
import pandas as pd

# Load previous tool results
civic_docs_path = locals()['var_function-call-14510963906005286500']
funding_path = locals()['var_function-call-14510963906005285081']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
# Ensure Amount is numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Create a set of potential project names for matching
# Normalize by stripping whitespace
known_project_names = set(funding_df['Project_Name'].str.strip())

completed_projects_2022 = []

def is_park_related(name, text):
    # Check if "park" is in name or text (case insensitive)
    keyword = "park"
    if keyword in name.lower():
        return True
    if keyword in text.lower():
        return True
    return False

def check_completion(text):
    # Check for "completed" and "2022"
    # Also handle "complete construction" etc.
    text_lower = text.lower()
    if "completed" in text_lower and "2022" in text_lower:
        return True
    # "Construction was completed November 2022" -> Matches
    # "Complete Construction: April 2023" -> Matches "complete" but not "2022" (if 2023)
    # Be careful not to match "Schedule: Complete ... 2022" if it's a future date in a 2021 doc?
    # But the query asks for projects *that were completed* in 2022.
    # The documents seem to be status reports. "Updates: Construction was completed..." implies it happened.
    # "Project Schedule: Complete Design: Summer 2023" -> Not completed.
    # So look for "Updates" section specifically or "was completed".
    if "was completed" in text_lower and "2022" in text_lower:
        return True
    return False

# Iterate through documents
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    current_section_text = []
    
    for line in lines:
        stripped_line = line.strip()
        
        # Check if this line is a project name
        if stripped_line in known_project_names:
            # If we were processing a project, check it before moving to next
            if current_project:
                full_section_text = " ".join(current_section_text)
                if check_completion(full_section_text):
                    if is_park_related(current_project, full_section_text):
                        completed_projects_2022.append(current_project)
            
            # Start new project
            current_project = stripped_line
            current_section_text = []
        else:
            if current_project:
                current_section_text.append(stripped_line)
    
    # Check the last project in the file
    if current_project:
        full_section_text = " ".join(current_section_text)
        if check_completion(full_section_text):
            if is_park_related(current_project, full_section_text):
                completed_projects_2022.append(current_project)

# Remove duplicates
completed_projects_2022 = list(set(completed_projects_2022))

# Calculate funding
# We sum the funding for the identified project names
# Note: There might be multiple funding records for one project name (different sources)
total_funding = funding_df[funding_df['Project_Name'].isin(completed_projects_2022)]['Amount'].sum()

print("__RESULT__:")
print(json.dumps({
    "completed_park_projects": completed_projects_2022,
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-7656597533557058168': 'file_storage/function-call-7656597533557058168.json', 'var_function-call-7656597533557058431': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14510963906005286500': 'file_storage/function-call-14510963906005286500.json', 'var_function-call-14510963906005285081': 'file_storage/function-call-14510963906005285081.json'}

exec(code, env_args)
