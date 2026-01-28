code = """import json

# Access the latest query results directly from storage
civic_docs_file = '../var_functions.query_db:64'
funding_file = '../var_functions.query_db:10'

# Load civic documents
import pathlib, json
civic_docs = []
if pathlib.Path(civic_docs_file).exists():
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)

# Load funding data
funding_data = []
if pathlib.Path(funding_file).exists():
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    key = item['Project_Name'].lower().replace(' ', '')
    funding_lookup[key] = int(item['Amount'])

# Parse documents for park projects completed in 2022
park_projects_2022 = []
total_text = ''

for doc in civic_docs:
    text = doc.get('text', '')
    total_text += text + '\n'
    lines = text.split('\n')
    
    for i in range(len(lines)-1):
        line = lines[i].strip()
        if not line or len(line) < 5 or line[0] in '-*([{':
            continue
        
        # Look for project names
        has_caps = any(c.isupper() for c in line[:30] if c.isalpha())
        if not has_caps:
            continue
        
        # Look ahead for completion info
        for j in range(i+1, min(i+10, len(lines))):
            next_line = lines[j].strip().lower()
            if 'completed' in next_line and '2022' in next_line:
                lower_line = line.lower()
                if 'park' in lower_line or any(k in lower_line for k in ['bluffs','shade','walkway','playground']):
                    park_projects_2022.append(line)
                    break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Find funding amounts
total_funding = 0
matched_projects = []

for proj in park_projects_2022:
    proj_key = proj.lower().replace(' ', '')
    if proj_key in funding_lookup:
        total_funding += funding_lookup[proj_key]
        matched_projects.append({'project': proj, 'amount': funding_lookup[proj_key]})

# Also check for specific known projects from preview text
if 'Bluffs Park Shade Structure' in total_text and '2022' in total_text:
    key = 'bluffsparkshadestructure'
    if key in funding_lookup and not any(m['project'] == 'Bluffs Park Shade Structure' for m in matched_projects):
        total_funding += funding_lookup[key]
        matched_projects.append({'project': 'Bluffs Park Shade Structure', 'amount': funding_lookup[key]})

print('__RESULT__:')
result = {
    'total_funding': total_funding,
    'project_count': len(matched_projects),
    'projects': matched_projects
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:42': ['civic_docs'], 'var_functions.execute_python:52': {'debug': 'done'}, 'var_functions.execute_python:54': {'status': 'debug'}, 'var_functions.execute_python:58': {'status': 'debug_info_recorded'}, 'var_functions.execute_python:62': {'debug': 'path_identification'}, 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
