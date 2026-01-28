code = """import json
import re

# Load data
civic_path = locals()['var_functions.query_db:44']
funding_path = locals()['var_functions.query_db:31']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Build funding map
funding_map = {}
for record in funding_data:
    name = record['Project_Name']
    amt = int(record['Amount'])
    funding_map[name] = funding_map.get(name, 0) + amt

# Extract 2022 Spring projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    current_proj = None
    for i, line in enumerate(lines):
        # Detect project name lines
        if len(line) > 15 and not line.isupper() and not line.startswith('(') and 'cid:' not in line:
            # Check if next line is schedule-related
            if i + 1 < len(lines):
                next_line = lines[i+1]
                if any(keyword in next_line for keyword in ['Updates:', 'Schedule:', 'Project Description:']):
                    current_proj = line
        
        # Look for Spring 2022 dates
        if '2022' in line and 'Spring' in line:
            if current_proj:
                spring_projects.append(current_proj)
                current_proj = None

# Remove duplicates
unique = list(dict.fromkeys(spring_projects))

# Match funding
total_funding = 0
results = []

for proj in unique:
    if proj in funding_map:
        total_funding += funding_map[proj]
        results.append({'project': proj, 'funding': funding_map[proj]})
    else:
        # Partial match check
        for funded in funding_map:
            if proj.lower() in funded.lower() or funded.lower().startswith(proj.lower()[0:15]):
                total_funding += funding_map[funded]
                results.append({'project': proj, 'funding': funding_map[funded], 'matched_to': funded})
                break

# Format output
output = {
    'count': len(results),
    'total_funding': total_funding,
    'projects': results
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
