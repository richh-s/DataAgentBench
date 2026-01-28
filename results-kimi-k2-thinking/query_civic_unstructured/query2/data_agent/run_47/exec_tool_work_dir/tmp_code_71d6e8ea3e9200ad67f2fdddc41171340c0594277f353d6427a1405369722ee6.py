code = """import json
import re

# Load civic documents
civic_docs_file = locals()['var_functions.query_db:6']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Function to extract completed projects with 2022 dates
def extract_2022_completed_projects(doc_text):
    projects = []
    lines = doc_text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for project names (title case lines that are not metadata)
        if (len(line) > 10 and 
            not any(keyword in line.lower() for keyword in ['project description', 'project updates', 'project schedule', 
                                                          'recommended action', 'discussion:', 'public works', 'agenda'])
            and not line.startswith('•') and not line.startswith('-') and not line.startswith('(')):
            
            # Check if next few lines contain completion info with 2022
            next_lines = '\n'.join(lines[i+1:i+5]).lower()
            
            if 'complet' in next_lines and '2022' in next_lines:
                # Extract completion date
                date_match = re.search(r'(\w+\s+2022)', next_lines, re.IGNORECASE)
                if date_match:
                    completion_date = date_match.group(1)
                    
                    # Check if park-related
                    is_park = 'park' in line.lower() or 'playground' in line.lower()
                    
                    projects.append({
                        'Project_Name': line,
                        'completion_date': completion_date,
                        'is_park': is_park
                    })
    
    return projects

# Extract all 2022 completed projects
all_projects = []
for doc in civic_docs:
    projects = extract_2022_completed_projects(doc['text'])
    all_projects.extend(projects)

print(f"Found {len(all_projects)} projects completed in 2022")

# Show park projects
park_projects = [p for p in all_projects if p['is_park']]
print(f"Park-related projects: {len(park_projects)}")
for proj in park_projects:
    print(f"  - {proj['Project_Name']} ({proj['completion_date']})")

result = {
    'all_projects': all_projects,
    'park_projects': park_projects
}

print('__RESULT__:', json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'status': 'loaded', 'count': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': {'file_path': 'file_storage/functions.query_db:6.json', 'doc_count': 5}}

exec(code, env_args)
