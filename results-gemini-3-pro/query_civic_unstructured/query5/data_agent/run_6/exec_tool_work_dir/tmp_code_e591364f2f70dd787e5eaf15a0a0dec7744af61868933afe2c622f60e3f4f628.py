code = """import json
import sqlite3
import pandas as pd
import re

# Load Funding Data
# The result is in a file because it was large.
with open(locals()['var_function-call-12055061757030169906'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Load Civic Docs
with open(locals()['var_function-call-12055061757030168917'], 'r') as f:
    civic_docs = json.load(f)

# Helper function to check if a project is disaster-related based on name
def is_disaster_project(name):
    keywords = ['FEMA', 'CalJPIA', 'CalOES', 'Disaster', 'Woolsey']
    for k in keywords:
        if k in name:
            return True
    return False

# Sort project names by length descending to match longest first
# This helps avoiding matching "Project A" inside "Project A (FEMA)"
project_names = sorted(funding_df['Project_Name'].unique(), key=len, reverse=True)

projects_found = {} # Name -> {start_date: ..., type: ...}

for doc in civic_docs:
    text = doc['text']
    # Normalize text slightly
    # Remove the weird cid characters if possible or just ignore
    # The preview showed (cid:190) etc.
    
    # We want to find where each project appears.
    # Because text is unstructured, let's find all occurrences of all project names
    # and for each occurrence, look ahead for "Begin Construction"
    
    for pname in project_names:
        if pname in projects_found:
            continue # Already found info for this project (assuming consistent info)
            
        # Regex to find project name as a standalone line or significant header
        # Escape pname for regex
        pattern = re.escape(pname)
        # We look for the pname in the text
        # If found, we extract a chunk of text after it to find the date
        
        matches = [m.start() for m in re.finditer(pattern, text)]
        for start_idx in matches:
            # Look at the text following the match, say next 1000 chars
            chunk = text[start_idx:start_idx+2000]
            
            # Find Start Date
            # Pattern for start date: "Begin Construction" or "Start Date"
            # It seems the format is "Begin Construction: <Date>"
            # Also handle the bullets like (cid:131)
            
            date_match = re.search(r'Begin Construction\s*[:\-]?\s*([^\n\r]*)', chunk, re.IGNORECASE)
            start_date = None
            if date_match:
                start_date = date_match.group(1).strip()
            
            # If we didn't find "Begin Construction", maybe "Start Date"
            if not start_date:
                date_match = re.search(r'Start Date\s*[:\-]?\s*([^\n\r]*)', chunk, re.IGNORECASE)
                if date_match:
                    start_date = date_match.group(1).strip()

            # Determine type
            # Check if "Disaster Recovery Projects" header is above this project
            # This is hard to do with just the chunk.
            # But we can check the hints: "Disaster project names often include suffixes..."
            
            p_type = "capital" # default
            if is_disaster_project(pname):
                p_type = "disaster"
            
            # If we found a date, store it. Even if no date, store it to avoid reprocessing if we assume unique names?
            # Actually, we only care if we find a date in 2022.
            
            if start_date:
                projects_found[pname] = {
                    "start_date": start_date,
                    "type": p_type
                }
                break # Found the project info in this doc
        
print("__RESULT__:")
print(json.dumps(projects_found, indent=2))"""

env_args = {'var_function-call-6195825054144325774': ['civic_docs'], 'var_function-call-6195825054144327317': ['Funding'], 'var_function-call-17054451881073245513': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-17054451881073244554': 'file_storage/function-call-17054451881073244554.json', 'var_function-call-12055061757030168917': 'file_storage/function-call-12055061757030168917.json', 'var_function-call-12055061757030169906': 'file_storage/function-call-12055061757030169906.json'}

exec(code, env_args)
