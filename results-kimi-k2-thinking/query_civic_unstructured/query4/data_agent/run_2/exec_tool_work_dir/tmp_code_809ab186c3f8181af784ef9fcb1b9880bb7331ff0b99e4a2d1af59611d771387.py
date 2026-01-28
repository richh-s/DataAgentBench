code = """import json
import re
from collections import defaultdict

# Load the funding data
funding_key = 'var_functions.query_db:20'
civic_key = 'var_functions.query_db:21'

# The data is stored as file paths, let's try to access it
import os
import sys

# Since the results are stored as file paths, we need to read them directly
try:
    # Try to read as actual file paths
    with open(funding_key, 'r') as f:
        funding_data = json.load(f)
except:
    # If that doesn't work, check what's in locals()
    funding_data = locals().get(funding_key, [])

try:
    with open(civic_key, 'r') as f:
        civic_docs = json.load(f)
except:
    civic_docs = locals().get(civic_key, [])

print(f"Funding records: {len(funding_data) if isinstance(funding_data, list) else 'Not a list'}")
print(f"Civic documents: {len(civic_docs) if isinstance(civic_docs, list) else 'Not a list'}")

# Inspect the structure
if funding_data and isinstance(funding_data, list):
    print("First funding record:", funding_data[0])
if civic_docs and isinstance(civic_docs, list):
    print("First civic doc keys:", list(civic_docs[0].keys()))
    print("Sample text:", civic_docs[0]['text'][:500])

# If we have data, process it
projects_with_dates = []

if civic_docs and isinstance(civic_docs, list):
    for doc in civic_docs:
        text = doc.get('text', '')
        lines = text.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and headers
            if not line or line.startswith('Page') or line.startswith('Agenda Item'):
                i += 1
                continue
                
            # Look for project names (reasonable length, starts with capital, not a header)
            if (len(line) > 15 and 
                line[0].isupper() and 
                not any(keyword in line.lower() for keyword in ['commission', 'meeting', 'agenda', 'report', 'public works', 'capital improvement', 'disaster recovery', 'discussion'])):
                
                project_name = line
                
                # Check if this is actually a date line or something else
                if re.match(r'^[A-Z][a-z]+\s+\d{4}$', line) or re.match(r'^\d{4}-[A-Z]', line):
                    i += 1
                    continue
                
                start_date = None
                end_date = None
                
                # Scan ahead for date information
                j = i + 1
                while j < min(i + 15, len(lines)):
                    next_line = lines[j].strip()
                    
                    # Look for Spring 2022 specifically
                    if '2022' in next_line and 'Spring' in next_line:
                        if not start_date:
                            start_date = '2022-Spring'
                            break
                    
                    # Also check for months in 2022
                    if '2022' in next_line:
                        if any(month in next_line for month in ['March', 'April', 'May', '03-', '04-', '05-']):
                            start_date = '2022-Spring'
                            break
                    
                    j += 1
                
                # If we found a Spring 2022 date, add the project
                if start_date:
                    projects_with_dates.append({
                        'Project_Name': project_name,
                        'start_date': start_date
                    })
            
            i += 1

print(f"\nFound {len(projects_with_dates)} projects with Spring 2022 start dates:")
for p in projects_with_dates:
    print(f"  - {p['Project_Name']}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json'}

exec(code, env_args)
