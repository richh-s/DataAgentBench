code = """import json

# Load funding data from file
funding_file = 'var_functions.query_db:30'
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents from file
civic_file = 'var_functions.query_db:31'
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create set of funded project names (lowercase)
funded_names = {}
for rec in funding_records:
    try:
        amount = int(rec.get('Amount', 0))
        if amount > 50000:
            name = rec.get('Project_Name', '').strip()
            if name:
                funded_names[name.lower()] = name
    except:
        continue

print('Funding projects > 50K: ' + str(len(funded_names)))

# Extract design projects from civic docs
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Locate design section
    idx1 = text.find('Capital Improvement Projects (Design)')
    if idx1 == -1:
        continue
    
    idx2 = text.find('Capital Improvement Projects (Construction)', idx1)
    idx3 = text.find('Capital Improvement Projects (Not Started)', idx1)
    
    end = len(text)
    if idx2 > idx1:
        end = min(end, idx2)
    if idx3 > idx1:
        end = min(end, idx3)
    
    section = text[idx1:end]
    lines = section.split('\n')
    
    # Extract project names
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        
        if 'cid:' in line or 'Updates:' in line or 'Project Schedule:' in line:
            continue
        
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        if line[0].isupper() and len(line.split()) >= 2:
            # Verify context
            is_valid = False
            for j in range(i+1, min(i+4, len(lines))):
                if 'updates:' in lines[j].lower():
                    is_valid = True
                    break
            
            if not is_valid:
                if any(k in line for k in ['Project', 'Improvements', 'Repairs', 'Drainage']):
                    is_valid = True
            
            if is_valid and line not in design_projects:
                design_projects.append(line)

print('Design projects: ' + str(len(design_projects)))

# Match projects
matches = []
for proj in design_projects:
    proj_key = proj.lower()
    if proj_key in funded_names:
        matches.append(proj)
    else:
        for funded_key in funded_names:
            if proj_key in funded_key or funded_key in proj_key:
                proj_words = set(proj_key.split())
                funded_words = set(funded_key.split())
                if len(proj_words.intersection(funded_words)) >= 2:
                    matches.append(proj)
                    break

unique = list(set(matches))
print('Matched: ' + str(len(unique)))

result = len(unique)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
