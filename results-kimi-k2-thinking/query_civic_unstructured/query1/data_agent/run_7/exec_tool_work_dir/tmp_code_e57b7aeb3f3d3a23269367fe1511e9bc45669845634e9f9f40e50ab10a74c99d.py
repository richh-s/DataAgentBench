code = """import json
import re

# Load MongoDB data
mongo_path = locals().get('var_functions.query_db:10')
if isinstance(mongo_path, str) and '.json' in mongo_path:
    with open(mongo_path, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_path or []

# Load funding data  
funding_path = locals().get('var_functions.query_db:22')
if isinstance(funding_path, str) and '.json' in funding_path:
    with open(funding_path, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_path or []

print('Loaded {0} docs, {1} funding records'.format(len(mongo_docs), len(funding_records)))

# Build funding map
funding_map = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    if name:
        funding_map[name] = int(rec.get('Amount', 0))

# Extract projects with their status from MongoDB
project_status = {}

for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Find status sections
    design_start = text.find('Capital Improvement Projects (Design)')
    constr_start = text.find('Capital Improvement Projects (Construction)')
    not_started_start = text.find('Capital Improvement Projects (Not Started)')
    
    # Extract design section
    if design_start > 0:
        end_pos = constr_start if constr_start > design_start else len(text)
        design_section = text[design_start:end_pos]
        
        # Get project names from this section
        lines = [l.strip() for l in design_section.split('\n') if l.strip()]
        for line in lines:
            # Skip noise
            if any(x in line for x in ['Updates:', 'Schedule:', 'Page', 'Item', 'Public Works', 'Commission', 'Agenda', 'Subject:', 'To:', 'From:', 'Complete Design', 'Advertise', 'Begin Construction']):
                continue
            if line.startswith('(') or line.endswith(':') or line.isupper():
                continue
            if len(line) > 8 and 'project' not in line.lower() and 'capital' not in line.lower():
                project_status[line] = 'design'

print('Found {0} project-status mappings'.format(len(project_status)))

# Match with funding
matches = []
for project_name, status in project_status.items():
    if status == 'design':
        # Try to match with funded projects
        proj_words = set(project_name.lower().replace('project', '').split())
        
        for funded_name in funding_map:
            fund_words = set(funded_name.lower().replace('project', '').split())
            
            # Remove common words
            common = {'and', 'road', 'repair', 'repairs', 'improvements', 'the', 'improvement'}
            proj_key = proj_words - common
            fund_key = fund_words - common
            
            # Check overlap
            overlap = proj_key.intersection(fund_key)
            if len(overlap) >= 2:
                if funded_name not in [m['name'] for m in matches]:
                    matches.append({'name': funded_name, 'amount': funding_map[funded_name]})
                break

print('Final matches: {0}'.format(len(matches)))

# Return result
result = json.dumps({'count': len(matches), 'projects': matches[:3]})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
