code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:0']
with open(funding_path) as f:
    funding_list = json.load(f)

# Load civic documents
civic_path = locals()['var_functions.query_db:2']
with open(civic_path) as f:
    civic_list = json.load(f)

# Create funding map
funding_map = {}
for item in funding_list:
    amt = item.get('Amount')
    if amt and int(amt) > 50000:
        funding_map[item['Project_Name']] = int(amt)

print('Filtered funding records:', len(funding_map))

# Extract design projects from documents
design_projects = []
for doc in civic_list:
    txt = doc.get('text', '')
    
    # Simple section extraction
    design_start = txt.find('Capital Improvement Projects (Design)')
    if design_start > 0:
        construction_start = txt.find('Capital Improvement Projects (Construction)', design_start)
        if construction_start > 0:
            section = txt[design_start:construction_start]
        else:
            section = txt[design_start:]
        
        blocks = section.split('\n\n')
        for block in blocks:
            block = block.strip()
            if block and len(block) > 15:
                lines = [L.strip() for L in block.split('\n') if L.strip()]
                if lines:
                    name = lines[0]
                    if (name and 'Updates' not in name and 'Schedule' not in name 
                        and not name.startswith('(') and not name.startswith('•')
                        and not name.isupper() and len(name.split()) >= 2):
                        design_projects.append(name)

print('Design projects extracted:', len(design_projects))

# Normalize and match
def normalize_name(n):
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    n = re.sub(r'\s+(Project|Improvements|Repairs)$', '', n, flags=re.IGNORECASE)
    return n.strip().lower()

final_matches = []
used_project_names = set()

for dproj in design_projects:
    d_norm = normalize_name(dproj)
    
    for fund_name in funding_map:
        if fund_name in used_project_names:
            continue
        
        f_norm = normalize_name(fund_name)
        
        if d_norm in f_norm or f_norm in d_norm:
            final_matches.append({
                'project_name': fund_name,
                'funding': funding_map[fund_name],
                'type': 'capital',
                'status': 'design'
            })
            used_project_names.add(fund_name)

print('Matched capital design projects:', len(final_matches))

for i, p in enumerate(final_matches[:10]):
    print(f'{i+1}. {p["project_name"]} - ${p["funding"]}')

result_data = {'count': len(final_matches), 'projects': final_matches[:15]}
print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
