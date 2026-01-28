code = """import json
import re

# Access the civic documents data
civic_docs = var_functions.query_db:2
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs_data = json.load(f)
else:
    civic_docs_data = civic_docs

# Access the funding data  
funding = var_functions.query_db:5
if isinstance(funding, str) and funding.endswith('.json'):
    with open(funding, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding

print(f"Number of civic documents: {len(civic_docs_data)}")
print(f"Number of funding records: {len(funding_data)}")
print("\nFirst few funding records:")
for i, record in enumerate(funding_data[:5]):
    print(f"  {i+1}. {record['Project_Name']}: ${record['Amount']}")

# Extract projects from civic documents with Spring 2022 start dates
spring_2022_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    # Look for project patterns with dates
    # Common patterns: project name followed by date info
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        # Check if this line mentions a Spring 2022 date
        if '2022-Spring' in line or '2022-March' in line or '2022-April' in line or '2022-May' in line:
            # Look backwards for project name (previous lines)
            project_name = None
            for j in range(i-1, max(i-5, -1), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and not prev_line.startswith('●') and len(prev_line) > 5:
                    if 'Project Schedule' not in prev_line and 'Updates' not in prev_line and 'Complete Design' not in prev_line:
                        project_name = prev_line
                        break
            
            if project_name:
                # Clean up common formatting artifacts
                project_name = project_name.replace('●', '').replace('■', '').strip()
                if project_name and not project_name.startswith('_') and len(project_name) > 5:
                    spring_2022_projects.append({
                        'Project_Name': project_name,
                        'Source_Document': doc.get('filename', ''),
                        'Date_Context': line.strip()
                    })

print(f"\nFound {len(spring_2022_projects)} potential Spring 2022 projects in civic documents")
if spring_2022_projects:
    print("Sample projects:")
    for proj in spring_2022_projects[:10]:
        print(f"  - {proj['Project_Name'][:80]}...")

# Try a different approach - extract all project names from the documents
all_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    # Look for common project headings
    patterns = [
        r'^[A-Z][a-zA-Z\s&\-]+Project\s*$',
        r'^[A-Z][a-zA-Z\s&\-]+Improvements\s*$', 
        r'^[A-Z][a-zA-Z\s&\-]+Repairs\s*$',
        r'^[A-Z][a-zA-Z\s&\-]+Replacement\s*$'
    ]
    
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        for pattern in patterns:
            if re.match(pattern, line) and len(line) > 10:
                if 'City Council' not in line and 'Public Works' not in line and 'Commission' not in line:
                    all_projects.append(line)

print(f"\nFound {len(set(all_projects))} unique project-style headings")
print("Sample project headings:")
for proj in list(set(all_projects))[:10]:
    print(f"  - {proj}")

# Save results for next step
result = {
    'spring_2022_projects': spring_2022_projects,
    'all_project_headings': list(set(all_projects)),
    'funding_data': funding_data
}

import sys
result_json = json.dumps(result, indent=2)[:50000]  # Limit size
print('\n__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
