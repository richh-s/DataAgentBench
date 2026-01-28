code = """import json
import re

# Load MongoDB data from file path
mongo_path = var_functions.query_db:47
if isinstance(mongo_path, str) and mongo_path.endswith('.json'):
    with open(mongo_path, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = []

print('Mongo docs loaded:', len(mongo_docs))

# Load funding data from file path
funding_path = var_functions.query_db:46
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_recs = json.load(f)
else:
    funding_recs = []

print('Funding records loaded:', len(funding_recs))

# Create funding map of projects > $50k
capital_funding = {}
for rec in funding_recs:
    amount = int(rec.get('Amount', 0))
    name = rec.get('Project_Name', '')
    if amount > 50000 and name:
        capital_funding[name] = amount

print('Funding projects > 50k:', len(capital_funding))

# Extract design projects from MongoDB
design_projects = []

design_section_start = 'Capital Improvement Projects (Design)'
design_section_end = 'Capital Improvement Projects (Construction)'

for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Find design section
    start_idx = text.find(design_section_start)
    if start_idx == -1:
        continue
    
    end_idx = text.find(design_section_end, start_idx)
    if end_idx == -1:
        end_idx = len(text)
    
    design_section = text[start_idx:end_idx]
    lines = [line.strip() for line in design_section.split('\n') if line.strip()]
    
    # Extract project names (filter out noise)
    for line in lines:
        # Skip headers, footers, bullets
        if any(skip in line for skip in ['Updates:', 'Schedule:', 'Page', 'Item', 'Public Works', 'Commission', 'Agenda', 'Subject:', 'To:', 'From:', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Capital Improvement Projects', 'Complete Design', 'Advertise', 'Begin Construction']):
            continue
        if line.startswith('(') or line.endswith(':') or line.isupper():
            continue
        if len(line) > 8 and line not in design_projects:
            design_projects.append(line)

print('Design projects found:', len(design_projects))

# Match design projects with funding
def normalize_project_name(name):
    return name.lower().replace('project', '').strip()

def get_key_words(name):
    words = set(normalize_project_name(name).split())
    common = {'road', 'repair', 'repairs', 'improvements', 'improvement', 'and', 'the', 'drain', 'drainage', 'storm', 'project'}
    return words - common

matched_funding = []
for design_proj in design_projects:
    design_keys = get_key_words(design_proj)
    if not design_keys:
        continue
    
    for funded_name in capital_funding:
        funded_keys = get_key_words(funded_name)
        # Check for overlap of key words
        overlap = design_keys.intersection(funded_keys)
        # Match if at least 2 key words overlap
        if len(overlap) >= 2:
            if funded_name not in [m['funded'] for m in matched_funding]:
                matched_funding.append({
                    'design': design_proj,
                    'funded': funded_name,
                    'amount': capital_funding[funded_name]
                })
                break

print('Matches found:', len(matched_funding))

# Prepare result
result = json.dumps({
    'count': len(matched_funding),
    'matches': matched_funding[:10]
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:47': 'file_storage/functions.query_db:47.json'}

exec(code, env_args)
