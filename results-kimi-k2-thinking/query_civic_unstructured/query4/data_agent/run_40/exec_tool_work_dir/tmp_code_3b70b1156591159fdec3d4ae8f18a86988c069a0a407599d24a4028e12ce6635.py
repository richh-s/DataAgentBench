code = """import json
import re

# Get data directly by reading from the JSON files
import os

# Try to find our data files
funding_path = None
civic_path = None

for root, dirs, files in os.walk('/'):
    for file in files:
        if 'query_db:5' in file:
            funding_path = os.path.join(root, file)
        elif 'query_db:2' in file:
            civic_path = os.path.join(root, file)

print("Funding path:", funding_path)
print("Civic path:", civic_path)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print("Loaded:", len(funding_data), "funding,", len(civic_docs), "civic docs")

# Extract Spring 2022 projects
spring_2022_names = []
for doc in civic_docs:
    text = doc['text']
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if 'Spring 2022' in line or '2022-Spring' in line:
                # Look for project name (typically previous non-empty line)
                for j in range(min(i, 5)):
                    idx = i - j - 1
                    if idx >= 0 and lines[idx].strip():
                        proj_name = lines[idx].strip()
                        if len(proj_name) > 5 and not proj_name.startswith('('):
                            spring_2022_names.append(proj_name)
                            break

print("Spring 2022 candidates:", len(spring_2022_names))

# Match with funding
total = 0
count = 0
matched = set()

for funding in funding_data:
    f_name = funding['Project_Name']
    for proj in spring_2022_names:
        # Match if either contains the other (partial match)
        if f_name in proj or proj in f_name or any(word in f_name for word in proj.split() if len(word) > 4):
            if f_name not in matched:
                matched.add(f_name)
                total += int(funding['Amount'])
                count += 1
                break

result = {"project_count": count, "total_funding": total}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
