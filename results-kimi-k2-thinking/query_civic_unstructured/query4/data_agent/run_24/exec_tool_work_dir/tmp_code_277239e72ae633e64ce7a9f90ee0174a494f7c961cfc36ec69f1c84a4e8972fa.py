code = """import json
import re

# Load the civic documents from the file
file_path = var_functions.query_db:0
with open(file_path, 'r') as f:
    documents = json.load(f)

print(f"Loaded {len(documents)} documents")

# Function to extract projects with Spring 2022 start dates
spring_2022_projects = []

for doc in documents:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines or very short lines
        if not line or len(line) < 10:
            continue
        
        # Look for project names - capitalized lines containing project-related terms
        project_terms = ['project', 'improvements', 'repairs', 'facility', 'park', 'road', 'drainage', 'bridge', 'playground', 'treatment', 'wall', 'study', 'system', 'lane', 'structure']
        
        has_project_term = any(term in line.lower() for term in project_terms)
        is_capitalized = line[0].isupper() if line else False
        
        if has_project_term and is_capitalized:
            # Check if this line has date info itself or look ahead for date info
            project_name = line
            
            # Look for Spring 2022 in next few lines
            found_spring_2022 = False
            for j in range(i, min(i+10, len(lines))):
                check_line = lines[j].strip()
                
                # Check for Spring 2022 patterns
                if '2022' in check_line and ('Spring' in check_line or 'spring' in check_line or 'March' in check_line or 'April' in check_line or 'May' in check_line):
                    if any(keyword in check_line for keyword in ['Advertise', 'Begin', 'Start', 'Complete', 'Design', 'Construction']):
                        found_spring_2022 = True
                        break
            
            if found_spring_2022:
                spring_2022_projects.append(project_name)
                print(f"Found project: {project_name}")

# Count unique projects
unique_projects = list(set(spring_2022_projects))

print(f"\nTotal unique projects starting in Spring 2022: {len(unique_projects)}")

result = json.dumps({"count": len(unique_projects), "projects": unique_projects})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
