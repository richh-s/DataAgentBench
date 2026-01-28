code = """import json

# Get the results from storage
funding_result = locals()['var_functions.query_db:66']
civic_result = locals()['var_functions.query_db:64']

# Load the JSON data - these are file paths
with open(funding_result) as f:
    funding_data = json.load(f)

with open(civic_result) as f:
    civic_data = json.load(f)

print('Funding items:', len(funding_data))
print('Civic documents:', len(civic_data))

# Build funding lookup
funding_dict = {}
for item in funding_data:
    name = item['Project_Name']
    amount = int(item['Total_Amount'])
    funding_dict[name] = amount

# Extract documents mentioning Spring 2022
spring_docs = []
for doc in civic_data:
    text = doc.get('text', '').lower()
    if 'spring 2022' in text or '2022-spring' in text:
        spring_docs.append(doc)

# Find project names in Spring 2022 documents
spring_projects = set()
for doc in spring_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line and len(line) > 15 and line[0].isupper():
            low = line.lower()
            if 'project' in low or 'improvement' in low or 'repair' in low:
                spring_projects.add(line)

# Match with funding
matched = {}
for proj in spring_projects:
    if proj in funding_dict:
        matched[proj] = funding_dict[proj]
    else:
        # Fuzzy match
        for funded in funding_dict:
            if proj.lower() in funded.lower():
                matched[funded] = funding_dict[funded]
                break

count = len(matched)
total = sum(matched.values())
print('Matched:', count, 'projects')
print('Total funding:', total)

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
