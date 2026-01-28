code = """import json
import re

# Read the full results from the stored JSON files
with open('file_storage/functions.query_db:0.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:2.json', 'r') as f:
    civic_docs_data = json.load(f)

# Step 1: Filter funding data for projects related to 'emergency' or 'FEMA'
emergency_fema_projects = []

for record in funding_data:
    project_name = record.get('Project_Name', '').lower()
    funding_source = record.get('Funding_Source', '').lower()
    
    # Check if project is related to emergency/FEMA
    if 'emergency' in project_name or 'fema' in project_name or 'emergency' in funding_source or 'fema' in funding_source:
        emergency_fema_projects.append(record)

# Also include projects with FEMA/CalOES/CalJPIA suffixes
fema_markers = ['(fema project)', '(caloes project)', '(caljpia project)', 'fema/caloes', 'fema']"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_result_type': "<class 'str'>", 'civic_docs_result_type': "<class 'str'>", 'funding_result_preview': 'file_storage/functions.query_db:0.json', 'civic_docs_result_preview': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
