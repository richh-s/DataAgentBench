code = """import json
import os
import re

# Load the MongoDB results
result_file = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_32.json'
with open(result_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Total documents with 2022: {len(civic_docs)}")

spring_2022_projects = set()

# Look for Spring 2022 indicators
spring_indicators = [
    '2022-Spring',
    'Spring-2022',
    'Spring 2022',
    '2022-03', '2022-04', '2022-05',
    '2022-Mar', '2022-Apr', '2022-May',
    'Mar 2022', 'Apr 2022', 'May 2022',
    'March 2022', 'April 2022', 'May 2022'
]

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip empty lines
        if not line:
            continue
            
        # Look for project names (uppercase or containing year)
        is_potential_project = False
        if line.isupper() and len(line) > 15:
            # Skip headers
            if not any(skip in line for skip in ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'MEETING', 'SUBJECT:', 'RECOMMENDED ACTION:', 'PREPARED BY', 'APPROVED BY']):
                is_potential_project = True
        elif '2022' in line and len(line) > 10:
            if not any(skip in line for skip in ['Page', 'AGENDA', 'Subject:', 'Prepared by:', 'Approved by:']):
                is_potential_project = True
        
        if is_potential_project:
            # Look ahead for schedule info
            look_ahead = ' '.join(lines[i:i+15])
            
            # Check if this project has Spring 2022 date
            has_spring_2022 = any(indicator in look_ahead for indicator in spring_indicators)
            
            # Also check for Advertise/Begin with Spring 2022
            if not has_spring_2022:
                # Look for patterns like "Advertise: Spring 2022" or "Begin: Spring 2022"
                spring_pattern = re.compile(r'(Advertise|Begin|Start|Complete)[^\n]{0,50}(?:Spring|Mar|Apr|May)[^\n]{0,50}2022', re.IGNORECASE)
                if spring_pattern.search(look_ahead):
                    has_spring_2022 = True
            
            if has_spring_2022:
                spring_2022_projects.add(line)

project_list = sorted(list(spring_2022_projects))
print(f"Spring 2022 projects: {len(project_list)}")
print("Projects:")
for proj in project_list:
    print(f"  - {proj}")

result = {'count': len(project_list), 'projects': project_list}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
