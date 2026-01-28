code = """import json

# Access the query results
civic_docs_path = locals()['var_functions.query_db:51']
funding_path = locals()['var_functions.query_db:19']

# Load data
with open(civic_docs_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_data = json.load(f)

# Create funding lookup
funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name']] = int(item['Total_Amount'])

# Search for Spring 2022 projects
import re

spring_patterns = [
    r'2022[-\s]?Spring',
    r'2022[-\s]?March',
    r'2022[-\s]?April',
    r'2022[-\s]?May',
    r'Spring[-\s]?2022',
    r'March[-\s]?2022',
    r'April[-\s]?2022',
    r'May[-\s]?2022'
]

pattern = re.compile('|'.join(spring_patterns), re.IGNORECASE)

projects_found = set()

for doc in civic_docs:
    text = doc['text']
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        if pattern.search(section):
            lines = section.split('\n')
            for line in lines[:3]:
                line = line.strip()
                if (line and len(line) > 10 and 
                    not line.startswith('Page') and
                    'Agenda' not in line and
                    'Item' not in line):
                    
                    if line.istitle() or line.isupper() or '&' in line:
                        clean_name = re.sub(r'[^\w\s&-]', '', line)
                        clean_name = re.sub(r'\s+', ' ', clean_name).strip()
                        if len(clean_name) > 5:
                            projects_found.add(clean_name)
                            break

# Match with funding
total_funding = 0
matched_projects = []

for project in projects_found:
    amount = funding_lookup.get(project, 0)
    
    if amount == 0:
        # Try without suffixes
        base_name = re.sub(r'\s*\(FEMA.*\)|\s*\(CalOES.*\)|\s*\(CalJPIA.*\)', '', project).strip()
        amount = funding_lookup.get(base_name, 0)
    
    if amount > 0:
        total_funding += amount
        matched_projects.append({'name': project, 'funding': amount})

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [], 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:30': [{'Total_Funding': 'None'}], 'var_functions.query_db:48': [{'project_count': '1', 'total_funding': '38000'}], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json'}

exec(code, env_args)
