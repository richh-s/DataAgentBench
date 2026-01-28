code = """import json
import re
from datetime import datetime

# Get the stored data using locals()
civic_docs_file = locals()['var_functions.query_db:5']
funding_file = locals()['var_functions.query_db:6']

# Read the data
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create a dictionary for funding lookup
funding_lookup = {}
for record in funding_data:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    if proj_name not in funding_lookup:
        funding_lookup[proj_name] = []
    funding_lookup[proj_name].append(amount)

# Helper function to check if a date string indicates Spring 2022
def is_spring_2022(date_str):
    if not date_str or not isinstance(date_str, str):
        return False
    
    # Check if it's 2022
    if '2022' not in date_str:
        return False
    
    # Check for Spring indicators
    spring_indicators = ['spring', 'march', 'april', 'may', '03', '04', '05']
    date_lower = date_str.lower()
    
    for indicator in spring_indicators:
        if indicator in date_lower:
            return True
    
    return False

# Extract project information from civic docs
spring_2022_projects = {}

# Patterns to look for project information
project_patterns = [
    r'([A-Z][^.!?:\n]*?\bProject\b[^.!?:\n]*)',
    r'([A-Z][^.!?:\n]*?\bImprovements\b[^.!?:\n]*)',
    r'([A-Z][^.!?:\n]*?\bRepairs\b[^.!?:\n]*)',
    r'([A-Z][^.!?:\n]*?\bSystem\b[^.!?:\n]*)',
    r'([A-Z][^.!?:\n]*?\bInfrastructure\b[^.!?:\n]*)'
]

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract potential project descriptions
    all_matches = []
    for pattern in project_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        all_matches.extend(matches)
    
    # Look for date patterns near project names
    for match in all_matches:
        # Look for start dates in the surrounding text
        # Try to find date patterns like "2022-Spring", "2022-March", etc.
        date_match = re.search(r'(2022[-\s]?(?:Spring|March|April|May|Mar|Apr|May|03|04|05))', text, re.IGNORECASE)
        if date_match:
            date_str = date_match.group(1)
            if is_spring_2022(date_str):
                # Clean up project name
                proj_name = match.strip()
                if len(proj_name) > 10 and len(proj_name) < 200:  # Reasonable length
                    spring_2022_projects[proj_name] = date_str

# Also create a simpler extraction method - look for lines that contain both project indicators and dates
lines = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines.extend(text.split('\n'))

for line in lines:
    if len(line.strip()) < 10:
        continue
    
    # Check if line mentions a project
    project_indicators = ['project', 'improvements', 'repairs', 'system', 'infrastructure', 'facility']
    has_project = any(indicator in line.lower() for indicator in project_indicators)
    
    # Check for 2022 spring date
    if has_project and is_spring_2022(line):
        # Clean up the line to use as project name
        clean_name = line.strip()
        # Try to find a reasonable project name length
        if len(clean_name) < 150:
            spring_2022_projects[clean_name] = 'found in line'

print('__RESULT__:')
print(json.dumps({
    'total_spring_2022_projects': len(spring_2022_projects),
    'projects': list(spring_2022_projects.keys())[:20],  # Show first 20
    'funding_records_available': len(funding_data)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_docs_sample': "{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\"}}

exec(code, env_args)
