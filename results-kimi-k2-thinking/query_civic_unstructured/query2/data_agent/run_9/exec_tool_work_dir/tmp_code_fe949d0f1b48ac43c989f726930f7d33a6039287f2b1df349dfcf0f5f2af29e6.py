code = """import json
import re

# Access the stored variable using locals()
storage_key = 'var_functions.query_db:2'
park_docs_result = locals()[storage_key]

print(f"Storage key: {storage_key}")
print(f"Result type: {type(park_docs_result)}")

# Load the full result from the file if it's a file path
if isinstance(park_docs_result, str) and '.json' in park_docs_result:
    file_path = park_docs_result
    print(f"Reading data from file: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        park_docs = json.load(f)
else:
    park_docs = park_docs_result

print(f"Total park-related documents: {len(park_docs)}")
if park_docs:
    print(f"First document keys: {list(park_docs[0].keys())}")

# Function to extract project information from text
def extract_projects_from_text(text):
    """Extract project information from document text"""
    projects = []
    
    # Look for patterns indicating park projects
    patterns = [
        # Pattern 1: Look for park project names and completion info
        r'([A-Za-z\s]+Park[A-Za-z\s]+?)\n(?:(?:.|\n)*?)(construction was completed|completed|Complete).*?2022',
        # Pattern 2: Generic park projects
        r'([A-Za-z\s]+Park[A-Za-z\s]*?(?:Improvements|Repair|Project|Structure))',
        # Pattern 3: Park-related projects with dates
        r'([A-Za-z\s]*?(?:Park|Playground)[A-Za-z\s]*?)\s+(?:.|\n)*?2022'
    ]
    
    # Also search line by line
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Look for park project names (lines containing 'Park' and other keywords)
        if 'Park' in line and len(line) > 10:
            # Check if this looks like a project name
            if any(keyword in line for keyword in ['Repair', 'Improvement', 'Project', 'Structure', 'Walkway', 'Playground']):
                # Look ahead for completion info
                completion_year = None
                status = None
                
                # Look ahead up to 10 lines
                for j in range(i+1, min(i+15, len(lines))):
                    next_line = lines[j].lower()
                    if '2022' in next_line:
                        if any(complete_marker in next_line for complete_marker in ['completed', 'construction was completed', 'notice of completion', 'complete']):
                            status = 'completed'
                            completion_year = '2022'
                            break
                
                if status == 'completed' and completion_year == '2022':
                    projects.append({
                        'Project_Name': line,
                        'status': status,
                        'topic': 'park',
                        'et': completion_year,
                        'type': 'capital'
                    })
    
    # Also use regex patterns on the whole text
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
        for match in matches:
            if isinstance(match, tuple):
                proj_name = match[0].strip()
            else:
                proj_name = match.strip()
            
            if proj_name and len(proj_name) > 5:
                # Check if completion info is in the surrounding text
                text_around = text[text.find(proj_name):text.find(proj_name)+500].lower()
                if any(complete_marker in text_around for complete_marker in ['completed', 'construction was completed', 'notice of completion']) and '2022' in text_around:
                    projects.append({
                        'Project_Name': proj_name,
                        'status': 'completed',
                        'topic': 'park',
                        'et': '2022',
                        'type': 'capital'
                    })
    
    return projects

# Extract projects from all documents
all_projects = []
print("\nExtracting projects from documents...")
for idx, doc in enumerate(park_docs):
    text = doc.get('text', '')
    projects = extract_projects_from_text(text)
    for proj in projects:
        proj['source_doc'] = doc.get('filename', f'doc_{idx}')
    all_projects.extend(projects)

print(f"Total projects extracted: {len(all_projects)}")

# Remove duplicates based on Project_Name
unique_projects = {}
for proj in all_projects:
    proj_name = proj['Project_Name']
    if proj_name not in unique_projects:
        unique_projects[proj_name] = proj

unique_park_2022_projects = list(unique_projects.values())
print(f"Unique park projects completed in 2022: {len(unique_park_2022_projects)}")

# Display the projects found
print("\nPark projects completed in 2022:")
for proj in unique_park_2022_projects:
    print(f"- {proj['Project_Name']} (from {proj.get('source_doc', 'unknown')})")

# Store results for next step
result_data = {
    'park_projects_2022': unique_park_2022_projects,
    'count': len(unique_park_2022_projects),
    'project_names': [p['Project_Name'] for p in unique_park_2022_projects]
}

print('__RESULT__:')
print(json.dumps(result_data, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
