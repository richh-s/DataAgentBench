code = """import json
import re

# Read file contents directly
civic_docs = json.loads(open('/tmp/tmpq0c3uww8.json').read())
funding_data = json.loads(open('/tmp/tmphv6u7l7_.json').read())

print('Data loaded')

# Define a function to check if a string looks like a project name
def is_project_name(text):
    if len(text) < 10 or len(text) > 200:
        return False
    if text.startswith(('(', '•', '-', '□')):
        return False
    if any(x in text for x in ['Updates:', 'Schedule:', 'To:', 'Page', 'Agenda Item']):
        return False
    return any(ind in text for ind in ['Project', 'Improvements', 'Repairs', 'Replacement', 'Structure'])

# Extract park projects completed in 2022
park_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if document mentions 2022 completion
    if '2022' in text and ('completed' in text.lower() or 'completion' in text.lower()):
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            if is_project_name(line):
                # Check if it's park-related
                if 'park' in line.lower() or 'Park' in line:
                    # Look ahead for 2022 completion
                    context = '\n'.join(lines[i:i+15])
                    if '2022' in context and ('completed' in context.lower() or 'completion' in context.lower()):
                        park_projects.add(line)

print('Park projects found:', len(park_projects))
for p in sorted(park_projects):
    print('-', p)

# Create funding lookup
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    funding_lookup[name] = amount

# Match and sum funding
total_funding = 0
matched_projects = []

for project in park_projects:
    # Direct match
    if project in funding_lookup:
        total_funding += funding_lookup[project]
        matched_projects.append(project)
        continue
    
    # Partial match - check word overlap
    project_words = set(project.lower().replace('(', '').replace(')', '').split())
    
    for fund_name, amount in funding_lookup.items():
        fund_words = set(fund_name.lower().replace('(', '').replace(')', '').split())
        
        # Check if they share key words (at least 3 words, not counting common words)
        common_words = {'project', 'improvements', 'repairs', 'replacement', 'and', 'the', 'a', 'an', 'of', 'in', 'at', 'to', 'for', 'with'}
        
        proj_key = project_words - common_words
        fund_key = fund_words - common_words
        
        if len(proj_key.intersection(fund_key)) >= 2:  # At least 2 matching key words
            total_funding += amount
            matched_projects.append(project)
            break

print('Matched projects:', len(matched_projects))
print('Total funding:', total_funding)

# Return as string (since it's a simple number)
print('__RESULT__:')
print(total_funding)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
