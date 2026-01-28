code = """import json
import re
from collections import defaultdict

# Load the civic documents data
civic_docs_path = var_functions.query_db:10
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:10

# Load the funding data
funding_path = var_functions.query_db:7
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = var_functions.query_db:7

# Create a mapping of project names to funding amounts
funding_map = {}
for record in funding_records:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_map[project_name] = amount

# Look for projects in the civic documents that started in Spring 2022
spring_2022_projects = []

# Define patterns to identify project names
project_pattern = r'([A-Z][a-zA-Z\s\d\-&]+?(?:Project|Improvements|Repairs|Drainage|Resurfacing|Structure|Facility|Study))'
fema_pattern = r'([A-Z][a-zA-Z\s\d\-&]+?(?:\(FEMA[^\)]*\)))'
caloes_pattern = r'([A-Z][a-zA-Z\s\d\-&]+?(?:\(CalOES[^\)]*\)))'
calpia_pattern = r'([A-Z][a-zA-Z\s\d\-&]+?(?:\(CalJPIA[^\)]*\)))'

# Define spring 2022 date patterns
spring_date_patterns = [
    r'2022\s*-\s*Spring',
    r'2022\s*-\s*March',
    r'2022\s*-\s*April', 
    r'2022\s*-\s*May',
    r'Spring\s*2022',
    r'March\s*2022',
    r'April\s*2022',
    r'May\s*2022'
]

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if this document contains Spring 2022
    has_spring_2022 = any(re.search(pattern, text, re.IGNORECASE) for pattern in spring_date_patterns)
    
    if has_spring_2022:
        # Find all potential project names in the text
        for pattern in [project_pattern, fema_pattern, caloes_pattern, calpia_pattern]:
            matches = re.finditer(pattern, text)
            for match in matches:
                project_name = match.group(1).strip()
                if project_name and len(project_name) > 10:
                    spring_2022_projects.append(project_name)

# Remove duplicates while preserving order
spring_2022_projects = list(dict.fromkeys(spring_2022_projects))

# Match projects with funding
project_funding = []
total_funding = 0

for project_name in spring_2022_projects:
    # Direct match
    if project_name in funding_map:
        funding = funding_map[project_name]
        if funding > 0:
            project_funding.append({
                'project_name': project_name,
                'funding': funding
            })
            total_funding += funding

# Count unique projects
num_projects = len(project_funding)

result = {
    'num_projects': num_projects,
    'total_funding': total_funding,
    'projects': project_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
