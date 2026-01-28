code = """import json
import re

# Load the data from the files
with open('var_functions.query_db:8', 'r') as f:
    funding_data = json.load(f)

with open('var_functions.query_db:14', 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(funding_data), 'funding records')
print('Loaded', len(civic_docs), 'civic documents')

# Build funding lookup dictionary
funding_lookup = {}
for item in funding_data:
    name = item.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(item.get('Amount', 0))

# Find all projects in civic documents that mention Spring 2022
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for project names followed by Spring 2022 dates
    # Pattern: Project name on one line, then schedule info with 2022
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
            
        # Skip headers and footers
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in ['page', 'agenda item', 'public works commission', 'capital improvement projects']):
            continue
            
        # Skip schedule lines
        if any(phrase in line_lower for phrase in ['updates:', 'project schedule:', 'complete design:', 'advertise:', 'begin construction:', 'estimated schedule:']):
            continue
            
        # Look for lines that appear to be project names
        # (Title case or mixed case, not bullet points, reasonable length)
        if (not line.startswith(('(', '-', '•', '·')) and 
            (line.istitle() or (sum(1 for c in line if c.isupper()) >= 3 and not line.isupper()))):
            
            # Look ahead for Spring 2022 mentions
            has_spring_2022 = False
            for j in range(i, min(i+15, len(lines))):
                context_line = lines[j].strip()
                
                # Check for 2022 with Spring or March/April/May
                if '2022' in context_line:
                    if any(indicator in context_line for indicator in ['Spring', 'March', 'April', 'May']) or \
                       any('2022-' + month in context_line for month in ['03', '04', '05']):
                        has_spring_2022 = True
                        break
            
            if has_spring_2022:
                spring_2022_projects.append(line)

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

print('Found potential Spring 2022 projects:', len(spring_2022_projects))
for proj in spring_2022_projects:
    print('-', proj)

# Match with funding and sum
matched_projects = []
total_funding = 0

for project_name in spring_2022_projects:
    # Direct exact match
    if project_name in funding_lookup:
        amount = funding_lookup[project_name]
        total_funding += amount
        matched_projects.append({'name': project_name, 'funding': amount})
    else:
        # Try partial match - look for project name within funding name or vice versa
        for fund_name, amount in funding_lookup.items():
            # Only match if project name is substantial (>15 chars) to avoid false positives
            if len(project_name) > 15:
                if (project_name.lower() in fund_name.lower() or fund_name.lower() in project_name.lower()):
                    total_funding += amount
                    matched_projects.append({'name': project_name, 'matched_fund': fund_name, 'funding': amount})
                    break

# Also include projects with '2022' in their funding name (strong indicator)
additional_2022_projects = []
for fund_name, amount in funding_lookup.items():
    if '2022' in fund_name and amount > 0:
        # Check if not already counted
        if not any(p['name'] == fund_name for p in matched_projects):
            additional_2022_projects.append({'name': fund_name, 'funding': amount})
            total_funding += amount

# Combine all
all_projects = matched_projects + additional_2022_projects

print('\nFinal matched projects:', len(all_projects))
for p in all_projects:
    print('-', p['name'], ': $', p['funding'])

result = {
    'project_count': len(all_projects),
    'total_funding': total_funding,
    'projects': all_projects
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:38': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:40': [], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': []}

exec(code, env_args)
