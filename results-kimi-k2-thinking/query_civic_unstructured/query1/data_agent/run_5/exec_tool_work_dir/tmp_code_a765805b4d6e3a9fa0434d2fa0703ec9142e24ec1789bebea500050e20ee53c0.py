code = """import json
import re

# Read data files
funding_file = locals()['var_functions.query_db:0']
with open(funding_file) as f:
    funding_records = json.load(f)

civic_file = locals()['var_functions.query_db:2']
with open(civic_file) as f:
    civic_docs = json.load(f)

# Get funded projects > $50k
capital_funding = {}
for rec in funding_records:
    if rec.get('Amount') and int(rec['Amount']) > 50000:
        capital_funding[rec['Project_Name']] = int(rec['Amount'])

print('Capital projects with funding > $50k:', len(capital_funding))

# Find design status projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Extract design section using simpler approach
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_section = parts[1].split('Capital Improvement Projects (Construction)')[0]
            
            # Split into project blocks
            blocks = design_section.split('\n\n')
            
            for block in blocks:
                block = block.strip()
                if not block or len(block) < 10:
                    continue
                
                # Get first non-empty line
                lines = [l.strip() for l in block.split('\n') if l.strip()]
                for line in lines[:3]:  # Check first 3 lines
                    # Skip if it's not a project name
                    if (line and 'Updates' not in line and 'Schedule' not in line 
                        and not line.startswith('(') and not line.startswith('•')
                        and not line.isupper() and len(line.split()) > 1):
                        design_projects.append(line)
                        break

print('Design status projects:', len(design_projects))

# Match projects
matched = []
seen = set()

# Helper to normalize names
def normalize(name):
    name = re.sub(r'\s*\([^)]*\)$', '', name)  # Remove (FEMA) etc
    name = re.sub(r'\s+(Project|Improvements|Repairs)$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

for design in design_projects:
    design_norm = normalize(design)
    
    for fund_name in capital_funding:
        fund_norm = normalize(fund_name)
        
        if design_norm in fund_norm or fund_norm in design_norm:
            if fund_name not in seen:
                matched.append({
                    'name': fund_name,
                    'amount': capital_funding[fund_name]
                })
                seen.add(fund_name)

print('Final matches:', len(matched))

# Show top matches
for i, m in enumerate(matched[:12]):
    print(f'{i+1}. {m["name"]} - ${m["amount"]}')

result = {'count': len(matched), 'projects': matched[:15]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
