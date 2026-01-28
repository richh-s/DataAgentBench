code = """import json
import re
from collections import defaultdict

# Load the civic documents data
civic_docs_var = globals()['var_functions_query_db_30']
funding_var = globals()['var_functions_query_db_5']

# Handle the data properly - they might be file paths or direct data
import os
if isinstance(civic_docs_var, str) and os.path.exists(civic_docs_var):
    with open(civic_docs_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_var if isinstance(civic_docs_var, list) else []

if isinstance(funding_var, str) and os.path.exists(funding_var):
    with open(funding_var, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_var if isinstance(funding_var, list) else []

print(f"Loaded {len(civic_docs)} civic documents")
print(f"Loaded {len(funding_data)} funding records")

# Function to extract projects from text
def extract_projects_from_text(text, filename):
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip empty lines and common non-project lines
        if not line or len(line) < 10 or line.startswith('Page '):
            continue
            
        # Look for project names (typically longer, descriptive lines)
        project_indicators = ['Project', 'Improvements', 'Repairs', 'Replacement', 'Facility', 'Road', 'Park', 'Drain', 'Bridge', 'Structure', 'System']
        
        if any(indicator.lower() in line.lower() for indicator in project_indicators):
            # Look ahead for schedule information
            context_window = '\n'.join(lines[i:i+10])
            
            # Check for Spring 2022 start dates
            spring_patterns = [
                r'2022[-\s]Spring', r'Spring[-\s]2022',
                r'2022[-\s](March|April|May)',
                r'(March|April|May)[-\s]2022'
            ]
            
            for pattern in spring_patterns:
                if re.search(pattern, context_window, re.IGNORECASE):
                    # Clean up the project name
                    clean_name = re.sub(r'^(cid:\d+\s*)+', '', line)
                    clean_name = re.sub(r'^[\-\*\•\d\.\s]+', '', clean_name)
                    clean_name = clean_name.strip()
                    
                    if clean_name and len(clean_name) > 10:
                        projects.append({
                            'project_name': clean_name,
                            'filename': filename,
                            'start_date': '2022-Spring'
                        })
                    break
    
    return projects

# Extract all Spring 2022 projects from all documents
all_spring_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    projects = extract_projects_from_text(text, filename)
    all_spring_projects.extend(projects)

# Remove duplicates by project name
unique_projects = {}
for proj in all_spring_projects:
    name = proj['project_name']
    if name not in unique_projects:
        unique_projects[name] = proj

spring_2022_projects = list(unique_projects.values())
print(f"Found {len(spring_2022_projects)} unique Spring 2022 projects")

# Match with funding data
funding_matches = []
for project in spring_2022_projects:
    proj_name = project['project_name'].lower()
    
    # Look for matching funding records
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        
        # Check for direct match or partial match
        if (proj_name in fund_name or fund_name in proj_name or 
            any(word in fund_name for word in proj_name.split() if len(word) > 4)):
            funding_matches.append({
                'project_name': project['project_name'],
                'funding_record_name': fund['Project_Name'],
                'amount': int(fund['Amount']),
                'source': fund['Funding_Source']
            })

# Also check for projects that might have FEMA/CalOES suffixes
def match_with_suffixes(project_name, funding_data):
    matches = []
    suffixes = ['', ' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)', ' (FEMA/CalOES Project)']
    
    for suffix in suffixes:
        test_name = project_name + suffix
        test_name_lower = test_name.lower()
        
        for fund in funding_data:
            if test_name_lower == fund['Project_Name'].lower():
                matches.append(fund)
    
    return matches

# Try more aggressive matching
all_matches = {}
for project in spring_2022_projects:
    proj_name = project['project_name']
    
    # Try exact match first
    exact_matches = [f for f in funding_data if f['Project_Name'].lower() == proj_name.lower()]
    
    if exact_matches:
        all_matches[proj_name] = exact_matches
    else:
        # Try partial matching
        proj_words = proj_name.lower().split()
        # Remove common words
        key_words = [w for w in proj_words if len(w) > 4 and w not in ['project', 'improvements', 'repairs', 'replacement']]
        
        for fund in funding_data:
            fund_name = fund['Project_Name'].lower()
            # Check if key words are present
            if all(word in fund_name for word in key_words[:2]):  # match first 2 key words
                if proj_name not in all_matches:
                    all_matches[proj_name] = []
                all_matches[proj_name].append(fund)

# Calculate total funding
total_funding = 0
matched_projects = []
for project_name, funds in all_matches.items():
    for fund in funds:
        total_funding += int(fund['Amount'])
        matched_projects.append({
            'project': project_name,
            'funding_name': fund['Project_Name'],
            'amount': int(fund['Amount'])
        })

print(f"Matched {len(all_matches)} projects with funding")
print(f"Total funding: ${total_funding:,}")

# Show sample matches
print("\nSample matched projects:")
for i, (proj, funds) in enumerate(list(all_matches.items())[:5]):
    print(f"{i+1}. {proj}")
    for fund in funds:
        print(f"   - {fund['Project_Name']}: ${int(fund['Amount']):,}")

print('__RESULT__:')
print(json.dumps({
    'num_spring_2022_projects': len(spring_2022_projects),
    'total_funding_dollars': total_funding,
    'num_projects_with_funding': len(all_matches),
    'sample_projects': [p['project_name'] for p in spring_2022_projects[:10]]
}, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'civic_count': 5, 'funding_count': 500}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
