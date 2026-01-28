code = """import json

# Load funding data (aggregated by project name)
with open(locals()['var_functions.query_db:114'], 'r') as f:
    funding_records = json.load(f)

# Load civic documents
with open(locals()['var_functions.query_db:122'], 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup: project name -> total amount
funding_lookup = {}
for record in funding_records:
    project_name = record['Project_Name']
    total_amount = int(record['Total_Amount'])
    funding_lookup[project_name] = total_amount

print('Funding lookup contains', len(funding_lookup), 'projects')

# Find projects with Spring 2022 start dates
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Look for Spring 2022 references in project schedules
    if 'spring 2022' in lower_text or '2022-spring' in lower_text:
        # Extract lines that might contain project names
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Look for project names (lines before schedule indicators)
            if (i > 0 and 
                ('complete design' in line.lower() or 
                 'advertise' in line.lower() or 
                 'begin construction' in line.lower()) and
                '2022' in line):
                # The previous line is likely the project name
                project_line = lines[i-1].strip()
                if (project_line and 
                    project_line[0].isupper() and 
                    len(project_line) > 10 and
                    not any(word in project_line.lower() 
                           for word in ['completed', 'page', 'item', 'agenda'])):
                    spring_2022_projects.add(project_line)

print('Spring 2022 project candidates:', len(spring_2022_projects))

# Match with funding database
matched_projects = {}
for project in spring_2022_projects:
    # Check exact match
    if project in funding_lookup:
        matched_projects[project] = funding_lookup[project]
    else:
        # Try partial matching (project name may be contained in funded name)
        proj_lower = project.lower()
        for funded_name in funding_lookup:
            funded_lower = funded_name.lower()
            if (proj_lower in funded_lower or 
                funded_lower in proj_lower or
                abs(len(proj_lower) - len(funded_lower)) < 10):
                # Additional heuristic: if names are similar length and share keywords
                matched_projects[funded_name] = funding_lookup[funded_name]
                break

project_count = len(matched_projects)
total_funding = sum(matched_projects.values())

print('Matched projects:', project_count)
print('Total funding:', total_funding)

result = {
    'count': project_count,
    'total_funding': total_funding,
    'projects': list(matched_projects.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.execute_python:98': {'found_spring': True, 'matched_funding': 8868000}, 'var_functions.query_db:108': 'file_storage/functions.query_db:108.json', 'var_functions.query_db:112': 'file_storage/functions.query_db:112.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:122': 'file_storage/functions.query_db:122.json', 'var_functions.execute_python:126': {'funding_projects': 500, 'spring_references': 4}}

exec(code, env_args)
