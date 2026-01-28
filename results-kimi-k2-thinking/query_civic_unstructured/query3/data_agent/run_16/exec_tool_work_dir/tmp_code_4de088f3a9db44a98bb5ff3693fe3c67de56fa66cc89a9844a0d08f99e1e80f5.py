code = """import json
import re

# Read the full results from the stored JSON files
with open('file_storage/functions.query_db:0.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:2.json', 'r') as f:
    civic_docs_data = json.load(f)

# Step 1: Identify emergency/FEMA related projects from funding data
emergency_fema_funding = []

for record in funding_data:
    project_name = record.get('Project_Name', '').lower()
    funding_source = record.get('Funding_Source', '').lower()
    
    # Check for emergency/FEMA indicators
    if any(keyword in project_name for keyword in ['emergency', 'fema']) or \
       any(keyword in funding_source for keyword in ['emergency', 'fema']) or \
       any(suffix in project_name for suffix in ['(fema project)', '(caloes project)', '(caljpia project)']):
        emergency_fema_funding.append(record)

# Create a dictionary for easy lookup by project name
funding_dict = {record['Project_Name'].lower(): record for record in emergency_fema_funding}

print(f"Found {len(emergency_fema_funding)} emergency/FEMA related funding records")
print("Sample project names:", [r['Project_Name'] for r in emergency_fema_funding[:5]])
print("__RESULT__:")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_result_type': "<class 'str'>", 'civic_docs_result_type': "<class 'str'>", 'funding_result_preview': 'file_storage/functions.query_db:0.json', 'civic_docs_result_preview': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
