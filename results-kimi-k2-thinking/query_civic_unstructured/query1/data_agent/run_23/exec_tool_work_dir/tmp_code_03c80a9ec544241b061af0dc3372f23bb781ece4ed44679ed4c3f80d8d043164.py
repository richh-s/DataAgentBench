code = """import json

# Load the data
with open('var_functions.query_db:74', 'r') as f:
    funding_records = json.load(f)

with open('var_functions.query_db:78', 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup
funded_names = {}
for rec in funding_records:
    name = rec.get('Project_Name', '').strip()
    amount = int(rec.get('Amount', 0))
    if name and amount > 50000:
        funded_names[name.lower()] = name

print(f'Funded projects > $50K: {len(funded_names)}')

# Extract design projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    # Find end of section
    end = len(text)
    markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']
    for marker in markers:
        pos = text.find(marker, start + 50)
        if start < pos < end:
            end = pos
    
    section = text[start:end]
    lines = section.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers
        skip_terms = ['cid:', 'Updates:', 'Project Schedule:', 'Page', 'RECOMMENDED ACTION:', 'DISCUSSION:']
        if any(term in line for term in skip_terms):
            continue
        
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        if line[0].isupper() and len(line.split()) >= 2:
            # Verify it's a project
            is_project = False
            for j in range(i+1, min(i+4, len(lines))):
                nxt = lines[j].lower()
                if 'updates:' in nxt or 'project schedule:' in nxt:
                    is_project = True
                    break
            
            if not is_project:
                keywords = ['Project', 'Improvements', 'Drainage', 'Repairs', 'Study', 'Replacement']
                if any(k in line for k in keywords):
                    is_project = True
            
            if is_project and line not in design_projects:
                design_projects.append(line)

print(f'Design projects: {len(design_projects)}')

# Match projects
matches = []
for proj in design_projects:
    proj_key = proj.lower()
    if proj_key in funded_names:
        matches.append(proj)
    else:
        # Fuzzy match
        for fund_key in funded_names:
            if proj_key in fund_key or fund_key in proj_key:
                proj_words = set(proj_key.split())
                fund_words = set(fund_key.split())
                if len(proj_words.intersection(fund_words)) >= 2:
                    matches.append(proj)
                    break

unique_matches = list(set(matches))
print(f'Final matches: {len(unique_matches)}')

result = len(unique_matches)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json'}

exec(code, env_args)
