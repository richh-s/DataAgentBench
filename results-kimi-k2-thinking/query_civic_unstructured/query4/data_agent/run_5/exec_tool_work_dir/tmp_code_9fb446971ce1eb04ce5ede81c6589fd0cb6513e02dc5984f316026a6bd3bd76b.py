code = """import json
import re

# Get the file paths directly from the stored results
civic_path = '/tmp/tmp5.json'
funding_path = '/tmp/tmp6.json'

# Load the data
civic_docs = json.load(open(civic_path))
funding_data = json.load(open(funding_path))

# Build funding lookup
funding = {}
for rec in funding_data:
    proj = rec['Project_Name']
    amt = int(rec['Amount'])
    funding[proj] = funding.get(proj, 0) + amt

# Find projects with "2022 Morning View" patterns
spring_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line = line.strip()
        if line and ('2022' in line) and ('Morning View' in line or 'Annual' in line):
            spring_projects.append(line)

# Remove duplicates
unique = list(dict.fromkeys(spring_projects))

# Count funding
total = 0
count = 0
for proj in unique:
    if proj in funding:
        count += 1
        total += funding[proj]

result = {'count': count, 'total_funding': total}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json'}

exec(code, env_args)
