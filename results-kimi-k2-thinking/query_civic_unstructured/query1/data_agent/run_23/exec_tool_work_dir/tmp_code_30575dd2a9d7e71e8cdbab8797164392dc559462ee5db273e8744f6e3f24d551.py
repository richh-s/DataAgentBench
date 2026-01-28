code = """import json
import re

# Load data
funding_path = 'var_functions.query_db:30'
civic_path = 'var_functions.query_db:31'

with open(funding_path) as f:
    funding_records = json.load(f)

with open(civic_path) as f:
    civic_docs = json.load(f)

# Create funding dictionary for projects > $50K
d funded_lookup = {}
for rec in funding_records:
    try:
        amt = int(rec.get('Amount', 0))
        if amt > 50000:
            name = rec.get('Project_Name', '').strip()
            if name:
                funded_lookup[name.lower()] = name
    except:
        pass

print('Funded projects > $50K: ' + str(len(funded_lookup)))

# Extract capital design projects
design_projects = []

def extract_project_name(text):
    if not text or len(text) < 10:
        return None
    if text.isupper() and len(text.split()) <= 3:
        return None
    if any(x in text for x in ['cid:', 'Updates:', 'Project Schedule:', 'Page', 'RECOMMENDED ACTION:', 'DISCUSSION:']):
        return None
    if text[0].isupper() and len(text.split()) >= 2:
        return text
    return None

for doc in civic_docs:
    text = doc.get('text', '')
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    end = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
        pos = text.find(marker, start + 50)
        if start < pos < end:
            end = pos
    
    section = text[start:end]
    lines = section.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        project_name = extract_project_name(line)
        if project_name:
            # Verify by checking subsequent lines
            is_valid = False
            for j in range(i+1, min(i+4, len(lines))):
                nxt = lines[j].lower()
                if 'updates:' in nxt or 'project schedule:' in nxt:
                    is_valid = True
                    break
            
            if not is_valid:
                # Check for project keywords
                keywords = ['Project', 'Improvements', 'Drainage', 'Repairs', 'Road', 'Park']
                for k in keywords:
                    if k in line:
                        is_valid = True
                        break
            
            if is_valid and line not in design_projects:
                design_projects.append(line)

print('Design projects extracted: ' + str(len(design_projects)))

# Match projects
matched = []
for proj in design_projects:
    proj_key = proj.lower()
    if proj_key in funded_lookup:
        matched.append(proj)
    else:
        # Fuzzy match
        for fund_key in funded_lookup:
            if proj_key in fund_key or fund_key in proj_key:
                proj_words = set(proj_key.split())
                fund_words = set(fund_key.split())
                if len(proj_words.intersection(fund_words)) >= 2:
                    matched.append(proj)
                    break

unique_matches = list(set(matched))
print('Final matches: ' + str(len(unique_matches)))

result = len(unique_matches)
print('__RESULT__:')
print(json.dumps(result))
}"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
