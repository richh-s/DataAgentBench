code = """import json
import re

# Load data from file paths
civic_docs = json.load(open('/tmp/tmpw8a01a0z.json'))
funding_records = json.load(open('/tmp/tmptjtu3_1d.json'))

print('Loaded {} civic documents and {} funding records'.format(len(civic_docs), len(funding_records)))

# Parse projects from civic documents
projects_with_dates = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for patterns that indicate project completion dates
    # Pattern 1: 'completed' followed by date
    completed_matches = re.finditer(r'completed[^\n]*2022[^\n]*', text, re.IGNORECASE)
    for match in completed_matches:
        line = match.group(0)
        if 'park' in line.lower():
            projects_with_dates.append({'line': line.strip(), 'project_name': 'Unknown'})
    
    # Pattern 2: Project name followed by completion info
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if 'completed' in line.lower() and '2022' in line and 'park' in line.lower():
            projects_with_dates.append({'line': line.strip(), 'project_name': 'Unknown'})

print('Found {} potential park projects completed in 2022'.format(len(projects_with_dates)))

# Show samples
for i, proj in enumerate(projects_with_dates[:5]):
    print('Sample {}: {}'.format(i+1, proj['line'][:100]))

# Create project names list for matching with funding
project_names = []
for proj in projects_with_dates:
    # Try to extract project name from the line
    line = proj['line']
    # Skip very short lines
    if len(line) < 10:
        continue
    # Remove common prefixes/suffixes
    clean_line = line.lower().replace('completed:', '').replace('construction was completed,', '').strip()
    # Extract first few words as potential project name
    words = clean_line.split()
    if len(words) >= 2:
        # Look for park names
        if 'bluffs park' in clean_line:
            project_names.append('Bluffs Park Shade Structure')
        elif 'marie canyon' in clean_line:
            project_names.append('Marie Canyon Green Streets')
        elif 'broad beach' in clean_line:
            project_names.append('Broad Beach Road Water Quality Repair')
        elif 'point dume' in clean_line:
            project_names.append('Point Dume Walkway Repairs')

print('Extracted {} project names'.format(len(project_names)))

# Match with funding records
funding_dict = {f['Project_Name'].lower(): int(f['Amount']) for f in funding_records}

total_funding = 0
matched_projects = []

for name in project_names:
    name_lower = name.lower()
    if name_lower in funding_dict:
        amount = funding_dict[name_lower]
        total_funding += amount
        matched_projects.append({'name': name, 'amount': amount})
        print('Matched: {} - ${}'.format(name, amount))

# Also try partial matching
for f in funding_records:
    f_name = f['Project_Name'].lower()
    if 'park' in f_name:
        # Check if this park project was completed in 2022
        for proj in projects_with_dates:
            if any(keyword in proj['line'].lower() for keyword in ['bluffs park', 'marie canyon', 'broad beach', 'point dume', 'park']):
                if any(keyword in proj['line'].lower() for keyword in ['2022', 'completed']):
                    if f['Project_Name'] not in [p['name'] for p in matched_projects]:
                        amount = int(f['Amount'])
                        total_funding += amount
                        matched_projects.append({'name': f['Project_Name'], 'amount': amount})
                        print('Partial matched: {} - ${}'.format(f['Project_Name'], amount))
                        break

print('\nTotal funding for 2022 completed park projects: ${}'.format(total_funding))
print('\nMatched projects count: {}'.format(len(matched_projects)))

__RESULT__:
result = {'total_funding': total_funding, 'matched_projects': matched_projects, 'status': 'completed'}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
