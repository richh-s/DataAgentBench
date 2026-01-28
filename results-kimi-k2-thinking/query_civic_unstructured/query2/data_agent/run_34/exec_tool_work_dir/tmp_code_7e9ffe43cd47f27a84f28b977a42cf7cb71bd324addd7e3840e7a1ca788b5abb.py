code = """import json, re

# Read civic documents file
civic_docs_file = var_functions.query_db:0
civic_docs = []
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Extract park-related projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Look for lines with park that might be project names
        if 'park' in line.lower() and len(line) > 5 and not line.startswith('('):
            # Check surrounding lines for completion in 2022
            for j in range(max(0, i-5), min(len(lines), i+15)):
                context_line = lines[j].strip()
                if 'construction was completed' in context_line.lower() and '2022' in context_line:
                    # Extract completion date
                    date_match = re.search(r'(\w+\s+2022)', context_line, re.IGNORECASE)
                    if date_match:
                        completion_date = date_match.group(1)
                        park_projects_2022.append({
                            'project_name': line,
                            'completion_date': completion_date,
                            'document': doc.get('filename', '')
                        })
                        break

# Remove duplicates
unique_projects = []
seen_names = set()
for proj in park_projects_2022:
    name = proj['project_name']
    if name not in seen_names:
        unique_projects.append(proj)
        seen_names.add(name)

print(f"Found {len(unique_projects)} park projects completed in 2022")
for proj in unique_projects:
    print(f"  - {proj['project_name']} ({proj['completion_date']})")

# Save to file for next step
with open('/tmp/park_projects_2022.json', 'w') as f:
    json.dump(unique_projects, f)

result = {
    'count': len(unique_projects),
    'projects': unique_projects
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.list_db:40': ['civic_docs']}

exec(code, env_args)
