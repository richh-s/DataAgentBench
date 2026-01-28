code = """import json
import re

print("Starting query processing...")

# Get the data from variables
funding_data = var_functions.query_db:5
civic_docs = var_functions.query_db:2

print("Data loaded")
print("Funding records:", len(funding_data))
print("Civic docs:", len(civic_docs))

# Extract spring 2022 projects from text
spring_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and ('Spring' in text or 'spring' in text or '-03-' in text or '-04-' in text or '-05-' in text):
        spring_projects.append(doc)

print("Potential spring 2022 docs:", len(spring_projects))

# Count projects and funding (simplified approach - will refine)
spring_2022_project_names = []

for doc in spring_projects:
    text_lines = doc['text'].split('\n')[:50]
    for i, line in enumerate(text_lines):
        if 'Spring 2022' in line or '2022-Spring' in line:
            if i > 0:
                spring_2022_project_names.append(text_lines[i-1].strip())

print("Found project candidates:", len(spring_2022_project_names))

# Match with funding records
total_funding = 0
matched_names = []

for funding in funding_data:
    funding_name = funding['Project_Name']
    for project_name in spring_2022_project_names:
        if len(project_name) > 10:
            if funding_name.lower() in project_name.lower() or project_name.lower() in funding_name.lower():
                if funding_name not in matched_names:
                    matched_names.append(funding_name)
                    amount = int(funding['Amount'])
                    total_funding += amount
                    print(f"Matched: {funding_name}, Amount: {amount}")

result_count = len(matched_names)
print(f"Final: {result_count} projects, ${total_funding}")

# Output in required format
result = {"project_count": result_count, "total_funding": total_funding}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
