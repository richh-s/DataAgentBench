code = """import json
import re

# Load the full result from the file
file_path = var_functions.query_db:2
print(f"Reading data from: {file_path}")

with open(file_path, 'r', encoding='utf-8') as f:
    park_docs = json.load(f)

print(f"Total park-related documents: {len(park_docs)}")
print(f"First document keys: {list(park_docs[0].keys()) if park_docs else 'No documents'}")

# Function to extract project information from text
def extract_projects_from_text(text):
    """Extract project information from document text"""
    projects = []
    
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names - typically capitalized lines, often followed by status indicators
        # Try to find patterns like project names followed by specific markers
        
        # Pattern 1: Common project name formats
        if len(line) > 5 and line.isupper() and not line.startswith('(') and not line.startswith('cid:'):
            # This might be a project name
            if current_project:
                projects.append(current_project)
            
            current_project = {
                'Project_Name': line,
                'status': None,
                'topic': 'park',
                'st': None,
                'et': None,
                'type': 'capital',
                'text_excerpt': line
            }
        
        # Pattern 2: Look for status and date indicators in subsequent lines
        if current_project:
            # Check for completion dates
            if any(marker in line.lower() for marker in ['complete', 'construction was completed', 'completed']):
                if '2022' in line:
                    current_project['et'] = '2022'
                    current_project['status'] = 'completed'
            
            # Extract more context
            if len(current_project.get('text_excerpt', '')) < 500:
                current_project['text_excerpt'] += ' ' + line
    
    if current_project:
        projects.append(current_project)
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in park_docs:
    projects = extract_projects_from_text(doc.get('text', ''))
    all_projects.extend(projects)

print(f"Total projects extracted: {len(all_projects)}")

# Filter for park projects completed in 2022
park_2022_completed = [p for p in all_projects if p['et'] == '2022' and 'park' in p['topic'].lower()]
print(f"Park projects completed in 2022: {len(park_2022_completed)}")

for p in park_2022_completed[:5]:
    print(f"- {p['Project_Name']}: {p['status']}, {p['et']}")

# Let's also search more thoroughly in the text for park projects not captured
additional_park_projects = []
for doc in park_docs:
    text = doc.get('text', '')
    
    # Look for patterns indicating completed park projects in 2022
    patterns = [
        r'([^\n]+park[^\n]*?)\s+.*?construction was completed.*?2022',
        r'([^\n]+park[^\n]*?)\s+.*?completed.*?2022',
        r'([^\n]+park[^\n]*?)\s+.*?2022.*?completed'
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
        for match in matches:
            proj_name = match.split('\n')[0].strip()
            if proj_name and len(proj_name) > 5:
                additional_park_projects.append({
                    'Project_Name': proj_name,
                    'status': 'completed',
                    'topic': 'park',
                    'et': '2022',
                    'type': 'capital',
                    'source_doc': doc.get('filename', 'unknown')
                })

print(f"\nAdditional park projects found with regex: {len(additional_park_projects)}")
for p in additional_park_projects[:5]:
    print(f"- {p['Project_Name']}")

# Combine both approaches
all_park_2022 = park_2022_completed + additional_park_projects
print(f"\nTotal unique park projects completed in 2022: {len(all_park_2022)}")

# Store results for next step
result_data = {
    'park_projects_2022': all_park_2022,
    'count': len(all_park_2022)
}

print('__RESULT__:')
print(json.dumps(result_data, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
