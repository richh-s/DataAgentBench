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

# Define patterns to identify project names and start dates
project_patterns = [
    r'([A-Z][a-zA-Z\s\d\-&]+?(?:Project|Improvements|Repairs|Drainage|Resurfacing|Structure|Facility|Study))',
    r'([A-Z][a-zA-Z\s\d\-&]+?(?:\(FEMA[^\)]*\)))',
    r'([A-Z][a-zA-Z\s\d\-&]+?(?:\(CalOES[^\)]*\)))',
    r'([A-Z][a-zA-Z\s\d\-&]+?(?:\(CalJPIA[^\)]*\)))'
]

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
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        
        # Check if this line contains a Spring 2022 start date
        has_spring_2022 = any(re.search(pattern, line, re.IGNORECASE) for pattern in spring_date_patterns)
        
        if has_spring_2022:
            # Look for project names in nearby context (previous few lines or in this line)
            for pattern in project_patterns:
                matches = re.finditer(pattern, text)
                for match in matches:
                    project_name = match.group(1).strip()
                    if project_name and len(project_name) > 10:  # Filter out short matches
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
    else:
        # Try fuzzy matching - look for similar project names
        for funded_project, amount in funding_map.items():
            # Check if one name contains the other or similar
            if (project_name.lower() in funded_project.lower() or 
                funded_project.lower() in project_name.lower() or
                funded_project.replace('(FEMA Project)', '').strip() == project_name or
                funded_project.replace('(CalOES Project)', '').strip() == project_name):
                project_funding.append({
                    'project_name': project_name,
                    'funding': amount
                })
                total_funding += amount
                break

# Also look for projects that have "2022" in their name (like "2022 Morning View...")
additional_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find projects with 2022 in their name
    pattern = r'(\d{4}\s+[A-Z][a-zA-Z\s\d\-&]+?(?:Project|Improvements|Repairs|Drainage|Resurfacing|Structure|Facility|Study))'
    matches = re.finditer(pattern, text)
    
    for match in matches:
        if '2022' in match.group(1):
            project_name = match.group(1).strip()
            # Check if it's a Spring project (look for Spring/March/April/May in context)
            context_start = max(0, match.start() - 200)
            context = text[context_start:match.end() + 200]
            
            has_spring = any(re.search(pattern, context, re.IGNORECASE) for pattern in spring_date_patterns)
            
            if has_spring and project_name not in spring_2022_projects:
                additional_projects.append(project_name)

# Remove duplicates from additional projects
additional_projects = list(dict.fromkeys(additional_projects))

# Add additional projects to our list
for project_name in additional_projects:
    if project_name not in [p['project_name'] for p in project_funding]:
        # Check funding
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
