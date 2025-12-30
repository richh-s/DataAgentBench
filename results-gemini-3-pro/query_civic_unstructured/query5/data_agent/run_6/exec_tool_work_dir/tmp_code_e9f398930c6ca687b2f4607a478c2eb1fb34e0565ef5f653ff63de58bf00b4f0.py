code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-12055061757030169906'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

with open(locals()['var_function-call-12055061757030168917'], 'r') as f:
    civic_docs = json.load(f)

def is_disaster_project(name):
    keywords = ["FEMA", "CalJPIA", "CalOES", "Disaster", "Woolsey", "Fire"]
    for k in keywords:
        if k in name:
            return True
    return False

project_names = sorted(funding_df['Project_Name'].unique(), key=len, reverse=True)
projects_info = {}

for doc in civic_docs:
    text = doc['text']
    for pname in project_names:
        if pname in projects_info:
            continue
        
        # Simple string find to avoid regex escaping issues with special chars in project names
        start_idx = text.find(pname)
        if start_idx != -1:
            chunk = text[start_idx:start_idx+2000]
            
            # Regex to find date
            # Pattern: Begin Construction followed by text
            match = re.search(r"Begin Construction[:\s]+(.*?)\n", chunk, re.IGNORECASE)
            
            start_date = None
            if match:
                start_date = match.group(1).strip()
            
            if start_date:
                if "2022" in start_date:
                    p_type = "capital"
                    if is_disaster_project(pname):
                        p_type = "disaster"
                    
                    projects_info[pname] = {
                        "start_date": start_date,
                        "type": p_type
                    }

total_funding = 0
disaster_projects = []

for pname, info in projects_info.items():
    if info["type"] == "disaster":
        amount = float(funding_df[funding_df['Project_Name'] == pname]['Amount'].sum())
        total_funding += amount
        disaster_projects.append({"name": pname, "amount": amount, "date": info["start_date"]})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": disaster_projects}, indent=2))"""

env_args = {'var_function-call-6195825054144325774': ['civic_docs'], 'var_function-call-6195825054144327317': ['Funding'], 'var_function-call-17054451881073245513': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-17054451881073244554': 'file_storage/function-call-17054451881073244554.json', 'var_function-call-12055061757030168917': 'file_storage/function-call-12055061757030168917.json', 'var_function-call-12055061757030169906': 'file_storage/function-call-12055061757030169906.json'}

exec(code, env_args)
