code = """import json
import re

result_file = '/tmp/tmpql5q6l6p.json'

# Load the JSON data from the file
with open(result_file, 'r') as f:
    docs_data = json.load(f)

print("Successfully loaded documents:", len(docs_data))

# Function to find park projects completed in 2022
def find_park_projects(text):
    projects = []
    text_lower = text.lower()
    
    # Check for required keywords
    has_park_terms = any(term in text_lower for term in ['park', 'playground'])
    has_completed = 'completed' in text_lower
    has_2022 = '2022' in text_lower
    
    if not (has_park_terms and has_completed and has_2022):
        return projects
    
    # Extract specific project mentions
    # Look for common patterns
    patterns = [
        r'([A-Za-z\s]+Park[A-Za-z\s]*)[^.]*?completed[^.]*2022',
        r'([A-Za-z\s]+Playground[A-Za-z\s]*)[^.]*?completed[^.]*2022',
        r'[^.]*park[^.]*?completed[^.]*2022',
    ]
    
    for pattern in patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            # Extract a reasonable project name
            project_text = match.group(0)
            # Get first few words as project name
            words = project_text.split()
            if len(words) > 0:
                proj_name = ' '.join(words[:8])
                projects.append({
                    'Project_Name': proj_name,
                    'topic': 'park',
                    'status': 'completed',
                    'year': '2022'
                })
                break  # One per section
    
    return projects

# Extract from all documents
all_projects = []
for doc in docs_data:
    projects = find_park_projects(doc.get('text', ''))
    all_projects.extend(projects)

# Deduplicate based on project name
unique_projects = []
seen_names = set()
for proj in all_projects:
    if proj['Project_Name'] not in seen_names:
        seen_names.add(proj['Project_Name'])
        unique_projects.append(proj)

print("Found unique projects:", len(unique_projects))

# Display some projects
for i, proj in enumerate(unique_projects[:20]):
    print(f"{i+1}. {proj['Project_Name']}")

result = json.dumps(unique_projects)
print("__RESULT__:")
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
