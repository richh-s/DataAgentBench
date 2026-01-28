code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:96']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents  
civic_file = locals()['var_functions.query_db:108']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup dictionary
funding_lookup = {}
for record in funding_records:
    name = record['Project_Name']
    amount = int(record['Total_Amount'])
    funding_lookup[name] = amount

print('Funding lookup built with', len(funding_lookup), 'projects')

# Find Spring 2022 projects
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    t = text.lower()
    
    # Check for Spring 2022 references
    if 'spring 2022' in t or '2022-spring' in t:
        # Extract project names (capitalized lines with keywords)
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and line[0].isupper():
                low = line.lower()
                if 'project' in low or 'improvement' in low or 'repair' in low:
                    spring_2022_projects.add(line)

print('Found', len(spring_2022_projects), 'potential Spring 2022 projects')

# Match with funding
matched = {}
for proj in spring_2022_projects:
    if proj in funding_lookup:
        matched[proj] = funding_lookup[proj]
    else:
        # Try partial match
        for funded in funding_lookup:
            if proj.lower() in funded.lower():
                matched[funded] = funding_lookup[funded]
                break

count = len(matched)
total = sum(matched.values())

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.execute_python:98': {'found_spring': True, 'matched_funding': 8868000}, 'var_functions.query_db:108': 'file_storage/functions.query_db:108.json'}

exec(code, env_args)
