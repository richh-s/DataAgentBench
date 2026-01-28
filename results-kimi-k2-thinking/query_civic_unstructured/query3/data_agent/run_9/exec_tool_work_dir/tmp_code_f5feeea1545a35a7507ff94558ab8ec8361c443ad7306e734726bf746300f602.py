code = """import json
import re

# Load civic documents data
civic_docs_file = open(var_functions.query_db_5)
civic_docs_data = json.load(civic_docs_file)
civic_docs_file.close()

# Load funding data
funding_file = open(var_functions.query_db_6)
funding_data = json.load(funding_file)
funding_file.close()

# Initialize results list
projects_info = []

# Extract FEMA/emergency projects from funding data
fema_projects = []
for record in funding_data:
    project_name = record['Project_Name']
    if re.search(r'FEMA|EMERGENCY', project_name, re.IGNORECASE):
        fema_projects.append({
            'Project_Name': project_name,
            'Funding_Source': record['Funding_Source'],
            'Amount': int(record['Amount'])
        })

print("Found", len(fema_projects), "FEMA/emergency projects in funding database")
for p in fema_projects[:5]:
    print("-", p['Project_Name'])

__RESULT__ = json.dumps(fema_projects[:20])  # Return first 20 as sample"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
