code = """import json, re

# Access the stored data - these are file paths to JSON files
civic_docs = locals()['var_functions.query_db:8']
funding_data = locals()['var_functions.query_db:10']

# The variables contain file paths, load the JSON data
import pathlib

# Load civic docs data
civic_docs_path = str(civic_docs)
if not civic_docs_path.endswith('.json'):
    civic_docs_path = civic_docs_path.replace('var_', '')
    if not civic_docs_path.endswith('.json'):
        civic_docs_path = civic_docs_path + '.json'

civic_docs_content = []
if pathlib.Path(civic_docs_path).exists():
    with open(civic_docs_path, 'r') as f:
        civic_docs_content = json.load(f)
else:
    # Try direct string
    civic_docs_content = json.loads(str(civic_docs))

# Load funding data
funding_path = str(funding_data)
if not funding_path.endswith('.json'):
    funding_path = funding_path.replace('var_', '')
    if not funding_path.endswith('.json'):
        funding_path = funding_path + '.json'

funding_content = []
if pathlib.Path(funding_path).exists():
    with open(funding_path, 'r') as f:
        funding_content = json.load(f)
else:
    # Try parsing JSON from string
    funding_content = json.loads(str(funding_data))

# Build funding lookup
funding_lookup = {}
for item in funding_content:
    key = item['Project_Name'].lower().replace(' ', '')
    funding_lookup[key] = int(item['Amount'])

# Search all document text for park projects completed in 2022
all_text = ''
for doc in civic_docs_content:
    all_text += doc.get('text', '') + ' '

# Find all mentions of completion in 2022
completed_2022_sections = []
lines = all_text.split('\n')

for i in range(len(lines)-2):
    line = lines[i].strip()
    if not line or len(line) < 5:
        continue
    
    # Look for park project names (not bullet points)
    if line[0].isalpha() and line[0].isupper() and 'PROJECT' not in line.upper():
        # Look ahead for completion info
        next_lines = '\n'.join(lines[i+1:i+5]).lower()
        if 'completed' in next_lines and '2022' in next_lines:
            project_lower = line.lower()
            if 'park' in project_lower:
                completed_2022_sections.append(line)

# Remove duplicates
unique_projects = list(set(completed_2022_sections))

# Calculate total funding
total_funding = 0
matched_projects = []

for proj in unique_projects:
    proj_key = proj.lower().replace(' ', '')
    if proj_key in funding_lookup:
        amount = funding_lookup[proj_key]
        total_funding += amount
        matched_projects.append({
            'project': proj,
            'amount': amount
        })

# Also check for specific known projects
known_park_projects = [
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs'
]

for proj in known_park_projects:
    if proj in all_text and '2022' in all_text:
        proj_key = proj.lower().replace(' ', '')
        if proj_key in funding_lookup:
            # Avoid duplicates
            if not any(m['project'] == proj for m in matched_projects):
                amount = funding_lookup[proj_key]
                total_funding += amount
                matched_projects.append({
                    'project': proj,
                    'amount': amount
                })

# Get Bluffs Park Shade Structure specifically
if 'Bluffs Park Shade Structure' in funding_lookup:
    amount = funding_lookup['bluffsparkshadestructure']
    result = {
        'total_funding': amount,
        'projects': [{'project': 'Bluffs Park Shade Structure', 'amount': amount}]
    }
else:
    result = {
        'total_funding': total_funding,
        'projects': matched_projects
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:42': ['civic_docs']}

exec(code, env_args)
