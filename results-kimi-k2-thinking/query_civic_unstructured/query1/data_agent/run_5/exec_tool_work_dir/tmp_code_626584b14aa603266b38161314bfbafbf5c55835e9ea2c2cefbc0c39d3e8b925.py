code = """import json

# Load funding data from the file
funding_file = locals()['var_functions.query_db:0']
with open(funding_file) as f:
    funding_list = json.load(f)

# Load civic documents  
civic_file = locals()['var_functions.query_db:2']
with open(civic_file) as f:
    civic_list = json.load(f)

# Find projects with funding > 50000
funding_dict = {}
for item in funding_list:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_dict[item['Project_Name']] = amount

print('Funding records:', len(funding_dict))

# Extract capital projects with design status
design_names = []

for doc in civic_list:
    text = doc.get('text', '')
    
    # Simple string search for design section
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            section = parts[1].split('Capital Improvement Projects (Construction)')[0]
            blocks = section.split('\n\n')
            for block in blocks:
                lines = [line.strip() for line in block.split('\n') if line.strip()]
                if lines:
                    name = lines[0]
                    # Simple filter
                    if name and 'Updates' not in name and 'Schedule' not in name and len(name) > 10:
                        design_names.append(name)

print('Design projects:', len(design_names))

# Simple matching function
def simple_match(name1, name2):
    # Clean names
    n1 = name1.split('(')[0].strip().lower()
    n2 = name2.split('(')[0].strip().lower()
    n1 = n1.replace('project', '').replace('improvements', '').strip()
    n2 = n2.replace('project', '').replace('improvements', '').strip()
    return n1 in n2 or n2 in n1

# Match projects
matches = []
used = set()

for design in design_names:
    for fund_name in funding_dict:
        if fund_name in used:
            continue
        if simple_match(design, fund_name):
            matches.append({'project': fund_name, 'amount': funding_dict[fund_name]})
            used.add(fund_name)

print('Final matches:', len(matches))

# Output result
result = {'count': len(matches), 'projects': matches[:15]}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
