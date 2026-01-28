code = """import json
import re

# Load the result from the previous query - handle both direct data and file path
raw_result = var_functions.query_db:0

if isinstance(raw_result, str) and '.json' in raw_result:
    # It's a file path
    with open(raw_result, 'r') as f:
        docs_data = json.load(f)
else:
    # It's direct data
    docs_data = raw_result

print("Number of documents retrieved:", len(docs_data))

# Function to extract park projects completed in 2022
def extract_park_projects(text):
    projects = []
    text_lower = text.lower()
    
    # Check if text contains both park-related terms, "completed", and "2022"
    has_park = any(term in text_lower for term in ['park', 'playground'])
    has_completed = 'completed' in text_lower
    has_2022 = '2022' in text_lower
    
    if not (has_park and has_completed and has_2022):
        return projects
    
    # Look for project sections - a simplified approach
    # Split by common project markers
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        section_lower = section.lower()
        
        # Look for park-related keywords and completed and 2022 in same section
        if all(term in section_lower for term in ['park', 'completed', '2022']) or \
           all(term in section_lower for term in ['playground', 'completed', '2022']):
            
            # Try to extract project name (first line or first few words)
            lines = section.strip().split('\n')
            if lines:
                # Get first non-empty line as potential project name
                for line in lines:
                    if line.strip() and len(line.strip()) > 5:
                        project_name = line.strip()
                        # Don't include dates as project names
                        if not re.match(r'.*\d{4}.*', project_name[:50]):
                            projects.append({
                                'Project_Name': project_name[:100],  # Limit length
                                'topic': 'park',
                                'status': 'completed',
                                'year': '2022'
                            })
                            break
    
    return projects

# Extract projects from documents
all_projects = []
for doc in docs_data:
    projects = extract_park_projects(doc.get('text', ''))
    all_projects.extend(projects)

print("Raw extracted projects:", len(all_projects))

# Deduplicate projects
unique_projects = []
seen_names = set()
for proj in all_projects:
    if proj['Project_Name'] not in seen_names:
        seen_names.add(proj['Project_Name'])
        unique_projects.append(proj)

print("Unique projects:", len(unique_projects))
for i, proj in enumerate(unique_projects[:15]):
    print(f"{i+1}. {proj['Project_Name']}")

# Return the projects data
result = json.dumps(unique_projects)
print("__RESULT__:")
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
