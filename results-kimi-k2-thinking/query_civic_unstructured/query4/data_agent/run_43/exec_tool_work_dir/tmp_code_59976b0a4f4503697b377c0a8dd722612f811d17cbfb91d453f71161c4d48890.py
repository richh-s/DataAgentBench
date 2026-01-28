code = """import json
import re

# Access the file paths
civic_docs_file = locals()['var_functions.query_db:22']

# Read and parse the civic documents
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Search for projects starting in Spring 2022
spring_patterns = [
    '2022-Spring', '2022-March', '2022-April', '2022-May',
    'Spring 2022', 'March 2022', 'April 2022', 'May 2022'
]

# Extract project names and their start times
projects_spring_2022 = []
all_start_times = []

for doc in civic_docs:
    text = doc['text']
    
    # First, try to extract project sections
    project_sections = re.split(r'\n\s*\n', text)
    
    for section in project_sections:
        if not section.strip():
            continue
            
        # Check if this section has a Spring 2022 start date
        has_spring_2022 = False
        date_found = None
        for pattern in spring_patterns:
            if re.search(pattern, section, re.IGNORECASE):
                has_spring_2022 = True
                date_found = pattern
                break
        
        if has_spring_2022:
            # Try to extract project name
            lines = section.split('\n')
            project_name = None
            
            for line in lines[:5]:
                line = line.strip()
                if not line or len(line) < 10:
                    continue
                if line.startswith('Page') or 'Agenda' in line or 'Item' in line or 'Capital Improvement' in line:
                    continue
                if re.match(r'^\d+\s*$', line):
                    continue
                
                # Check if it's a likely project name
                if (line.istitle() or sum(1 for c in line if c.isupper()) > len(line) * 0.3 or
                    '&' in line or 'Project' in line or 'Improvements' in line):
                    
                    project_name = line
                    break
            
            if project_name:
                # Clean up the project name
                project_name = re.sub(r'[^\w\s&-]', '', project_name)
                project_name = re.sub(r'\s+', ' ', project_name).strip()
                
                projects_spring_2022.append({
                    'project_name': project_name,
                    'start_date': date_found,
                    'filename': doc['filename']
                })
                all_start_times.append(date_found)

# Get unique project names
unique_projects = {}
for proj in projects_spring_2022:
    name = proj['project_name']
    if name not in unique_projects:
        unique_projects[name] = proj

print("__RESULT__:")
print(json.dumps({
    "total_mentions": len(all_start_times),
    "unique_projects_count": len(unique_projects),
    "unique_project_names": list(unique_projects.keys())
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [], 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'civic_docs_count': 5, 'funding_records_count': 500}}

exec(code, env_args)
