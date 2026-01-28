code = """import json
import re

# Read civic documents
civic_docs = []
with open('var_functions.query_db:8', 'r') as f:
    for line in f:
        try:
            doc = json.loads(line.strip())
            civic_docs.append(doc)
        except:
            # Handle multi-line JSON entries
            pass

# If above didn't work, try reading as full JSON
if not civic_docs:
    with open('var_functions.query_db:8', 'r') as f:
        content = f.read().strip()
        if content.startswith('['):
            civic_docs = json.loads(content)

# Read funding data
funding_data = []
with open('var_functions.query_db:5', 'r') as f:
    for line in f:
        try:
            record = json.loads(line.strip())
            funding_data.append(record)
        except:
            pass

if not funding_data:
    with open('var_functions.query_db:5', 'r') as f:
        content = f.read().strip()
        if content.startswith('['):
            funding_data = json.loads(content)

print(f'Loaded {len(civic_docs)} civic documents')
print(f'Loaded {len(funding_data)} funding records')

# Create a mapping of project names to funding
funding_map = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_map[proj_name] = amount

print(f'Created funding map with {len(funding_map)} projects')

# Search for park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Look for park-related project names
        if any(keyword in line.lower() for keyword in ['park', 'playground']):
            # Check if this line looks like a project name (not too short, not a heading)
            if (len(line) > 10 and 
                not line.startswith('Capital Improvement') and
                not line.startswith('Disaster Recovery') and
                not line.startswith('Prepared by') and
                not line.startswith('Approved by') and
                not line.startswith('RECOMMENDED') and
                not line.startswith('DISCUSSION') and
                not line.startswith('To:') and
                not line.startswith('Subject:')):
                
                # Look for completion status in surrounding lines
                is_completed_2022 = False
                context_lines = lines[max(0, i-5):min(len(lines), i+10)]
                
                for ctx_line in context_lines:
                    ctx_lower = ctx_line.lower()
                    if ('completed' in ctx_lower or 'completion' in ctx_lower) and '2022' in ctx_line:
                        is_completed_2022 = True
                        break
                
                if is_completed_2022:
                    # Check if this project has funding
                    matched_funding = 0
                    for funded_proj in funding_map:
                        if line.lower() in funded_proj.lower() or funded_proj.lower() in line.lower():
                            matched_funding = funding_map[funded_proj]
                            break
                    
                    park_projects_2022.append({
                        'project_name': line,
                        'funding': matched_funding,
                        'status': 'completed_2022'
                    })

print(f'\nFound {len(park_projects_2022)} park projects completed in 2022')
for proj in park_projects_2022:
    print(f'- {proj["project_name"]}: ${proj["funding"]}')

# Calculate total funding
total_funding = sum(proj['funding'] for proj in park_projects_2022)
print(f'\nTotal funding: ${total_funding}')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
