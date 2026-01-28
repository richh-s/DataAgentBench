code = """import json
import re

# Access the civic docs and funding data from the stored variables
civic_docs_str = var_functions.query_db_5
funding_str = var_functions.query_db_6

# Parse the JSON strings
civic_docs_data = json.loads(civic_docs_str)
funding_data = json.loads(funding_str)

print("Civic docs count:", len(civic_docs_data))
print("Funding records count:", len(funding_data))

# Find FEMA/emergency projects in funding data
fema_projects = []
for rec in funding_data:
    pname = rec['Project_Name'].upper()
    if 'FEMA' in pname or 'EMERGENCY' in pname:
        fema_projects.append({
            'Project_Name': rec['Project_Name'],
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount']),
            'Status': 'Unknown'  # Default status
        })

print("\nFound", len(fema_projects), "FEMA/emergency projects")

# Try to extract status from civic docs text
for i, project in enumerate(fema_projects):
    base_name = project['Project_Name'].split(' (')[0]  # Remove parenthetical
    
    for doc in civic_docs_data:
        text = doc['text'].upper()
        if base_name.upper() in text:
            # Look for status indicators in the text
            if 'CONSTRUCTION' in text:
                if 'UNDER CONSTRUCTION' in text or 'BEGIN CONSTRUCTION' in text:
                    project['Status'] = 'Construction'
            elif 'DESIGN' in text and 'COMPLETE DESIGN' in text:
                project['Status'] = 'Design'
            elif 'COMPLETED' in text or 'COMPLETION' in text:
                project['Status'] = 'Completed'
            elif 'NOT STARTED' in text:
                project['Status'] = 'Not Started'
            break

# Output results
__RESULT__ = json.dumps(fema_projects, indent=2)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
