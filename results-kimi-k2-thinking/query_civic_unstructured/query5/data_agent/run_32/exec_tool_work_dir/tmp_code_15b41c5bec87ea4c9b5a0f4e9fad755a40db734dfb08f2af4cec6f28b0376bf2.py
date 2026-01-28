code = """import json, re, sys

# Load data from files
funding_path = '/tmp/tmp_hb9f3fdk.json'
civic_docs_path = '/tmp/tmp_cdv8r04p.json'

with open(funding_path, 'r') as f:
    funding = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup
funding_lookup = {}
funding_by_partial_name = {}

for item in funding:
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[name] = amount
    
    # Also create lookup by base name without suffixes
    base_name = re.sub(r'\s*\(.*?\)', '', name).strip()
    if base_name not in funding_by_partial_name:
        funding_by_partial_name[base_name] = []
    funding_by_partial_name[base_name].append({'full_name': name, 'amount': amount})

# Search civic documents for 2022 disaster projects
all_text = ""
for doc in civic_docs:
    all_text += doc.get('text', '') + "\n"

# Find all project names with 2022 and disaster indicators
disaster_projects_2022 = set()

# Look for FEMA/CalJPIA/CalOES projects with 2022
lines = all_text.split('\n')
for i, line in enumerate(lines):
    line = line.strip()
    if re.search(r'(FEMA|CalJPIA|CalOES)', line, re.IGNORECASE) and '2022' in line:
        # Extract project name (usually the line itself or previous line)
        proj_name = line
        disaster_projects_2022.add(proj_name)
        
    # Look for patterns like "2022 ... Project Name"
    if line.startswith('2022') and len(line) < 200:
        disaster_projects_2022.add(line)

# Also search for "2022" followed by project-like names in the next lines
for i, line in enumerate(lines):
    if '2022' in line and i + 1 < len(lines):
        next_line = lines[i + 1].strip()
        if next_line and len(next_line) < 150 and not next_line.startswith('('):
            # Check if next line looks like a project name (starts with capital letter, not a bullet)
            if re.match(r'^[A-Z]', next_line):
                disaster_projects_2022.add(next_line)

# Now match with funding data
total_funding = 0
matched_projects = []

for proj in disaster_projects_2022:
    # Direct match
    if proj in funding_lookup:
        total_funding += funding_lookup[proj]
        matched_projects.append({'name': proj, 'amount': funding_lookup[proj]})
        continue
    
    # Partial match - check base name
    base_name = re.sub(r'\s*\(.*?\)', '', proj).strip()
    if base_name in funding_by_partial_name:
        # Find the best match
        candidates = funding_by_partial_name[base_name]
        if len(candidates) == 1:
            total_funding += candidates[0]['amount']
            matched_projects.append({'name': proj, 'amount': candidates[0]['amount']})
        else:
            # Multiple variants, pick the one with FEMA suffix if available
            for cand in candidates:
                if 'FEMA' in cand['full_name']:
                    total_funding += cand['amount']
                    matched_projects.append({'name': proj, 'amount': cand['amount']})
                    break

result = {
    'total_funding_2022_disaster': total_funding,
    'project_count': len(matched_projects),
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
