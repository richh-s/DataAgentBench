code = """import json
import re

# Load civic documents from the stored file
docs_file = locals()['var_functions.query_db:12']
with open(docs_file, 'r') as f:
    documents = json.load(f)

print("Number of civic documents:", len(documents))
print("First document filename:", documents[0]['filename'])

# Function to parse project information from document text
def parse_projects_from_text(text, filename):
    projects = []
    
    # Look for disaster-related projects with 2022 start dates
    # Search for patterns like "(FEMA Project)", "(CalOES Project)", "(CalJPIA Project)"
    # and check for 2022 in the text near them
    
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names with disaster indicators
        # Pattern: project name followed by (FEMA Project) or similar
        if '(FEMA Project)' in line or '(CalOES Project)' in line or '(CalJPIA Project)' in line:
            # Extract project name
            project_name = line.strip()
            
            # Check if this project has 2022 start date in nearby text
            # Look at next few lines for date information
            nearby_text = ' '.join(lines[i:i+20])
            
            # Check for 2022 in start dates (st field)
            has_2022 = False
            if '2022' in nearby_text:
                # Look for start date patterns
                start_patterns = [
                    r'(?:Start|Schedule|Timeline).{0,100}2022',
                    r'Begin\s*(?:Construction|Design).{0,100}2022',
                    r'2022\s*(?:Spring|Fall|Summer|Winter)',
                    r'(?:Spring|Fall|Summer|Winter)\s*2022'
                ]
                
                for pattern in start_patterns:
                    if re.search(pattern, nearby_text, re.IGNORECASE):
                        has_2022 = True
                        break
            
            # Also check filename for date patterns
            if '2022' in filename:
                has_2022 = True
            
            if has_2022:
                projects.append({
                    'Project_Name': project_name,
                    'type': 'disaster',
                    'st': '2022',
                    'source': filename
                })
    
    # Also look for disaster-related keywords in project descriptions
    disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'recovery', 'fire']
    
    # Simple heuristic: if line looks like a project name (uppercase, starts with bullet or is short)
    # and contains disaster keywords, and 2022 appears nearby
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and common headers
        if not line or line.startswith('---') or line.startswith('==='):
            continue
            
        # Check if line might be a project name (not too long, starts with capital, may have numbers)
        if (len(line) < 150 and 
            (line[0].isupper() or line.startswith('•') or line.startswith('·') or 
             re.match(r'^\d+', line))):
            
            # Check for disaster keywords
            has_disaster_keyword = any(keyword.lower() in line.lower() for keyword in disaster_keywords)
            
            if has_disaster_keyword:
                # Look for 2022 in nearby context
                nearby_text = ' '.join(lines[max(0, i-5):i+20])
                if '2022' in nearby_text or '2022' in filename:
                    projects.append({
                        'Project_Name': line.strip('•·- '),
                        'type': 'disaster',
                        'st': '2022',
                        'source': filename
                    })
    
    return projects

# Parse all documents
all_projects = []
for doc in documents:
    projects = parse_projects_from_text(doc['text'], doc['filename'])
    all_projects.extend(projects)

print("\nExtracted projects:")
for p in all_projects[:10]:
    print(f"- {p['Project_Name']}")

print(f"\nTotal disaster projects with 2022: {len(all_projects)}")

# Save results
result = {
    'project_count': len(all_projects),
    'projects': all_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'doc_count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'filename': 'malibucity_agenda_03222023-2060.txt'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
