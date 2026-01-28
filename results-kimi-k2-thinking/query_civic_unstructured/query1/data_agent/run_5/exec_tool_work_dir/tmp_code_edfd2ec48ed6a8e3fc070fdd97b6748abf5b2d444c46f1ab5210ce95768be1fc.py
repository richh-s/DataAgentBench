code = """import json, re

# Load funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file) as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file) as f:
    civic_docs = json.load(f)

# Get projects with amount > 50000
funding_map = {}
for rec in funding_data:
    if rec.get('Amount') and int(rec['Amount']) > 50000:
        funding_map[rec['Project_Name']] = int(rec['Amount'])

print('Funding records:', len(funding_map))

# Extract design projects
design_list = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section header
    design_marker = 'Capital Improvement Projects (Design)'
    construction_marker = 'Capital Improvement Projects (Construction)'
    
    if design_marker in text:
        start = text.index(design_marker)
        end = text.index(construction_marker) if construction_marker in text else len(text)
        design_section = text[start:end]
        
        # Split projects
        blocks = design_section.split('\n\n')
        for block in blocks:
            block = block.strip()
            if len(block) > 10:
                lines = [l.strip() for l in block.split('\n') if l.strip()]
                for line in lines[:3]:
                    if (line and 'Updates' not in line and 'Schedule' not in line 
                        and not line.startswith('(') and not line.startswith('•')
                        and not line.isupper() and len(line.split()) > 2):
                        design_list.append(line)
                        break

print('Design projects:', len(design_list))

# Match projects
def clean(name):
    name = re.sub(r'\s*\([^)]*\)$', '', name)
    name = re.sub(r'\s+(Project|Improvements|Repairs)$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

results = []
seen = set()

for design_proj in design_list:
    design_clean = clean(design_proj)
    
    for fund_name in funding_map:
        fund_clean = clean(fund_name)
        
        if design_clean in fund_clean or fund_clean in design_clean:
            if fund_name not in seen:
                results.append({
                    'project_name': fund_name,
                    'amount': funding_map[fund_name]
                })
                seen.add(fund_name)

print('Matches found:', len(results))

for i, r in enumerate(results[:10]):
    print(f'{i+1}. {r["project_name"]} - ${r["amount"]}')

final = {'count': len(results), 'projects': results[:15]}
print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
