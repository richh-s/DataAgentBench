code = """import json
import re

funding_data = locals()['var_functions.query_db:5']
civic_docs = locals()['var_functions.query_db:2']

print("Processing", len(civic_docs), "documents and", len(funding_data), "funding records")

spring_2022_projects = []

for doc in civic_docs:
    text = doc['text'].lower()
    # Check if document contains spring 2022 references
    if 'spring 2022' in text or '2022-spring' in text:
        lines = doc['text'].split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if 'Spring 2022' in lines[i] or '2022-Spring' in lines[i]:
                # Look backwards for project name (non-empty line)
                for j in range(i-1, max(0, i-6), -1):
                    prev_line = lines[j].strip()
                    if prev_line and len(prev_line) > 10 and not prev_line.startswith('('):
                        spring_2022_projects.append(prev_line)
                        break

print("Found project candidates:", len(spring_2022_projects))

# Match with funding
total_funding = 0
project_count = 0
used_projects = set()

for funding in funding_data:
    funding_name = funding['Project_Name']
    for proj in spring_2022_projects:
        # Simple matching - check if either contains the other
        if funding_name in proj or proj in funding_name:
            if funding_name not in used_projects:
                used_projects.add(funding_name)
                total_funding += int(funding['Amount'])
                project_count += 1
                break

result = {"project_count": project_count, "total_funding": total_funding}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
