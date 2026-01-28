code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file) as f:
    funding_records = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file) as f:
    civic_documents = json.load(f)

# Step 1: Filter funding > $50,000
funding_dict = {}
for rec in funding_records:
    amount = int(rec.get('Amount', 0))
    if amount > 50000:
        funding_dict[rec['Project_Name']] = amount

print('Projects with funding > $50k count:', len(funding_dict))

# Step 2: Extract design status projects
design_project_list = []

for doc in civic_documents:
    text = doc.get('text', '')
    
    # Simple string find to locate design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start > 0:
        construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
        if construction_start < 0:
            construction_start = len(text)
        section = text[design_start:construction_start]
        
        # Split by double newlines
        parts = section.split('\n\n')
        for part in parts:
            part = part.strip()
            if len(part) > 15 and 'Design)' not in part:
                # Get first line
                lines = [line.strip() for line in part.split('\n') if line.strip()]
                if lines:
                    name = lines[0]
                    # Filter
                    valid = True
                    if 'Updates' in name or 'Schedule' in name:
                        valid = False
                    if name.startswith('(') or name.startswith('•'):
                        valid = False
                    if name.isupper():
                        valid = False
                    if len(name) < 8:
                        valid = False
                    if valid:
                        design_project_list.append(name)

print('Design status projects count:', len(design_project_list))

# Step 3: Match by normalized names
def normalize(name):
    # Basic cleaning
    if '(' in name:
        name = name.split('(')[0]
    name = name.replace('Project', '').replace('Improvements', '').replace('Repairs', '')
    return name.strip().lower()

matched = []
seen = set()

for dname in design_project_list:
    dclean = normalize(dname)
    for fund_name in funding_dict:
        if fund_name in seen:
            continue
        fclean = normalize(fund_name)
        if dclean in fclean or fclean in dclean:
            matched.append({
                'project_name': fund_name,
                'funding': funding_dict[fund_name],
                'type': 'capital',
                'status': 'design'
            })
            seen.add(fund_name)

print('Matched count:', len(matched))

# Sample
for i, p in enumerate(matched[:10]):
    print(f"{i+1}. {p['project_name']} - ${p['funding']}")

result = {'count': len(matched), 'projects': matched[:15]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
