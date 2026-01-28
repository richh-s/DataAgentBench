code = """import json

# Load funding data
with open(locals()['var_functions.query_db:0']) as f:
    funding_recs = json.load(f)

# Load civic docs
with open(locals()['var_functions.query_db:2']) as f:
    civic_docs = json.load(f)

# Filter funding > $50,000
funding_map = {}
for rec in funding_recs:
    if rec.get('Amount'):
        amount = int(rec['Amount'])
        if amount > 50000:
            funding_map[rec['Project_Name']] = amount

print('Projects with funding > 50000:', len(funding_map))

# Extract design projects from documents
design_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start >= 0:
        construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
        if construction_start < 0:
            construction_start = len(text)
        
        section = text[design_start:construction_start]
        
        # Split projects
        parts = section.split('\n\n')
        for part in parts:
            part = part.strip()
            if len(part) > 20:
                lines = [line.strip() for line in part.split('\n') if line.strip()]
                if lines:
                    name = lines[0]
                    # Filter obvious project names
                    if (name and 'Updates:' not in name and 'Schedule:' not in name
                        and not name.startswith('(') and not name.startswith('•')
                        and not name.isupper() and len(name) > 10):
                        design_names.append(name)

print('Design projects found:', len(design_names))

# Match by simple name comparison (no regex, to avoid syntax errors)
def clean_name(name):
    # Remove parenthetical suffixes and common words
    name = name.split('(')[0]
    name = name.replace('Project', '').replace('Improvements', '').replace('Repairs', '')
    return name.strip().lower()

matched = []
used = set()

for design in design_names:
    design_clean = clean_name(design)
    
    for fund_name in funding_map:
        if fund_name in used:
            continue
        fund_clean = clean_name(fund_name)
        
        # Check if one contains the other
        if design_clean in fund_clean or fund_clean in design_clean:
            matched.append({
                'project_name': fund_name,
                'amount': funding_map[fund_name]
            })
            used.add(fund_name)

print('Matched projects:', len(matched))

# Show verification
for i, proj in enumerate(matched[:10]):
    print(f"{i+1}. {proj['project_name']} - ${proj['amount']}")

result = {'count': len(matched), 'projects': matched[:15]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
