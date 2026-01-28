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
    
    # Look for patterns indicating completed projects with dates containing 2022
    # Pattern 1: Look for completed projects with "Construction was completed" or similar
    pattern1 = r'Construction was completed[^.\n]*?(\w+\s+2022)'
    matches1 = re.findall(pattern1, text, re.IGNORECASE)
    
    if matches1:
        # Find the project name before this completion statement
        # Look backwards from the completion statement
        for match in re.finditer(pattern1, text, re.IGNORECASE):
            completion_date = match.group(1)
            # Get text before this match
            before_text = text[:match.start()]
            # Look for project name in the preceding lines
            # Project names are typically on their own line before updates
            lines_before = before_text.split('\n')
            for line in reversed(lines_before[-20:]):  # Check last 20 lines
                line = line.strip()
                # Look for what might be a project name (not empty, not status indicators)
                if line and len(line) > 5 and ' ' in line and not line.startswith('(') and not line.startswith('-'):
                    # Check if park-related
                    if 'park' in line.lower():
                        projects.append({
                            'project_name': line,
                            'completion_date': completion_date,
                            'filename': filename,
                            'topic': 'park',
                            'status': 'completed',
                            'et': completion_date
                        })
                        break
    
    # Pattern 2: Look for project list items with explicit dates
    # This matches patterns like "Project Name\nUpdates: ...\nComplete: Month Year"
    pattern2 = r'([A-Z][A-Za-z\s]+)\s*\n\(cid:\d+\) Updates?:[^\n]*\n\(cid:\d+\) Complete(?:d)?:\s*(\w+\s+2022)'
    matches2 = re.findall(pattern2, text)
    
    for proj_name, comp_date in matches2:
        if 'park' in proj_name.lower():
            projects.append({
                'project_name': proj_name.strip(),
                'completion_date': comp_date,
                'filename': filename,
                'topic': 'park',
                'status': 'completed',
                'et': comp_date
            })

# Remove duplicates based on project name
unique_projects = []
seen_names = set()
for proj in projects:
    if proj['project_name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['project_name'])

print(f"Found {len(unique_projects)} park-related projects completed in 2022:")
for proj in unique_projects:
    print(f"- {proj['project_name']}: {proj['completion_date']}")

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
