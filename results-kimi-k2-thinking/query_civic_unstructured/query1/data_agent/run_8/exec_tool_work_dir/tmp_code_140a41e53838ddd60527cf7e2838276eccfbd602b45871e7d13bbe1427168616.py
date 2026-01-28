code = """import json
import re

# Read civic documents from file
civic_file_path = locals()['var_functions.query_db:12']
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Read funding data from file
funding_file_path = locals()['var_functions.query_db:2']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Create a mapping of project names to funding amounts
funding_map = {}
for record in funding_data:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    if amount > 50000:
        funding_map[proj_name] = amount

# Extract project information from civic documents
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_section = None
    
    for line in lines:
        line = line.strip()
        
        # Identify section headers
        if 'Capital Improvement Projects (Design)' in line:
            current_section = 'design'
            continue
        elif 'Capital Improvement Projects (Construction)' in line:
            current_section = 'construction'
            continue
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_section = 'not started'
            continue
            
        # Look for project names
        if current_section and line and len(line) > 10:
            # Skip common patterns
            lower_line = line.lower()
            skip_words = ['updates', 'schedule', 'revised', 'preliminary', 'page', 'complete design']
            if any(word in lower_line for word in skip_words):
                continue
            
            # Skip bullet points
            if line.startswith('(') or line.startswith('Page'):
                continue
            
            # Clean the project name
            clean_name = re.sub(r'\(cid:\d+\)', '', line).strip()
            clean_name = re.sub(r'^[^A-Za-z]*', '', clean_name).strip()
            
            if len(clean_name) > 5 and 'cid:' not in clean_name:
                # Determine project type based on keywords
                proj_type = 'capital'
                if 'FEMA' in clean_name or 'CalOES' in clean_name:
                    proj_type = 'disaster'
                
                projects.append({
                    'name': clean_name,
                    'status': current_section,
                    'type': proj_type
                })

# Find design projects with funding > 50000
design_funded = []
for proj in projects:
    if proj['status'] == 'design':
        for fund_name, amount in funding_map.items():
            if proj['name'] in fund_name or fund_name in proj['name']:
                design_funded.append({
                    'name': fund_name,
                    'funding': amount
                })
                break

# Count unique projects
unique = []
seen = set()
for proj in design_funded:
    if proj['name'] not in seen:
        seen.add(proj['name'])
        unique.append(proj)


result = {"count": len(unique)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'record_count': 276, 'sample_project_names': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 276, 'funding_sample': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
