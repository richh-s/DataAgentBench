code = """import json
import pandas as pd
import re

# Load Funding Data
with open(locals()['var_function-call-4014968237340428108'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
project_names = set(funding_df['Project_Name'].unique())

# Load Civic Docs
with open(locals()['var_function-call-4014968237340429633'], 'r') as f:
    civic_docs = json.load(f)

# Helper function to check for "park" topic
def is_park_project(text, project_name):
    keywords = ['park', 'playground', 'recreation']
    text_lower = text.lower()
    name_lower = project_name.lower()
    for kw in keywords:
        if kw in name_lower or kw in text_lower:
            return True
    return False

# Helper to find completion date in 2022
def check_completion_2022(text):
    # Pattern to find "completed" followed closely by a date in 2022
    # e.g. "Construction was completed November 2022"
    # or "completed, January 2023" (not 2022)
    
    # We look for "completed" and "2022" in the same sentence or line
    # Or "Status: Completed" and "Date: ... 2022"
    
    text_lower = text.lower()
    
    if "completed" in text_lower and "2022" in text_lower:
        # Simple heuristic: if both appear in the text block associated with the project
        # But we must be careful not to pick up future dates like "expected completed 2022" if it's currently 2021?
        # The prompt implies we are looking for "completed in 2022".
        
        # Let's look for specific patterns
        # "completed November 2022"
        # "completed in 2022"
        
        # Regex for "completed" ... "2022"
        if re.search(r"completed.*?2022", text_lower, re.DOTALL):
            return True
            
    return False

identified_projects = []

for doc in civic_docs:
    text = doc['text']
    # Split text into lines to process somewhat sequentially
    lines = text.split('\n')
    
    current_project = None
    current_project_buffer = []
    
    for line in lines:
        line_clean = line.strip()
        
        # Check if line is a project name
        # We use strict matching against the funding DB project names to be safe, 
        # or maybe fuzzy matching if needed. Let's try strict first.
        # Some names in text might have extra chars or be uppercased.
        
        found_name = None
        for name in project_names:
            if name.lower() == line_clean.lower():
                found_name = name
                break
            # Startswith check for names with subtitles like (FEMA Project) in text but not in list?
            # Actually funding list has those suffixes.
            if line_clean.lower().startswith(name.lower()) and len(line_clean) < len(name) + 5:
                found_name = name
                break
        
        if found_name:
            # Save previous project info
            if current_project:
                full_text = "\n".join(current_project_buffer)
                identified_projects.append({
                    'Project_Name': current_project,
                    'text': full_text
                })
            
            # Start new project
            current_project = found_name
            current_project_buffer = []
        
        if current_project:
            current_project_buffer.append(line_clean)
            
    # Don't forget the last one
    if current_project:
        full_text = "\n".join(current_project_buffer)
        identified_projects.append({
            'Project_Name': current_project,
            'text': full_text
        })

# Now filter identified projects
park_projects_2022 = []

for proj in identified_projects:
    name = proj['Project_Name']
    text = proj['text']
    
    # Check topic
    if not is_park_project(text, name):
        continue
        
    # Check status and date
    # We want "completed in 2022"
    if check_completion_2022(text):
        park_projects_2022.append(name)

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Calculate funding
total_funding = 0
matched_records = []
for name in park_projects_2022:
    record = funding_df[funding_df['Project_Name'] == name]
    if not record.empty:
        amount = record['Amount'].sum()
        total_funding += amount
        matched_records.append({"name": name, "amount": int(amount)})

result = {
    "identified_park_projects_completed_2022": matched_records,
    "total_funding": int(total_funding)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1448852997668966591': ['civic_docs'], 'var_function-call-1448852997668967958': ['Funding'], 'var_function-call-4014968237340428108': 'file_storage/function-call-4014968237340428108.json', 'var_function-call-4014968237340429633': 'file_storage/function-call-4014968237340429633.json'}

exec(code, env_args)
