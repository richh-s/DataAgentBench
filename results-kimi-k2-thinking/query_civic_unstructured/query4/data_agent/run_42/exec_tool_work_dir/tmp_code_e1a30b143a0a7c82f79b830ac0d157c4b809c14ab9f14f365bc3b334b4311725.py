code = """import json

# Get MongoDB file path
mongo_path = locals()['var_functions.query_db:42']
funding_path = locals()['var_functions.query_db:4']

print('Mongo file:', mongo_path)
print('Funding file:', funding_path)

# Read MongoDB data
mongo_file = open(mongo_path)
mongo_docs = json.load(mongo_file)
mongo_file.close()

print('Mongo docs loaded:', len(mongo_docs))

# Read funding data
funding_file = open(funding_path)
funding_recs = json.load(funding_file)
funding_file.close()

print('Funding records loaded:', len(funding_recs))

# Create funding lookup
d = {}
for rec in funding_recs:
    d[rec['Project_Name']] = int(rec['Amount'])

# Extract projects starting in Spring 2022
spring_projects = set()
for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Spring' in text and '2022' in text:
        # Search for construction start patterns
        import re
        # Pattern to find project sections with construction dates
        pattern = r'([^\n]+)\n.*?Begin Construction.*?2022'
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            proj_name = match.group(1).strip()
            if proj_name and not proj_name.startswith('('):
                if 'Schedule' not in proj_name and len(proj_name) > 5:
                    spring_projects.add(proj_name)

print('Spring projects found:', len(spring_projects))
print(list(spring_projects)[:10])

# Match with funding
matched = []
for proj in spring_projects:
    if proj in d:
        matched.append({'name': proj, 'funding': d[proj]})

count = len(matched)
total = sum(m['funding'] for m in matched)

print('Final count:', count)
print('Final total funding:', total)

result = {'project_count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
