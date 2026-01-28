code = """import json
import re

# Load the funding data
funding_file = str(var_functions.query_db:5)
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load the civic docs text data
civic_file = str(var_functions.query_db:6)
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Process funding data
funding_dict = {}
for record in funding_data:
    name = record.get('Project_Name', '')
    if name:
        funding_dict[name] = {
            'Funding_ID': record.get('Funding_ID', ''),
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': int(record.get('Amount', 0))
        }

# Extract projects from civic docs
all_projects = []
for doc in civic_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
        
        # Skip headers
        skip_terms = ['agenda', 'report', 'meeting', 'item', 'to:', 'prepared by:', 'approved by:', 'date:', 'subject:', 'page', 'public works', 'commission', 'recommended action:', 'discussion:']
        if any(term in line.lower()[:50] for term in skip_terms):
            continue
        
        # Look for completed park projects in 2022
        if 'completed' in line.lower() and '2022' in line:
            # Look backwards for project name (usually 1-3 lines before)
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if prev_line and len(prev_line) > 5 and not any(marker in prev_line for marker in ['(', 'cid:', 'Updates:', 'Schedule:', '-']):
                    if any(keyword in prev_line.lower() for keyword in ['park', 'playground']):
                        all_projects.append({
                            'Project_Name': prev_line,
                            'status': 'completed',
                            'year': '2022',
                            'topic': 'park'
                        })
                        break

# Find matching funding records
park_projects_2022 = []
project_names_added = set()

for project in all_projects:
    proj_name = project['Project_Name']
    
    # Direct match
    for fund_name, fund_info in funding_dict.items():
        if (fund_name.lower() == proj_name.lower() or
            fund_name.lower() in proj_name.lower() or
            proj_name.lower() in fund_name.lower()):
            
            if fund_name not in project_names_added:
                park_projects_2022.append({
                    'Project_Name': fund_name,
                    'Funding_Source': fund_info['Funding_Source'],
                    'Amount': fund_info['Amount']
                })
                project_names_added.add(fund_name)
            break

# If no matches found, check funding table for park projects
if not park_projects_2022:
    for fund_name, fund_info in funding_dict.items():
        if any(keyword in fund_name.lower() for keyword in ['park', 'playground', 'bluffs park']):
            # Look for completion mention in civic docs
            for doc in civic_data:
                text = doc.get('text', '')
                if fund_name.lower() in text.lower() and 'completed' in text.lower() and '2022' in text:
                    if fund_name not in project_names_added:
                        park_projects_2022.append({
                            'Project_Name': fund_name,
                            'Funding_Source': fund_info['Funding_Source'],
                            'Amount': fund_info['Amount']
                        })
                        project_names_added.add(fund_name)
                    break

# Calculate total
total_funding = sum(p['Amount'] for p in park_projects_2022)

result = {
    'total_funding': total_funding,
    'project_count': len(park_projects_2022),
    'projects': park_projects_2022
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
