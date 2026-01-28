code = """import json

# Load data from files
with open(var_functions.query_db_2, 'r') as f:
    funding_data = json.load(f)

with open(var_functions.query_db_5, 'r') as f:
    civic_docs = json.load(f)

# Step 1: Get all projects with funding > $50,000
funding_projects = set()
for rec in funding_data:
    if int(rec.get('Amount', 0)) > 50000:
        funding_projects.add(rec.get('Project_Name', ''))

# Step 2: Extract project information from civic documents
# We'll search for patterns that indicate project type and status
project_matches = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    lines = doc.get('text', '').split('\n')
    
    # Look through each line for project indicators
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check if this line looks like a project name
        if (len(line) < 80 and 
            not line.startswith('(') and 
            not any(x in line.lower() for x in ['project schedule', 'updates', 'discussion', 'agenda', 'to:', 'prepared by:', 'date:']) and
            not any(x in line.lower() for x in ['complete design:', 'advertise:', 'begin construction:'])):
            
            # Check subsequent lines for status and type
            subsequent_text = ' '.join(lines[i:i+10]).lower()
            
            has_design = 'design' in subsequent_text
            has_capital = 'capital' in subsequent_text or 'capital improvement' in subsequent_text
            
            if has_design and has_capital:
                project_matches.append(line)

# Step 3: Find intersections between funding and extracted projects
valid_projects = []
for project_name in project_matches:
    if project_name in funding_projects:
        # Find funding details
        for rec in funding_data:
            if rec.get('Project_Name') == project_name and int(rec.get('Amount', 0)) > 50000:
                valid_projects.append({
                    'name': project_name,
                    'amount': int(rec.get('Amount', 0))
                })

# Output results
result = {'count': len(valid_projects), 'projects': valid_projects[:5]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
