code = """# Load data and process
import json

# Load funding data
funding_file = var_functions.query_db:30
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents  
civic_file = var_functions.query_db:31
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding dictionary (amount > 50000)
funding_projects = {}
for rec in funding_records:
    try:
        amt = int(rec.get('Amount', 0))
        if amt > 50000:
            name = rec.get('Project_Name', '').strip()
            if name:
                funding_projects[name.lower()] = name
    except:
        pass

print('Funded projects > $50K: ' + str(len(funding_projects)))

# Extract capital design projects from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section start
    design_idx = text.find('Capital Improvement Projects (Design)')
    if design_idx == -1:
        continue
    
    # Find section end
    end_idx = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 
                   'Capital Improvement Projects (Not Started)']:
        marker_idx = text.find(marker, design_idx + 50)
        if design_idx < marker_idx < end_idx:
            end_idx = marker_idx
    
    design_section = text[design_idx:end_idx]
    lines = design_section.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers
        if 'cid:' in line or 'Updates:' in line or 'Project Schedule:' in line or 'Page ' in line:
            continue
        
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        # Check for project name
        if line[0].isupper() and len(line.split()) >= 2:
            # Verify by checking following lines
            is_project = False
            for j in range(i+1, min(i+4, len(lines))):
                nxt = lines[j].lower()
                if 'updates:' in nxt or 'project schedule:' in nxt:
                    is_project = True
                    break
            
            # Also check for project keywords
            if not is_project:
                keywords = ['Project', 'Improvements', 'Drainage', 'Repairs', 'Road']
                for kw in keywords:
                    if kw in line:
                        is_project = True
                        break
            
            if is_project and line not in design_projects:
                design_projects.append(line)

print('Capital design projects found: ' + str(len(design_projects)))

# Match projects with funding
matched = []
for proj in design_projects:
    proj_key = proj.lower()
    if proj_key in funding_projects:
        matched.append(proj)
    else:
        # Fuzzy matching
        for fund_key in funding_projects:
            # Check if they overlap
            if proj_key in fund_key or fund_key in proj_key:
                proj_words = set(proj_key.split())
                fund_words = set(fund_key.split())
                if len(proj_words.intersection(fund_words)) >= 2:
                    matched.append(proj)
                    break

unique = list(set(matched))
print('Final matches: ' + str(len(unique)))

result = len(unique)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
