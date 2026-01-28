code = """import json, re

# Load data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file) as f:
    funding_recs = json.load(f)

civic_file = locals()['var_functions.query_db:2']
with open(civic_file) as f:
    civic_docs = json.load(f)

# Map funding by project name
funding_by_name = {}
for rec in funding_recs:
    amount = rec.get('Amount')
    if amount and int(amount) > 50000:
        funding_by_name[rec['Project_Name']] = int(amount)

print('Funded projects:', len(funding_by_name))

# Extract design projects
all_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    start_marker = 'Capital Improvement Projects (Design)'
    end_marker = 'Capital Improvement Projects (Construction)'
    
    if start_marker in text:
        start = text.index(start_marker) + len(start_marker)
        end = text.index(end_marker) if end_marker in text else len(text)
        section_text = text[start:end]
        
        # Parse projects
        blocks = section_text.split('\n\n')
        for block in blocks:
            block = block.strip()
            if block and len(block) > 10:
                lines = [l.strip() for l in block.split('\n') if l.strip()]
                if lines:
                    candidate = lines[0]
                    # Filter for actual project names
                    if (len(candidate) > 10 and 'Updates' not in candidate 
                        and 'Schedule' not in candidate and not candidate.startswith('(')
                        and not candidate.startswith('•') and not candidate.isupper()):
                        all_design_projects.append(candidate)

print('Design projects:', len(all_design_projects))

# Normalize and match
def normalize(name):
    name = re.sub(r'\s*\([^)]*\)$', '', name)
    name = re.sub(r'\s+(Project|Improvements|Repairs|Design)$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

matched_results = []
used_names = set()

for design in all_design_projects:
    design_norm = normalize(design)
    
    for fund_name in funding_by_name:
        if fund_name in used_names:
            continue
            
        fund_norm = normalize(fund_name)
        
        # Check substring match
        if design_norm in fund_norm or fund_norm in design_norm:
            matched_results.append({
                'name': fund_name,
                'funding': funding_by_name[fund_name],
                'status': 'design'
            })
            used_names.add(fund_name)

print('Matched:', len(matched_results))

# Show verification
for i, proj in enumerate(matched_results[:8]):
    print(f'{i+1}. {proj["name"]} - ${proj["funding"]}')

outcome = {'count': len(matched_results), 'projects': matched_results[:15]}
print('__RESULT__:')
print(json.dumps(outcome))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
