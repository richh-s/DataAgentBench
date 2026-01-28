code = """import json
import re
import pandas as pd

# Load the result from the previous query
result_file = var_functions.query_db:0
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        docs_data = json.load(f)
else:
    docs_data = var_functions.query_db:0

print("Number of documents retrieved:", len(docs_data))

# Function to extract project information from text
def extract_projects(text):
    projects = []
    
    # Look for project patterns with topic, status, dates
    # This is a simplified extraction - in practice you'd use more sophisticated NLP
    
    # Find sections that mention park and completed in 2022
    # Look for project descriptions with these patterns
    
    project_patterns = [
        r'([A-Za-z\s\-]+?Park[A-Za-z\s\-]+?)[\s\S]{0,200}?completed[\s\S]{0,200}?2022',
        r'([A-Za-z\s\-]+?)[\s\S]{0,200}?park[\s\S]{0,200}?completed[\s\S]{0,200}?2022',
        r'([A-Za-z\s\-]+?playground[A-Za-z\s\-]+?)[\s\S]{0,200}?completed[\s\S]{0,200}?2022',
    ]
    
    for pattern in project_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE)
        for match in matches:
            project_name = match.group(1).strip()
            # Clean up the project name
            project_name = re.sub(r'\s+', ' ', project_name)
            project_name = re.sub(r'\n', ' ', project_name)
            
            if len(project_name) < 100:  # Reasonable length
                projects.append({
                    'Project_Name': project_name,
                    'topic': 'park',
                    'status': 'completed',
                    'has_2022': True
                })
    
    return projects

# Extract projects from documents
all_projects = []
for doc in docs_data:
    projects = extract_projects(doc.get('text', ''))
    all_projects.extend(projects)

print("Extracted projects:", len(all_projects))
for i, proj in enumerate(all_projects[:10]):  # Show first 10
    print(f"{i+1}. {proj['Project_Name']}")

# Return the projects data
result = json.dumps(all_projects)
print("__RESULT__:")
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
