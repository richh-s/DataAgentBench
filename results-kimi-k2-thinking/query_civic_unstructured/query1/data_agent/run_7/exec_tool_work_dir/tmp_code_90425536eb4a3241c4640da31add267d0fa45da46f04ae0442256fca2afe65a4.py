code = """import json
import re

# Load data
mongo_path = locals().get('var_functions.query_db:10')
if isinstance(mongo_path, str) and '.json' in mongo_path:
    with open(mongo_path, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_path or []

funding_path = locals().get('var_functions.query_db:22')
if isinstance(funding_path, str) and '.json' in funding_path:
    with open(funding_path, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_path or []

print('Loaded {0} documents and {1} funding records'.format(len(mongo_docs), len(funding_records)))

# Simple approach: extract project names from design section
all_design_projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    sections = text.split('Capital Improvement Projects (Design)')
    if len(sections) > 1:
        design_text = sections[1]
        # Find project names (lines that are likely project names)
        for line in design_text.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and not line.startswith('(') and not line.isupper():
                if all(x not in line for x in ['Updates:', 'Schedule:', 'Page', 'Item', 'Public Works', 'Commission', 'Agenda', 'Subject:', 'To:', 'From:', 'Complete Design', 'Advertise', 'Begin Construction', 'Capital Improvement', 'DISCUSSION:', 'RECOMMENDED ACTION']):
                    if line not in all_design_projects:
                        all_design_projects.append(line)

print('Found {0} design project candidates'.format(len(all_design_projects)))

# Build simple funding lookup - just use the exact names
funding_names = set(rec.get('Project_Name', '') for rec in funding_records)
funding_amounts = {rec.get('Project_Name', ''): int(rec.get('Amount', 0)) for rec in funding_records}

# Try to match - check if any funded project name appears in our design list
matched = []
for design_proj in all_design_projects:
    for funded_name in funding_names:
        if len(funded_name) > 10:  # Only match substantial names
            # Check if the funded project is very similar to design project
            a = design_proj.lower().replace('project', '').strip()
            b = funded_name.lower().replace('project', '').strip()
            
            # Calculate word overlap
            a_words = set(a.split())
            b_words = set(b.split())
            
            # Filter out common words
            common = {'road', 'repair', 'repairs', 'improvements', 'and', 'the', 'improvement', 'project'}
            a_key = a_words - common
            b_key = b_words - common
            
            # If they share key words
            if len(a_key.intersection(b_key)) >= 2:
                if funded_name not in [m['name'] for m in matched]:
                    matched.append({
                        'name': funded_name,
                        'amount': funding_amounts[funded_name],
                        'design_name': design_proj
                    })
                    break

print('Final matched count: {0}'.format(len(matched)))

# Create result
result = json.dumps({
    'count': len(matched),
    'sample': matched[:5]
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
