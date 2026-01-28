code = """import json
import re

# Read the funding data from the file
funding_file = locals()['var_functions.query_db:2']
civic_file = locals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print("Files loaded successfully")
print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")

# Extract capital projects with design status from civic documents
projects_info = {}

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section header
    if 'Capital Improvement Projects (Design)' in text:
        start_idx = text.find('Capital Improvement Projects (Design)')
        # Find end of this section (look for next major header)
        end_idx = text.find('\n\n', start_idx + 50)
        if end_idx == -1:
            end_idx = len(text)
        
        section_text = text[start_idx:end_idx]
        lines = section_text.split('\n')
        
        for line in lines:
            line = line.strip()
            # Look for lines that seem like project titles
            if (line and 
                len(line) > 8 and
                not line.startswith('\\u') and  # Skip unicode bullets
                'Updates' not in line and
                'Project Schedule' not in line and
                'Capital Improvement' not in line and
                'Design' not in line):
                
                if 'Project' in line or (line[0].isupper() and ' ' in line):
                    projects_info[line] = {'status': 'design', 'type': 'capital'}

# Also look for project names in the full text
for doc in civic_docs:
    text = doc.get('text', '')
    # Pattern: Project name followed by bullet points starting project details
    pattern = r'\n([A-Z][a-zA-Z0-9\s&\-\/]+?(?:Project)?)\s*\n\s*(?:[\-\u2022])\s*\w+:?' 
    matches = re.findall(pattern, text)
    
    for match in matches:
        name = match.strip()
        if (len(name) > 10 and 
            'CAPITAL' not in name.upper() and
            'DISASTER' not in name.upper() and
            'FEMA' not in name.upper()):
            
            # Check surrounding context for design mention
            idx = text.find(name)
            if idx > 0:
                snippet = text[max(0, idx-200):idx+200].lower()
                if 'design' in snippet:
                    projects_info[name] = {'status': 'design', 'type': 'capital'}

# Filter out non-capital projects
filtered_projects = {}
for name, info in projects_info.items():
    lower_name = name.lower()
    if 'fema' not in lower_name and 'disaster' not in lower_name:
        filtered_projects[name] = info

print(f"Capital design projects: {len(filtered_projects)}")

# Match with funding > $50,000
matches = []

for funding in funding_data:
    name = funding['Project_Name']
    amount = int(funding['Amount'])
    
    if amount <= 50000:
        continue
    
    # Check direct match
    if name in filtered_projects:
        matches.append({'project': name, 'amount': amount})
    else:
        # Remove parenthetical suffixes
        base_name = re.sub(r'\s*\([^)]*\)$', '', name)
        if base_name in filtered_projects:
            matches.append({'project': name, 'base': base_name, 'amount': amount})

# Count unique base names
unique_bases = set()
for m in matches:
    base = m.get('base', m['project'])
    base_clean = re.sub(r'\s*\([^)]*\)$', '', base)
    unique_bases.add(base_clean)

count = len(unique_bases)

result = {
    'count': count,
    'samples': list(unique_bases)[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
