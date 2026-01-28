code = """import json

# Load the data
with open('/tmp/tmp6v8h4l_u.json', 'r') as f:
    funding_items = json.load(f)

with open('/tmp/tmp1i3q6xjc.json', 'r') as f:
    civic_documents = json.load(f)

# Build funding lookup (sum amounts for duplicate project names)
funding_lookup = {}
for item in funding_items:
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

# Find projects with Spring 2022 references
spring_projects = set()

for doc in civic_documents:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Look for Spring 2022 indicators
    if 'spring 2022' in lower_text or '2022-spring' in lower_text:
        # Extract potential project names from this document
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Project names are typically: capitalized, reasonable length, contain keywords
            if line and len(line) > 15 and line[0].isupper():
                lower_line = line.lower()
                keywords = ['project', 'improvement', 'repair', 'replacement']
                if any(k in lower_line for k in keywords):
                    spring_projects.add(line)

# Match projects with funding data
matched_projects = {}
for project in spring_projects:
    # Direct match
    if project in funding_lookup:
        matched_projects[project] = funding_lookup[project]
    else:
        # Fuzzy match: check if project name is contained in funded name or vice versa
        proj_lower = project.lower()
        for funded_name in funding_lookup:
            funded_lower = funded_name.lower()
            if proj_lower in funded_lower or funded_lower in proj_lower:
                matched_projects[funded_name] = funding_lookup[funded_name]
                break

# Calculate final results
count = len(matched_projects)
total_funding = sum(matched_projects.values())

# Prepare output
result = {'count': count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}}

exec(code, env_args)
