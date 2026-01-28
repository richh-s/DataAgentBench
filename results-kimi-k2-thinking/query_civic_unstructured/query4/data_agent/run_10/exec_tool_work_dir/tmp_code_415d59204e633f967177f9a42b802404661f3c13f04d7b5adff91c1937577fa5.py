code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:8']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Build funding lookup with sum aggregation
funding_lookup = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[project_name] = funding_lookup.get(project_name, 0) + amount

# Load civic documents
civic_path = locals()['var_functions.query_db:4']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Search for Spring 2022 projects without relying on complex regex
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check if document mentions Spring 2022 (case insensitive)
    if 'spring 2022' in lower_text or '2022-spring' in lower_text:
        # Split by lines and search for project-like names
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) > 10 and len(line) < 200:
                # Likely project name if starts with capital and contains keywords
                if line[0].isupper():
                    lower_line = line.lower()
                    keywords = ['project', 'improvement', 'repair', 'replacement', 'construction', 'renovation']
                    if any(kw in lower_line for kw in keywords):
                        spring_2022_projects.add(line)

# Now match these with funding database
matched_projects = {}
for project in spring_2022_projects:
    # Direct match
    if project in funding_lookup:
        matched_projects[project] = funding_lookup[project]
    else:
        # Try partial matching (simpler approach)
        project_lower = project.lower()
        for funded_name in funding_lookup:
            funded_lower = funded_name.lower()
            if project_lower in funded_lower or funded_lower in project_lower:
                matched_projects[funded_name] = funding_lookup[funded_name]
                break

# Results
project_count = len(matched_projects)
total_funding = sum(matched_projects.values())

result = {
    'count': project_count,
    'total_funding': total_funding,
    'projects': list(matched_projects.keys())
}

print('__RESULT__:')
output = json.dumps(result)
print(output)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}}

exec(code, env_args)
