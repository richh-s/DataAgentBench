code = """import json

funding_file = locals()['var_functions.query_db:8']
civic_file = locals()['var_functions.query_db:4']

# Load funding data
funding_records = json.load(open(funding_file))

# Build funding lookup
def build_funding_lookup(records):
    lookup = {}
    for record in records:
        name = record['Project_Name']
        amount = int(record['Amount'])
        if name in lookup:
            lookup[name] += amount
        else:
            lookup[name] = amount
    return lookup

funding_lookup = build_funding_lookup(funding_records)

# Load civic documents
civic_docs = json.load(open(civic_file))

# Search for Spring 2022 projects
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    has_spring_2022 = 'Spring 2022' in text or '2022-Spring' in text
    
    if has_spring_2022:
        # Extract project names (lines that look like project titles)
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and line[0].isupper():
                # Heuristic for project names
                keywords = ['project', 'improvement', 'repair', 'replacement', 'renovation', 'construction']
                if any(k in line.lower() for k in keywords):
                    spring_projects.add(line)

# Match projects with funding
matched_projects = {}
for project in spring_projects:
    if project in funding_lookup:
        matched_projects[project] = funding_lookup[project]
    else:
        # Fuzzy matching
        for funded_name in funding_lookup:
            if (project.lower() in funded_name.lower() or 
                funded_name.lower() in project.lower()):
                matched_projects[funded_name] = funding_lookup[funded_name]
                break

# Final results
result_count = len(matched_projects)
result_funding = sum(matched_projects.values())

result_dict = {
    'count': result_count,
    'total_funding': result_funding
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}}

exec(code, env_args)
