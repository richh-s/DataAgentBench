code = """import json
import re

# Read the civic documents from the file
civic_docs_file = var_functions.query_db:0
civic_docs = []

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Total civic documents: {len(civic_docs)}")

# Initialize list to store extracted project information
projects = []

# Iterate through each document
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for patterns indicating completed projects in 2022
    # Pattern 1: Look for "Construction was completed" with 2022 date
    pattern1 = r'Construction was completed[^\n]*2022'
    
    for match in re.finditer(pattern1, text, re.IGNORECASE):
        # Find the project name before this
        before_text = text[:match.start()]
        lines_before = before_text.split('\n')
        
        # Look backwards for a project name (likely not indented, not a status line)
        for line in reversed(lines_before[-15:]):  # Check last 15 lines
            line = line.strip()
            # Skip empty lines, status indicators, or lines that look like descriptions
            if (line and len(line) > 5 and ' ' in line and 
                not line.startswith('(') and not line.startswith('-') and 
                not line.lower().startswith('project') and
                'updates' not in line.lower() and
                'schedule' not in line.lower()):
                
                # Check if park-related
                if 'park' in line.lower():
                    # Extract the completion date from the match
                    date_match = re.search(r'(\w+\s+2022)', match.group())
                    if date_match:
                        completion_date = date_match.group(1)
                        projects.append({
                            'project_name': line,
                            'completion_date': completion_date,
                            'filename': filename,
                            'topic': 'park',
                            'status': 'completed',
                            'et': completion_date
                        })
                        break

# Remove duplicates based on project name
unique_projects = []
seen_names = set()

for proj in projects:
    # Clean up the project name (remove common suffixes/prefixes)
    clean_name = proj['project_name'].strip()
    if clean_name not in seen_names:
        unique_projects.append(proj)
        seen_names.add(clean_name)

print(f"Found {len(unique_projects)} unique park-related projects completed in 2022:")
for proj in unique_projects:
    print(f"  - {proj['project_name']} ({proj['completion_date']})")

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
