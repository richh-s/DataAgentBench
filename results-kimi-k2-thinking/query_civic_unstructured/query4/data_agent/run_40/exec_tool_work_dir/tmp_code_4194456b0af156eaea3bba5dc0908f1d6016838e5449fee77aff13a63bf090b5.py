code = """import json
import re

# Access variables more carefully
funding_data = globals().get('var_functions.query_db:5', locals().get('var_functions.query_db:5'))
civic_docs = globals().get('var_functions.query_db:2', locals().get('var_functions.query_db:2'))

# Debug print - careful about variable naming
print("Funding type:", type(funding_data))
print("Civic type:", type(civic_docs))

# Simple processing to extract project info
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '').lower()
    # Check for spring 2022 indicators
    if 'spring 2022' in text or '2022-spring' in text or re.search('2022-(03|04|05)', text):
        # Look for project names - these are typically capitalized lines
        lines = doc.get('text', '').split('\n')
        for i, line in enumerate(lines):
            # Spring 2022 found in this line or nearby
            has_spring = bool(re.search('spring 2022|2022-spring|2022-(03|04|05)', line, re.IGNORECASE))
            if has_spring:
                # Look before for project name
                for j in range(max(0, i-5), i):
                    prev_line = lines[j].strip()
                    if prev_line and not prev_line.startswith('(') and len(prev_line) > 15:
                        spring_2022_projects.add(prev_line)
                        break

# Now match these projects with funding
project_count = 0
total_funding = 0
matched_projects = set()

for project in spring_2022_projects:
    for funding in funding_data:
        funding_name = funding['Project_Name']
        # Match criteria
        if funding_name.lower() in project.lower() or project.lower() in funding_name.lower():
            matched_projects.add(funding_name)
            total_funding += int(funding['Amount'])
            project_count += 1

# Remove duplicates for actual count
final_count = len(matched_projects)

print("Result:", final_count, "projects with total funding", total_funding)

# Format the output properly
import sys
result = {"project_count": final_count, "total_funding": total_funding}
sys.stdout.write('__RESULT__:\n')
sys.stdout.write(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
