code = """import json
import re

# Load the data files
with open(locals()['var_functions.query_db:0']) as f:
    funding_recs = json.load(f)

with open(locals()['var_functions.query_db:2']) as f:
    civic_docs = json.load(f)

# Filter for funding > $50,000
funding_projects = {}
for rec in funding_recs:
    amt = rec.get('Amount')
    if amt and int(amt) > 50000:
        funding_projects[rec['Project_Name']] = int(amt)

print('Found', len(funding_projects), 'projects with funding > $50k')

# Extract capital projects with design status
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section using string methods
    start_marker = 'Capital Improvement Projects (Design)'
    end_marker = 'Capital Improvement Projects (Construction)'
    
    if start_marker in text:
        start = text.index(start_marker) + len(start_marker)
        end = text.index(end_marker) if end_marker in text[start:] else len(text)
        design_section = text[start:end]
        
        # Split by blank lines to find projects
        blocks = design_section.split('\n\n')
        for block in blocks:
            block = block.strip()
            if len(block) > 20:
                # Look for project name in first non-empty line
                lines = [line.strip() for line in block.split('\n') if line.strip()]
                if lines:
                    name = lines[0]
                    # Filter out non-project names
                    if (name and 'Updates' not in name and 'Schedule' not in name
                        and not name.startswith('(') and not name.startswith('•')
                        and not name.isupper() and len(name) > 5):
                        design_projects.append(name)

print('Design status projects:', len(design_projects))

# Match by project name (normalize first)
def normalize(name):
    # Remove suffixes like (FEMA), (CalJPIA), etc
    name = re.sub(r'\s*\([^)]*\)$', '', name)
    # Remove common endings
    name = re.sub(r'\s+(Project|Improvements|Repairs)$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

matched = []
used = set()

for design_name in design_projects:
    design_clean = normalize(design_name)
    
    for fund_name, amount in funding_projects.items():
        if fund_name in used:
            continue
        fund_clean = normalize(fund_name)
        
        # Check if names match (one contains the other)
        if design_clean in fund_clean or fund_clean in design_clean:
            matched.append({
                'project_name': fund_name,
                'funding': amount,
                'status': 'design',
                'type': 'capital'
            })
            used.add(fund_name)

print('Matched design projects with funding > $50k:', len(matched))

# Show some matches for verification
for i, p in enumerate(matched[:10]):
    print(f"{i+1}. {p['project_name']} - ${p['funding']}")

result = {'count': len(matched), 'projects': matched[:15]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
