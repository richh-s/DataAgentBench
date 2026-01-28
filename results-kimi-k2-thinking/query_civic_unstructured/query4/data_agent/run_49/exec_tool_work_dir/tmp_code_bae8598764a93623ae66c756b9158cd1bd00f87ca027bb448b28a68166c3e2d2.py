code = """import json
import re

# Load the civic documents data
civic_file = var_functions.query_db:38
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
funding_file = var_functions.query_db:39
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Create a map of project names to funding amounts
funding_map = {}
for rec in funding_records:
    project_name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    funding_map[project_name] = amount

print('Loaded', len(civic_docs), 'civic documents')
print('Loaded', len(funding_map), 'funding records')

# Check what's in the first civic document
first_doc = civic_docs[0]
print('First doc filename:', first_doc.get('filename'))
print('First doc text length:', len(first_doc.get('text', '')))

# Preview the beginning of the text
print('Text preview:', first_doc.get('text', '')[:500])

# Let's check if there are projects with 2022 in their name
projects_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:
        # Simple extraction: look for lines that contain 2022 and project keywords
        lines = text.split('\n')
        for line in lines:
            if '2022' in line and any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 'Drainage']):
                projects_2022.append(line.strip())

print('Projects with 2022 found:', projects_2022[:10])

# Also check for Spring date patterns
spring_patterns = ['Spring 2022', '2022-Spring', 'March 2022', 'April 2022', 'May 2022']
spring_indicators = []
for doc in civic_docs:
    text = doc.get('text', '')
    for pattern in spring_patterns:
        if pattern in text:
            spring_indicators.append(pattern)

print('Spring patterns found:', set(spring_indicators))

print('__RESULT__:')
print('Analysis started')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:34': [], 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:39': 'file_storage/functions.query_db:39.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
