code = """import json

# Load funding and civic data from storage
funding_result = locals()['var_functions.query_db:114']
civic_result = locals()['var_functions.query_db:122']

with open(funding_result, 'r') as f:
    funding_records = json.load(f)

with open(civic_result, 'r') as f:
    civic_documents = json.load(f)

# Build funding lookup dictionary
funding_lookup = {}
for record in funding_records:
    name = record['Project_Name']
    amount = int(record['Total_Amount'])
    funding_lookup[name] = amount

print('Funding records loaded:', len(funding_lookup))
print('Civic documents loaded:', len(civic_documents))

# Find projects with Spring 2022 references
spring_projects = set()

for doc in civic_documents:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check for Spring 2022 date references
    if 'spring 2022' in lower_text or '2022-spring' in lower_text:
        # Extract project names from surrounding context
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Heuristic: project names are capitalized, contain keywords, reasonable length
            if line and len(line) > 10 and line[0].isupper():
                low_line = line.lower()
                if any(kw in low_line for kw in ['project', 'improvement', 'repair', 'construction']):
                    # Check if this project is mentioned near Spring 2022
                    context_start = max(0, i-3)
                    context_end = min(len(lines), i+4)
                    context = ' '.join(lines[context_start:context_end]).lower()
                    if 'spring 2022' in context or '2022-spring' in context:
                        spring_projects.add(line)

print('Spring 2022 projects found:', len(spring_projects))

# Match projects with funding data
matched_projects = {}
for project in spring_projects:
    # Exact match first
    if project in funding_lookup:
        matched_projects[project] = funding_lookup[project]
    else:
        # Partial/fuzzy match if exact not found
        proj_lower = project.lower()
        for funded_name in funding_lookup:
            funded_lower = funded_name.lower()
            if proj_lower in funded_lower or funded_lower in proj_lower:
                matched_projects[funded_name] = funding_lookup[funded_name]
                break

project_count = len(matched_projects)
total_funding = sum(matched_projects.values())

print('Matched with funding:', project_count)
print('Total funding:', total_funding)

result = {'count': project_count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.execute_python:98': {'found_spring': True, 'matched_funding': 8868000}, 'var_functions.query_db:108': 'file_storage/functions.query_db:108.json', 'var_functions.query_db:112': 'file_storage/functions.query_db:112.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:122': 'file_storage/functions.query_db:122.json', 'var_functions.execute_python:126': {'funding_projects': 500, 'spring_references': 4}}

exec(code, env_args)
