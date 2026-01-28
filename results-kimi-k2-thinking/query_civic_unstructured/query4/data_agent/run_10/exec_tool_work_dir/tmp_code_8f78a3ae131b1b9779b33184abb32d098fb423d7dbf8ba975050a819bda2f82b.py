code = """import json
import re

# Load civic documents
civic_file = locals()['var_functions.query_db:4']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_file = locals()['var_functions.query_db:8']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create funding lookup
funding_lookup = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[project_name] = amount

print("Analysis of civic documents:")
print(f"Number of documents: {len(civic_docs)}")

# Look for Spring 2022 references in the text
spring_2022_projects = []
spring_2022_patterns = [
    r'Spring\s+2022',
    r'2022-Spring',
    r'March\s+2022',
    r'April\s+2022',
    r'May\s+2022',
    r'2022-March',
    r'2022-April',
    r'2022-May'
]

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for any Spring 2022 mentions
    for pattern in spring_2022_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            # Extract context around the match
            start = max(0, match.start() - 200)
            end = min(len(text), match.end() + 200)
            context = text[start:end]
            
            # Try to find project name in this context
            # Look for common project name patterns
            project_patterns = [
                r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s+Project)?)',
                r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s+Improvements)?)',
                r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s+Repair)?)',
                r'(\d{4}\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)'  # e.g., "2022 Morning View..."
            ]
            
            for proj_pattern in project_patterns:
                proj_matches = re.finditer(proj_pattern, context)
                for proj_match in proj_matches:
                    project_name = proj_match.group(1).strip()
                    if len(project_name) > 5 and not project_name.startswith('Page'):
                        spring_2022_projects.append({
                            'project_name': project_name,
                            'filename': filename,
                            'context': context[:100]
                        })

print(f"Found {len(spring_2022_projects)} potential Spring 2022 projects")

# Show unique projects
unique_projects = list(set([p['project_name'] for p in spring_2022_projects]))
print(f"Unique projects: {len(unique_projects)}")
for proj in unique_projects[:10]:
    print(f"  - {proj}")

print("__RESULT__:")
print(json.dumps({
    "potential_projects": len(spring_2022_projects),
    "unique_projects": len(unique_projects),
    "sample_projects": unique_projects[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}}

exec(code, env_args)
