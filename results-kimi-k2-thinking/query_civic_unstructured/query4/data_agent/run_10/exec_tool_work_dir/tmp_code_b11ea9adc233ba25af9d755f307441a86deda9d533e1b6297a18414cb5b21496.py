code = """import json

# Load funding data from aggregated query
funding_path = locals()['var_functions.query_db:96']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents 
with open(locals()['var_functions.query_db:92'], 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup: project name -> total funding amount
funding_lookup = {}
for record in funding_records:
    funding_lookup[record['Project_Name']] = int(record['Total_Amount'])

print('Built funding lookup with', len(funding_lookup), 'projects')
print('Analyzing', len(civic_docs), 'civic documents')

# Find projects with Spring 2022 references
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lowertext = text.lower()
    
    # Check for Spring 2022 date references
    if 'spring 2022' in lowertext or '2022-spring' in lowertext:
        # Extract potential project names
        for line in text.split('\n'):
            line = line.strip()
            # Heuristic: project names start with capital, reasonable length, contain keywords
            if line and len(line) > 15 and line[0].isupper():
                lowline = line.lower()
                keywords = ['project', 'improvement', 'repair', 'renovation']
                if any(k in lowline for k in keywords):
                    spring_projects.add(line)

print('Found', len(spring_projects), 'potential Spring 2022 projects')

# Match with funding database
matched = {}
for project in spring_projects:
    if project in funding_lookup:
        matched[project] = funding_lookup[project]
    else:
        # Try partial match
        proj_lower = project.lower()
        for funded in funding_lookup:
            if proj_lower in funded.lower():
                matched[funded] = funding_lookup[funded]
                break

# Final results
count = len(matched)
total = sum(matched.values())

print('Final count:', count)
print('Total funding:', total)

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.execute_python:98': {'found_spring': True, 'matched_funding': 8868000}}

exec(code, env_args)
