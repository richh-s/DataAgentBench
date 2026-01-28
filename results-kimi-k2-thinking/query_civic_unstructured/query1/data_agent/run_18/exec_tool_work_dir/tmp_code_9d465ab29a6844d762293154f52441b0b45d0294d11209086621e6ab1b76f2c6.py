code = """import json

funding_file = var_functions.query_db:58
civic_file = var_functions.query_db:59

with open(funding_file, 'r') as f:
    funding = json.load(f)
with open(civic_file, 'r') as f:
    docs = json.load(f)

# Get funded project names
funded_names = [f['Project_Name'] for f in funding]

# Extract design projects using a simpler text search approach
design_text = ''
for doc in docs:
    text = doc.get('text', '')
    
    # Find design section
    start = text.find('Capital Improvement Projects (Design)')
    if start < 0:
        continue
    
    # Extract until next major section
    after = text[start:]
    end = len(after)
    
    markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
    for marker in markers:
        pos = after.find(marker)
        if pos > 0 and pos < end:
            end = pos
    
    design_text += after[:end]

# Now extract project names from the combined design text
import re

# Find all capitalized lines that look like project names
project_pattern = re.compile(r'\n([A-Z][A-Za-z0-9\s&]{10,80})(?=\n)', re.MULTILINE)
candidates = project_pattern.findall(design_text)

# Clean and filter candidates
projects = []
for cand in candidates:
    clean = cand.strip()
    if len(clean) < 10:
        continue
    if clean.startswith('(') or ':' in clean or 'cid' in clean:
        continue
    if 'Updates' in clean or 'Schedule' in clean or 'Complete Design' in clean:
        continue
    if 'Project' in clean or 'Improvements' in clean or 'Repairs' in clean or 'Master Plan' in clean:
        projects.append(clean)

# Remove duplicates
projects = list(set(projects))

# Match with funded projects
count = 0
for proj in projects:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    
    for fund in funded_names:
        fund_lower = fund.lower()
        
        # Direct match
        if proj_lower in fund_lower or fund_lower in proj_lower:
            count += 1
            break
        
        # Word overlap of 3+ words
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            count += 1
            break

# Output result
result = json.dumps(count)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json'}

exec(code, env_args)
