code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-10835669272488718990'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-10835669272488721645'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

# Helper to clean name
def get_base_name(name):
    # Remove (...) suffixes
    base = re.sub(r'\s*\(.*?\)$', '', name)
    return base.strip()

# Create a mapping of base_name -> list of funding records
base_name_map = {}
for _, row in df_funding.iterrows():
    base = get_base_name(row['Project_Name'])
    if base not in base_name_map:
        base_name_map[base] = []
    base_name_map[base].append(row)

# Combine all text
full_text = "\n".join([d['text'] for d in civic_docs])

matched_projects = []
total_amount = 0
processed_base_names = set()

# Iterate over base names and search in text
for base_name, rows in base_name_map.items():
    if base_name in processed_base_names:
        continue
        
    # Search for base_name in text
    # We want to find the section for this project.
    # Usually it's "Base Name\n...Updates:"
    # We can search for the base_name followed by some newline and "Updates:"
    
    # Simple search
    idx = full_text.find(base_name)
    if idx != -1:
        # Found the name. Extract context (next 1000 chars)
        context = full_text[idx:idx+1000]
        
        # Check start date
        st_match = re.search(r'Begin Construction:\s*([A-Za-z0-9\s]+)', context)
        st = None
        if st_match:
            st = st_match.group(1).split('\n')[0].strip()
            
        # Check disaster type
        is_disaster = False
        
        # Check explicit keywords in name or rows
        # If any of the funding rows have "FEMA", "CalOES", "Disaster", etc. in Project_Name
        for row in rows:
            rn = row['Project_Name'].lower()
            if "fema" in rn or "caloes" in rn or "disaster" in rn:
                is_disaster = True
                break
        
        if not is_disaster:
            # Check context
            c_lower = context.lower()
            if "fema" in c_lower or "caloes" in c_lower or "disaster" in c_lower or "woolsey" in c_lower:
                is_disaster = True
        
        # Check start year 2022
        if st and "2022" in st:
            if is_disaster:
                # Add funding for ALL rows associated with this base_name
                # Because the text describes the project, and the funding table lists multiple sources for it.
                # "What is the total funding for disaster-related projects..."
                
                # Double check: is the text really describing this project?
                # If we matched "Birdview Avenue Improvements", we might be good.
                
                # Sum amounts
                project_total = 0
                for row in rows:
                    project_total += row['Amount']
                    matched_projects.append({
                        "Project_Name": row['Project_Name'],
                        "Amount": row['Amount'],
                        "Start": st
                    })
                total_amount += project_total
                
        processed_base_names.add(base_name)

print("__RESULT__:")
print(json.dumps({
    "matched_projects": matched_projects, 
    "total_amount": total_amount
}, indent=2))"""

env_args = {'var_function-call-10835669272488718990': 'file_storage/function-call-10835669272488718990.json', 'var_function-call-10835669272488721645': 'file_storage/function-call-10835669272488721645.json'}

exec(code, env_args)
