code = """import json
import re

# Read the full results from the stored JSON files
with open('file_storage/functions.query_db:0.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:2.json', 'r') as f:
    civic_docs_data = json.load(f)

# Step 1: Identify all emergency/FEMA related funding records
emergency_fema_funding = []

for record in funding_data:
    project_name = record.get('Project_Name', '')
    funding_source = record.get('Funding_Source', '')
    
    project_name_lower = project_name.lower()
    funding_source_lower = funding_source.lower()
    
    # Check for emergency/FEMA indicators
    if (any(keyword in project_name_lower for keyword in ['emergency', 'fema']) or
        any(keyword in funding_source_lower for keyword in ['emergency', 'fema']) or
        any(suffix in project_name_lower for suffix in ['(fema project)', '(caloes project)', '(caljpia project)'])):
        emergency_fema_funding.append(record)

print(f"Found {len(emergency_fema_funding)} emergency/FEMA related funding records")

# Create a lookup dictionary by project name
funding_lookup = {record['Project_Name']: record for record in emergency_fema_funding}

# Display some of the found projects
print("Emergency/FEMA projects found in funding data:")
for i, proj in enumerate(emergency_fema_funding[:10], 1):
    print(f"{i}. {proj['Project_Name']} - {proj['Funding_Source']} - ${proj['Amount']}")

result = {
    'funding_count': len(emergency_fema_funding),
    'sample_projects': emergency_fema_funding[:5]
}

print('__RESULT__')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_result_type': "<class 'str'>", 'civic_docs_result_type': "<class 'str'>", 'funding_result_preview': 'file_storage/functions.query_db:0.json', 'civic_docs_result_preview': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
