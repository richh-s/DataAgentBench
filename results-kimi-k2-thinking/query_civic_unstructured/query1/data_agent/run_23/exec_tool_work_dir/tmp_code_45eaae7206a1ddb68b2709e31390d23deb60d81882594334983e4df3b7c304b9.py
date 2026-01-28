code = """import json

# Load funding data from storage key
funding_file = var_functions.query_db:30
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents from storage key
civic_file = var_functions.query_db:31
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build set of funded project names (lowercase)
funded_names = {}
for rec in funding_records:
    try:
        amount = int(rec.get('Amount', 0))
        if amount > 50000:
            name = rec.get('Project_Name', '').strip()
            if name:
                funded_names[name.lower()] = name
    except:
        pass

print('Total funded projects > $50K: ' + str(len(funded_names)))

# Extract design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find end of section
    construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
    notstarted_start = text.find('Capital Improvement Projects (Not Started)', design_start)
    
    end_pos = len(text)
    if construction_start > design_start:
        end_pos = min(end_pos, construction_start)
    if notstarted_start > design_start:
        end_pos = min(end_pos, notstarted_start)
    
    design_section = text[design_start:end_pos]
    lines = design_section.split('\n')
    
    # Extract project names
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers
        if line.startswith('cid:') or 'Updates:' in line or 'Project Schedule:' in line or 'Page ' in line:
            continue
        
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        # Check if it's a project name
        if line[0].isupper() and len(line.split()) >= 2:
            # Verify
            valid = False
            for j in range(i+1, min(i+4, len(lines))):
                nxt = lines[j].lower()
                if 'updates:' in nxt or 'project schedule:' in nxt:
                    valid = True
                    break
            
            if not valid:
                for kw in ['Project', 'Improvements', 'Drainage', 'Repairs', 'Road']:
                    if kw in line:
                        valid = True
                        break
            
            if valid and line not in design_projects:
                design_projects.append(line)

print('Capital design projects found: ' + str(len(design_projects)))

# Match
matched = []
for p in design_projects:
    pk = p.lower()
    if pk in funded_names:
        matched.append(p)
    else:
        for fk in funded_names:
            if pk in fk or fk in pk:
                proj_words = set(pk.split())
                funded_words = set(fk.split())
                if len(proj_words.intersection(funded_words)) >= 2:
                    matched.append(p)
                    break

unique_matched = list(set(matched))
print('Final matched count: ' + str(len(unique_matched)))

result = len(unique_matched)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
