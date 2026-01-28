code = """import json, re

# Load funding and civic data
with open(locals()['var_functions.query_db:114'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:122'], 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup
def build_lookup(data):
    lookup = {}
    for item in data:
        lookup[item['Project_Name']] = int(item['Total_Amount'])
    return lookup

funding_lookup = build_lookup(funding_data)

# Find projects mentioning Spring 2022
spring_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    # Look for Spring 2022 in schedule contexts
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Look for lines that might be project names
            if line and len(line) > 15 and line[0].isupper():
                low = line.lower()
                if 'project' in low or 'improvement' in low or 'repair' in low:
                    # Check if this line is near a Spring 2022 date reference
                    context_start = max(0, i-3)
                    context_end = min(len(lines), i+4)
                    context = '\n'.join(lines[context_start:context_end])
                    if 'Spring 2022' in context or '2022-Spring' in context:
                        spring_projects.add(line)

# Match with funding database
matched = {}
for proj in spring_projects:
    if proj in funding_lookup:
        matched[proj] = funding_lookup[proj]
    else:
        # Partial match
        proj_lower = proj.lower()
        for funded in funding_lookup:
            funded_lower = funded.lower()
            if proj_lower in funded_lower or funded_lower in proj_lower:
                matched[funded] = funding_lookup[funded]
                break

count = len(matched)
total = sum(matched.values())

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.execute_python:98': {'found_spring': True, 'matched_funding': 8868000}, 'var_functions.query_db:108': 'file_storage/functions.query_db:108.json', 'var_functions.query_db:112': 'file_storage/functions.query_db:112.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:122': 'file_storage/functions.query_db:122.json', 'var_functions.execute_python:126': {'funding_projects': 500, 'spring_references': 4}}

exec(code, env_args)
