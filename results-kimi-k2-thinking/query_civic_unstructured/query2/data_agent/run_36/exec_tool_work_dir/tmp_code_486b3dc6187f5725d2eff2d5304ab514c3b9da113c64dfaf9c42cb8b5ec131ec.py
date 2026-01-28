code = """import json
import re

# Load the result from the previous query
result_data = var_functions.query_db:0

# Handle both file path (string) and direct data (list)
if isinstance(result_data, str) and 'json' in result_data:
    with open(result_data, 'r') as f:
        docs_data = json.load(f)
else:
    docs_data = result_data

print("Number of documents retrieved:", len(docs_data))

# Function to extract park projects completed in 2022
def extract_park_projects(text):
    projects = []
    text_lower = text.lower()
    
    # Check if text contains required keywords
    has_park = any(term in text_lower for term in ['park', 'playground'])
    has_completed = 'completed' in text_lower
    has_2022 = '2022' in text_lower
    
    if not (has_park and has_completed and has_2022):
        return projects
    
    # Split text into sections
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        section_lower = section.lower()
        
        # Check for park/playground with completed and 2022
        if ('park' in section_lower or 'playground' in section_lower) and 'completed' in section_lower and '2022' in section_lower:
            lines = section.strip().split('\n')
            for line in lines:
                line_clean = line.strip()
                if line_clean and len(line_clean) > 5:
                    project_name = line_clean
                    if not re.match(r'.*\d{4}.*', project_name[:50]):
                        projects.append({
                            'Project_Name': project_name[:100],
                            'topic': 'park',
                            'status': 'completed',
                            'year': '2022'
                        })
                        break
    
    return projects

# Extract projects
all_projects = []
for doc in docs_data:
    projects = extract_park_projects(doc.get('text', ''))
    all_projects.extend(projects)

# Deduplicate
unique_projects = []
seen = set()
for proj in all_projects:
    if proj['Project_Name'] not in seen:
        seen.add(proj['Project_Name'])
        unique_projects.append(proj)

print("Unique park projects in 2022:", len(unique_projects))
for i, proj in enumerate(unique_projects[:15]):
    print(f"{i+1}. {proj['Project_Name']}")

result = json.dumps(unique_projects)
print("__RESULT__:")
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
