code = """import json

# Load funding data
with open('storage/var_functions.query_db:6.json') as f:
    funding = json.load(f)

# Load mongo data
with open('storage/var_functions.query_db:2.json') as f:
    mongo = json.load(f)

# Projects with funding > $50,000
funding_names = [f['Project_Name'] for f in funding if f['Amount'] > 50000]

# Extract design projects from mongo docs
design_names = []
for doc in mongo:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Find lines between Design and Construction sections
        start_marker = 'Capital Improvement Projects (Design)'
        end_marker = 'Capital Improvement Projects (Construction)'
        
        start_idx = text.find(start_marker)
        if start_idx >= 0:
            end_idx = text.find(end_marker, start_idx)
            if end_idx >= 0:
                design_section = text[start_idx:end_idx]
            else:
                # Alternative end marker
                end_marker2 = 'Capital Improvement Projects (Not Started)'
                end_idx2 = text.find(end_marker2, start_idx)
                design_section = text[start_idx:end_idx2] if end_idx2 >= 0 else text[start_idx:]
            
            # Extract project names (lines that are project titles)
            lines = design_section.split('\n')
            for line in lines[1:]:  # Skip the header row
                clean = line.strip()
                # Skip empty/invalid lines
                if not clean or clean.startswith('(') or clean.startswith('•'):
                    continue
                # Skip update lines
                if 'Updates:' in clean or 'Schedule:' in clean or 'To:' in clean:
                    continue
                if 'Consultant' in clean or 'Staff' in clean or 'Project' in clean[:15]:
                    continue
                if len(clean) > 5 and not clean.isupper():
                    project_name = clean.strip('•- ')
                    design_names.append(project_name)

# Find matching projects
matches = []
for f in funding_names:
    found_match = False
    for d in design_names:
        # Case-insensitive partial match
        if f.lower() in d.lower() or d.lower() in f.lower():
            found_match = True
            break
    if found_match and f not in matches:
        matches.append(f)

count = len(matches)
print('__RESULT__: {}
{}'.format(count, count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
