code = """import json
import re
import os

# Try to find the file from the environment or use a direct approach
# Let's list files in the current directory to find the json file
files = []
try:
    files = os.listdir('.')
    json_files = [f for f in files if f.endswith('.json')]
    # Look for the most recent json file
    if json_files:
        latest_file = max(json_files, key=os.path.getctime)
        civic_docs_file = latest_file
    else:
        # Try common temp locations
        temp_dirs = [os.path.expanduser('~/.divey/tmp'), '/tmp', '.']
        for temp_dir in temp_dirs:
            if os.path.exists(temp_dir):
                files = os.listdir(temp_dir)
                json_files = [f for f in files if f.endswith('.json') and 'civic' in f.lower()]
                if json_files:
                    civic_docs_file = os.path.join(temp_dir, json_files[0])
                    break
        else:
            # Last resort: try to read from the variable directly
            civic_docs_file = None
except Exception as e:
    civic_docs_file = None

# Load the civic documents
if civic_docs_file and os.path.exists(civic_docs_file):
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
else:
    # If file not found, let's try to work with what we have
    # This is a fallback - we'll need to query the database again
    print('__RESULT__:')
    print(json.dumps({'error': 'Could not load civic documents file', 'files_found': files}))
    exit()

# Function to identify disaster projects from text
def find_disaster_projects_2022(text):
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
            
        # Check if this line looks like a project name
        likely_project = False
        
        # Pattern 1: Ends with "Project"
        if line.endswith('Project'):
            likely_project = True
        # Pattern 2: Contains "Project:" 
        elif 'Project:' in line:
            likely_project = True
        # Pattern 3: Starts with year and contains Project
        elif line.startswith('2022') and 'Project' in line:
            likely_project = True
        # Pattern 4: Uppercase words ending with Project
        elif re.match(r'^[A-Z][A-Za-z\s]+Project$', line):
            likely_project = True
            
        if likely_project:
            # Check if this is disaster-related
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in ['fema', 'caljpia', 'caloes', 'disaster', 'fire', 'emergency', 'woolsey']):
                # Check for 2022 in surrounding lines
                context = ''
                start_idx = max(0, i-3)
                end_idx = min(len(lines), i+8)
                for j in range(start_idx, end_idx):
                    context += lines[j] + '\n'
                
                if '2022' in context:
                    projects.append(line)
    
    return projects

# Extract disaster projects
all_disaster_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    projects = find_disaster_projects_2022(text)
    all_disaster_projects.extend(projects)

# Also search for FEMA/CalJPIA/CalOES suffixes specifically
for doc in civic_docs:
    text = doc.get('text', '')
    # This pattern matches: Project Name (FEMA Project), etc.
    pattern = r'([A-Z][^\n(]*?)\s*\(([^)]*(?:FEMA|CalJPIA|CalOES)[^)]*Project)\)'
    matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
    
    for match in matches:
        proj_name = match[0].strip()
        # Check if 2022 appears near this project in the text
        if proj_name and len(proj_name) > 5:
            # Find position in text
            try:
                pos = text.index(match[0])
                context = text[max(0, pos-200):min(len(text), pos+200)]
                if '2022' in context:
                    all_disaster_projects.append(proj_name)
            except:
                all_disaster_projects.append(proj_name)

# Remove duplicates while preserving order
seen = set()
unique_projects = []
for proj in all_disaster_projects:
    if proj not in seen:
        seen.add(proj)
        unique_projects.append(proj)

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_2022': unique_projects,
    'count': len(unique_projects)
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
