code = """import json, re, os

# Access the result from the query
funding_path = locals()['var_functions.query_db:18']
civic_docs_path = locals()['var_functions.query_db:30']

# Load funding data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_docs))

# Look for Spring 2022 pattern in documents
spring_months = ['March', 'April', 'May']
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        # Check for 2022 and spring months
        if '2022' in line and any(month in line for month in spring_months):
            # Look back for project name
            for j in range(max(0, i-8), i):
                prev_line = lines[j].strip()
                # Heuristic for project name
                if (prev_line and len(prev_line) > 10 and 
                    prev_line[0].isupper() and 
                    ' ' in prev_line and  # Contains spaces, not a single word
                    not any(x in prev_line for x in ['Updates:', 'Schedule:', 'Item', 'Page', 'Agenda', '---'])):
                    spring_2022_projects.append(prev_line)
                    break

# Get unique projects
unique_projects = list(set(spring_2022_projects))
print('Unique Spring 2022 projects found:', len(unique_projects))

# Match with funding data
funding_matches = []
total_funding = 0

for proj_name in unique_projects:
    # Look for matching project in funding data
    for funding in funding_data:
        funding_proj = funding['Project_Name']
        # Simple match - if project name contains or equals
        if (proj_name in funding_proj or funding_proj in proj_name or
            proj_name.replace(' Project', '') in funding_proj):
            funding_matches.append({
                'project': proj_name,
                'funding_project': funding_proj,
                'amount': int(funding['Amount'])
            })
            total_funding += int(funding['Amount'])

print('Matching funding records:', len(funding_matches))
print('Total funding:', total_funding)

result = {
    'spring_2022_projects_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects[:15],  # Show first 15
    'funding_matches': funding_matches[:10]  # Show first 10 matches
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
