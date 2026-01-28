code = """import json, re
import os

# Access variables with proper names
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:8']

# Check if files exist and load them
if os.path.exists(funding_path) and os.path.exists(civic_path):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
    with open(civic_path, 'r') as f:
        civic_docs = json.load(f)
    
    # Build funding map for amounts > 50000
    def clean_name(name):
        name = re.sub(r'\(FEMA[^\)]*\)', '', name, flags=2)
        name = re.sub(r'\(CalOES[^\)]*\)', '', name, flags=2)
        name = re.sub(r'\(CalJPIA[^\)]*\)', '', name, flags=2)
        name = re.sub(r'\s*Project\s*$', '', name, flags=2)
        return name.strip().lower()
    
    funding_map = {}
    for record in funding_data:
        amt = int(record['Amount'])
        if amt > 50000:
            key = clean_name(record['Project_Name'])
            if key:
                funding_map[key] = True
    
    # Extract design projects from civic docs
    design_projects = set()
    for doc in civic_docs:
        txt = doc.get('text', '')
        start_pos = txt.find('Capital Improvement Projects (Design)')
        if start_pos == -1:
            continue
        end_pos = txt.find('Capital Improvement Projects (Construction)', start_pos)
        if end_pos == -1:
            end_pos = len(txt)
        section = txt[start_pos:end_pos]
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 10 and not line.startswith('(') and 'Capital Improvement' not in line:
                if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line:
                    keywords = ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs','street','water','traffic']
                    if any(kw in line.lower() for kw in keywords):
                        design_projects.add(line)
    
    # Count matches
    count = sum(1 for proj in design_projects if clean_name(proj) in funding_map)
    
    result = {'count': count, 'status': 'success'}
else:
    result = {'error': 'File not found', 'funding_path': funding_path, 'civic_path': civic_path}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
