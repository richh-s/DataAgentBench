code = """import json

# Load funding data  
funding_file = locals()['var_functions.query_db:66']
with open(funding_file, 'r') as f:
    funding_items = json.load(f)

# Load civic documents
with open(locals()['var_functions.query_db:90'], 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup: project name -> total amount
funding_lookup = {}
for item in funding_items:
    name = item['Project_Name']
    amount = int(item['Total_Amount'])
    funding_lookup[name] = amount

print('Funding lookup built with', len(funding_lookup), 'projects')

# Find Spring 2022 projects - look for date references
spring_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    has_spring = 'spring 2022' in lower_text or '2022-spring' in lower_text
    
    if has_spring:
        print('Found Spring 2022 in document:', doc.get('filename'))
        # Extract project names (capitalized lines that look like project titles)
        for line in text.split('\n'):
            line = line.strip()
            if line and line[0].isupper() and len(line) > 10:
                low_line = line.lower()
                if any(k in low_line for k in ['project', 'improvement', 'repair']):
                    spring_projects.add(line)

# Match with funding
matched = {}
for project in spring_projects:
    if project in funding_lookup:
        matched[project] = funding_lookup[project]
    else:
        # Try fuzzy match: project name contained in funded name
        proj_lower = project.lower()
        for funded in funding_lookup:
            if proj_lower in funded.lower():
                matched[funded] = funding_lookup[funded]
                break

count = len(matched)
total = sum(matched.values())
print('Matched projects:', count)
print('Total funding:', total)
print('Projects:', list(matched.keys()))

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json'}

exec(code, env_args)
