code = """import json

# Load funding and civic data
funding_data = json.load(open(locals()['var_functions.query_db:114']))
civic_docs = json.load(open(locals()['var_functions.query_db:122']))

# Create funding lookup dictionary
funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name']] = int(item['Total_Amount'])

# Find projects that started in Spring 2022
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check for spring 2022 references
    if 'spring 2022' in lower_text or '2022-spring' in lower_text:
        # Extract project names (simplified approach)
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Simple heuristic: line begins with capital letter, contains keywords, reasonable length
            if line and len(line) > 15:
                if line[0].isupper():
                    low_line = line.lower()
                    if 'project' in low_line or 'improvement' in low_line or 'repair' in low_line:
                        spring_2022_projects.add(line)

# Match with funding database
matched_projects = {}
for project in spring_2022_projects:
    if project in funding_lookup:
        matched_projects[project] = funding_lookup[project]
    else:
        # Try fuzzy matching
        proj_low = project.lower()
        for funded_name in funding_lookup:
            funded_low = funded_name.lower()
            if proj_low in funded_low or funded_low in proj_low:
                matched_projects[funded_name] = funding_lookup[funded_name]
                break

count = len(matched_projects)
total = sum(matched_projects.values())

print('__RESULT__:')
print(json.dumps({'count': count, 'total_funding': total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.execute_python:98': {'found_spring': True, 'matched_funding': 8868000}, 'var_functions.query_db:108': 'file_storage/functions.query_db:108.json', 'var_functions.query_db:112': 'file_storage/functions.query_db:112.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:122': 'file_storage/functions.query_db:122.json', 'var_functions.execute_python:126': {'funding_projects': 500, 'spring_references': 4}}

exec(code, env_args)
