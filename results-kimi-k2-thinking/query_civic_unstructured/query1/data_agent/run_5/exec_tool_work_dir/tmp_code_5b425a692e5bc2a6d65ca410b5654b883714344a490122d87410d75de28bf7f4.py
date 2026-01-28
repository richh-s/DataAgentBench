code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:0']
with open(funding_path) as f:
    funding_data = json.load(f)

# Load civic documents  
civic_path = locals()['var_functions.query_db:2']
with open(civic_path) as f:
    civic_data = json.load(f)

# Filter funding > $50k
funding_map = {}
for rec in funding_data:
    if rec.get('Amount'):
        amount = int(rec['Amount'])
        if amount > 50000:
            funding_map[rec['Project_Name']] = amount

print('Funding records > $50k:', len(funding_map))

# Extract design projects from documents
design_list = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Use string find instead of regex to avoid quote issues
    start_pos = text.find('Capital Improvement Projects (Design)')
    if start_pos >= 0:
        end_pos = text.find('Capital Improvement Projects (Construction)', start_pos)
        if end_pos < 0:
            end_pos = len(text)
        section = text[start_pos:end_pos]
        
        # Split projects by double newline
        blocks = section.split('\n\n')
        for block in blocks:
            block = block.strip()
            if len(block) > 20:
                lines = [L.strip() for L in block.split('\n') if L.strip()]
                if lines:
                    name = lines[0]
                    # Filter out non-project names
                    if (name and 'Updates' not in name and 'Schedule' not in name
                        and not name.startswith('(') and not name.startswith('•')
                        and not name.isupper() and len(name.split()) >= 2):
                        design_list.append(name)

print('Design projects found:', len(design_list))

# Match projects
def clean_name(n):
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    n = re.sub(r'\s+(Project|Improvements|Repairs)$', '', n, flags=re.IGNORECASE)
    return n.strip().lower()

matched_projects = []
used_names = set()

for design_name in design_list:
    design_clean = clean_name(design_name)
    
    for fund_name in funding_map:
        if fund_name in used_names:
            continue
        fund_clean = clean_name(fund_name)
        
        # Check substring match
        if design_clean in fund_clean or fund_clean in design_clean:
            matched_projects.append({
                'project_name': fund_name,
                'amount': funding_map[fund_name]
            })
            used_names.add(fund_name)

print('Matched projects:', len(matched_projects))

# Show sample matches
for i, proj in enumerate(matched_projects[:10]):
    print(f"{i+1}. {proj['project_name']} - ${proj['amount']}")

result = json.dumps({'count': len(matched_projects), 'projects': matched_projects[:15]})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
