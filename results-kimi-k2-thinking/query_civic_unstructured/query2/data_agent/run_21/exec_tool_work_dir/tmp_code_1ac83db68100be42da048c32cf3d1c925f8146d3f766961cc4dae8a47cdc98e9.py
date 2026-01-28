code = """import json
import re
import os

# Load funding data
funding_path = locals()['var_functions.query_db:10']
civic_path = locals()['var_functions.query_db:11']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

print('Funding records:', len(funding_data))
print('Civic docs:', len(civic_data))

# Filter park-related funding projects
park_funding = [f for f in funding_data if 'park' in f['Project_Name'].lower()]
print('Park funding records:', len(park_funding))

# Find park projects completed in 2022 from civic docs
completed_2022_parks = []

for doc in civic_data:
    text = doc['text'].lower()
    
    # Look for park projects with 2022 completion
    # Pattern: project name containing park and completion in 2022
    if 'park' in text and '2022' in text:
        # Check if it indicates completion
        completion_indicators = ['completed', 'completion', 'complete construction', 'construction was completed']
        if any(indicator in text for indicator in completion_indicators):
            # Extract project names - look for lines with park and completion
            lines = doc['text'].split('\n')
            for line in lines:
                line_lower = line.lower()
                if 'park' in line_lower and '2022' in line_lower:
                    if any(indicator in line_lower for indicator in completion_indicators):
                        completed_2022_parks.append(line.strip())

print('Potential 2022 park completions found:', len(completed_2022_parks))
for i, p in enumerate(completed_2022_parks[:10]):
    print(f'  {i+1}. {p}')

# More detailed extraction - project names and completion status
project_pattern = r'([A-Z][^.]*?Park[^.]*?)(?:\.|\n|$)'

park_projects = []
for doc in civic_data:
    text = doc['text']
    # Find park project sections
    if 'park' in text.lower():
        lines = text.split('\n')
        current_project = None
        
        for i, line in enumerate(lines):
            line_lower = line.lower()
            # Look for project name (usually title case lines containing Park)
            if 'park' in line_lower and len(line.strip()) > 10 and not line.strip().startswith('('):
                # Check if it's likely a project name (has Park and looks like a title)
                if any(word.isupper() or word.istitle() for word in line.split()):
                    current_project = line.strip()
            
            # Look for completion status with 2022
            if current_project and '2022' in line:
                if any(status in line_lower for status in ['completed', 'completion', 'complete construction']):
                    park_projects.append({
                        'project': current_project,
                        'status_line': line.strip(),
                        'completed_2022': True
                    })

print('\nDetailed park projects with 2022 completion:', len(park_projects))
for p in park_projects[:5]:
    print(f"  Project: {p['project']}")
    print(f"  Status: {p['status_line']}")
    print()"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
