code = """import json
import re

# Get file paths from previous queries
civic_docs_path = locals()['var_functions.query_db:22']
funding_path = locals()['var_functions.query_db:19']

# Load data
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_list = json.load(f)

# Create funding lookup dictionary
funding_lookup = {}
for item in funding_list:
    funding_lookup[item['Project_Name']] = int(item['Total_Amount'])

# Define Spring 2022 patterns
spring_patterns = re.compile(r'2022[-\s]?(Spring|March|April|May)|(?:Spring|March|April|May)[-\s]?2022', re.IGNORECASE)

spring_projects = set()

# Extract projects mentioning Spring 2022
for doc in civic_docs:
    text = doc['text']
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        if spring_patterns.search(section):
            lines = section.split('\n')
            for line in lines[:5]:
                line = line.strip()
                if line and 10 < len(line) < 150:
                    if line.istitle() or line.isupper() or '&' in line:
                        cleaned = re.sub(r'[^\w\s&-]', '', line)
                        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
                        spring_projects.add(cleaned)
                        break

# Match with funding
def find_funding(project_name):
    if project_name in funding_lookup:
        return funding_lookup[project_name]
    
    base_name = re.sub(r'\s*\(FEMA.*\)|\s*\(CalOES.*\)|\s*\(CalJPIA.*\)', '', project_name)
    if base_name in funding_lookup:
        return funding_lookup[base_name]
    
    for funded_name in funding_lookup:
        if base_name.lower() in funded_name.lower():
            return funding_lookup[funded_name]
    
    return 0

# Calculate total funding
total_funding = 0
projects_with_funding = []

for project in spring_projects:
    amount = find_funding(project)
    if amount > 0:
        total_funding += amount
        projects_with_funding.append({'project': project, 'funding': amount})

result = {
    "project_count": len(projects_with_funding),
    "total_funding": total_funding,
    "projects": projects_with_funding
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [], 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:30': [{'Total_Funding': 'None'}]}

exec(code, env_args)
