code = """import json
import re

# Load funding data from the stored file path
funding_file_path = var_functions.query_db:2
with open(funding_file_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents from the stored file path
civic_file_path = var_functions.query_db:32
with open(civic_file_path, 'r') as f:
    civic_documents = json.load(f)

# Build funding map for projects with amount > $50,000
funding_map = {}
for record in funding_records:
    amount = float(record.get('Amount', 0))
    if amount > 50000:
        project_name = record['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', project_name).strip()
        funding_map[project_name] = amount
        funding_map[clean_name] = amount

# Extract capital projects with design status from civic documents
capital_design_projects = set()

for doc in civic_documents:
    text = doc.get('text', '')
    
    # Find the design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Get text up to next major section
    remaining = text[design_start:]
    construction_start = remaining.find('Capital Improvement Projects (Construction)')
    if construction_start > 0:
        design_section = remaining[:construction_start]
    else:
        design_section = remaining
    
    # Extract project names
    for line in design_section.split('\n'):
        line = line.strip()
        if len(line) > 15 and not any(word in line.upper() for word in ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'PAGE', 'AGENDA']) and not any(phrase in line for phrase in ['Updates:', 'Schedule:', 'Capital Improvement Projects']) and not line.startswith('('):
            # Skip disaster projects
            if not any(keyword in line for keyword in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                capital_design_projects.add(line)

# Count matches
matched_count = 0
matched_details = []

for project in capital_design_projects:
    clean_project = re.sub(r'\s*\([^)]*\)\s*$', '', project).strip()
    
    if project in funding_map or clean_project in funding_map:
        matched_count += 1
        amount = funding_map.get(project) or funding_map.get(clean_project, 0)
        matched_details.append({'project': project, 'funding': int(amount)})

# Return the count
result = {'count': matched_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
