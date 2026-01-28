code = """import json
import re

# Read funding data
funding_file_path = locals()['var_functions.query_db:0']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Get projects with funding > $50,000
funding_dict = {}
for f in funding_data:
    if f.get('Amount') and int(f['Amount']) > 50000:
        funding_dict[f['Project_Name']] = int(f['Amount'])

print('Funding records found:', len(funding_dict))

# Read civic docs
civic_file_path = locals()['var_functions.query_db:2']
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Extract projects with design status
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section - use raw string for regex
    pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Disaster Recovery|$)'
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        section = match.group(1)
        # Split by project blocks
        blocks = re.split(r'\n\s*\n', section)
        
        for block in blocks:
            block = block.strip()
            if not block:
                continue
            
            # Get first line as project name
            lines = [l.strip() for l in block.split('\n') if l.strip()]
            
            for line in lines:
                # Skip metadata lines
                if (line and 'Updates:' not in line and 'Schedule:' not in line 
                    and not line.startswith('(') and not line.startswith('•')
                    and not line.isupper() and len(line) > 5):
                    design_projects.append(line)
                    break

print('Design projects found:', len(design_projects))

# Match by project name
matches = []
seen = set()

# Helper to normalize names
def clean_name(name):
    name = re.sub(r'\s*\([^)]*\)$', '', name)  # Remove suffixes like (FEMA)
    name = re.sub(r'\s+Project$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

for design_proj in design_projects:
    design_clean = clean_name(design_proj)
    
    for fund_name in funding_dict:
        fund_clean = clean_name(fund_name)
        
        # Check if one name contains the other
        if (design_clean in fund_clean or fund_clean in design_clean):
            if fund_name not in seen:
                matches.append({
                    'project_name': fund_name,
                    'amount': funding_dict[fund_name]
                })
                seen.add(fund_name)

print('Matched projects:', len(matches))

# Show some matches
for i, m in enumerate(matches[:10]):
    print(f"{i+1}. {m['project_name']} (${m['amount']})")

result = {
    'count': len(matches),
    'projects': matches[:15]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
