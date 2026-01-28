code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-4188935786568154927'], 'r') as f:
    docs = json.load(f)

with open(locals()['var_function-call-4188935786568153704'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
# Ensure Amount is numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
all_project_names = set(funding_df['Project_Name'].unique())

# Helper to find project info
project_metadata = {} # {name: {'type': 'capital'/'disaster', 'start_dates': []}}

# Keywords for disaster
disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster", "Emergency"]

for doc in docs:
    text = doc['text']
    # Normalize text slightly
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check if line is a project name
        # We need to be careful about exact matches vs partial. 
        # The project names in funding list seem clean.
        # But in text, they might be surrounded by whitespace or headers.
        
        # Try to match exact project name
        found_name = None
        if line in all_project_names:
            found_name = line
        else:
            # Check if line is contained in a project name or vice versa? 
            # Given the preview, "2022 Morning View Resurfacing..." is exact.
            pass
            
        if found_name:
            current_project = found_name
            if current_project not in project_metadata:
                project_metadata[current_project] = {'type': 'capital', 'start_dates': [], 'is_disaster': False}
            
            # Check name for disaster cues
            if any(k in current_project for k in ["FEMA", "CalOES", "CalJPIA", "Disaster"]):
                project_metadata[current_project]['is_disaster'] = True
            
            continue
            
        if current_project:
            # We are inside a project block
            # Check for disaster keywords in the text line
            if any(k in line for k in disaster_keywords):
                project_metadata[current_project]['is_disaster'] = True
            
            # Check for Start Date
            # Pattern: "Begin Construction: <Date>"
            # Also handle bullets like (cid:131)
            lower_line = line.lower()
            if "begin construction" in lower_line:
                # Extract the part after :
                parts = line.split(":", 1)
                if len(parts) > 1:
                    date_str = parts[1].strip()
                    project_metadata[current_project]['start_dates'].append(date_str)
            elif "start date" in lower_line: # fallback
                 parts = line.split(":", 1)
                 if len(parts) > 1:
                    date_str = parts[1].strip()
                    project_metadata[current_project]['start_dates'].append(date_str)

# Now filter and sum
total_funding = 0
disaster_projects_found = []

for pname, info in project_metadata.items():
    # Determine if disaster
    is_disaster = info['is_disaster']
    
    # Determine if started in 2022
    started_2022 = False
    for d in info['start_dates']:
        if "2022" in d:
            started_2022 = True
            break
    
    if is_disaster and started_2022:
        # Get funding
        amt = funding_df[funding_df['Project_Name'] == pname]['Amount'].sum()
        total_funding += amt
        disaster_projects_found.append(pname)

result = {
    "total_funding": total_funding,
    "projects": disaster_projects_found
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4188935786568154927': 'file_storage/function-call-4188935786568154927.json', 'var_function-call-4188935786568153704': 'file_storage/function-call-4188935786568153704.json'}

exec(code, env_args)
