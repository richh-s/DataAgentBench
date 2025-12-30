code = """import json
import pandas as pd

civic_key = 'var_function-call-620945809164347431'

with open(locals()[civic_key], 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Debug: check potential project lines
        # Look for the marker in next line
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if 'Updates:' in next_line or 'Project Description:' in next_line:
                if line and 'Projects' not in line and 'Page' not in line:
                    projects.append(line)
        i += 1

print("__RESULT__:")
print(json.dumps(projects[:20])) # Print first 20 extracted names"""

env_args = {'var_function-call-12743158555268498599': 'file_storage/function-call-12743158555268498599.json', 'var_function-call-12743158555268500242': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-620945809164347431': 'file_storage/function-call-620945809164347431.json', 'var_function-call-620945809164347688': 'file_storage/function-call-620945809164347688.json', 'var_function-call-2444153523796257528': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000', 'status': 'not started'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000', 'status': 'not started'}]}

exec(code, env_args)
