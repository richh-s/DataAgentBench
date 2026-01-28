code = """import json
import re

# Access the file paths
civic_docs_file = locals()['var_functions.query_db:22']
funding_file = locals()['var_functions.query_db:19']

# Read and parse the civic documents
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Read and parse the funding data
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create a funding lookup dictionary
funding_lookup = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Total_Amount'])
    funding_lookup[project_name] = amount

# Patterns for Spring 2022
spring_patterns = [
    r'2022[-\s]?Spring',
    r'2022[-\s]?March',
    r'2022[-\s]?April', 
    r'2022[-\s]?May',
    r'March[-\s]?2022',
    r'April[-\s]?2022',
    r'May[-\s]?2022',
    r'Spring[-\s]?2022'
]

pattern = re.compile('|'.join(spring_patterns), re.IGNORECASE)

# Extract projects with Spring 2022 start dates
spring_projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Find all mentions of Spring 2022 dates
    for match in pattern.finditer(text):
        # Get context around the date (100 chars before and after)
        start = max(0, match.start() - 100)
        end = min(len(text), match.end() + 100)
        context = text[start:end]
        
        # Try to find project name in context
        lines = context.split('\n')
        project_name = None
        
        for line in lines:
            line = line.strip()
            if (line and 
                len(line) > 10 and 
                len(line) < 150 and
                not line.startswith('Page') and
                'Agenda' not in line and
                'Item' not in line and
                'Capital Improvement' not in line and
                'RECOMMENDED' not in line and
                not re.match(r'^\d+\s*$', line)):
                
                # Likely project name indicators
                if (line.istitle() or 
                    line.isupper() or
                    '&' in line or
                    'Project' in line or
                    'Improvements' in line or
                    'Repair' in line or
                    'Drainage' in line or
                    'Road' in line):
                    
                    # Clean the name
                    project_name = re.sub(r'[^\w\s&-]', '', line)
                    project_name = re.sub(r'\s+', ' ', project_name).strip()
                    break
        
        if project_name:
            spring_projects.append({
                'project_name': project_name,
                'context': context.replace('\n', ' ')[:200]
            })

# Get unique project names
unique_projects = {}
for proj in spring_projects:
    name = proj['project_name']
    if name not in unique_projects:
        unique_projects[name] = proj

# Match with funding
def find_matching_funding(project_name, funding_lookup):
    # Exact match
    if project_name in funding_lookup:
        return project_name, funding_lookup[project_name]
    
    # Try without common suffixes
    base_name = re.sub(r'\s*\(FEMA.*\)$|\s*\(CalOES.*\)$|\s*\(CalJPIA.*\)$', '', project_name)
    if base_name in funding_lookup:
        return base_name, funding_lookup[base_name]
    
    # Try fuzzy matching
    for funded_name in funding_lookup:
        if base_name.lower() in funded_name.lower() or funded_name.lower() in base_name.lower():
            return funded_name, funding_lookup[funded_name]
    
    return None, None

# Find funding for each unique project
projects_with_funding = []
total_funding = 0

for project_name, project_data in unique_projects.items():
    matching_name, amount = find_matching_funding(project_name, funding_lookup)
    
    if matching_name and amount:
        projects_with_funding.append({
            'project_name': project_name,
            'funding_name': matching_name,
            'amount': amount
        })
        total_funding += amount

print("__RESULT__:")
print(json.dumps({
    "spring_2022_projects_count": len(projects_with_funding),
    "total_funding": total_funding,
    "projects": projects_with_funding[:20]  # First 20 for preview
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [], 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:30': [{'Total_Funding': 'None'}]}

exec(code, env_args)
