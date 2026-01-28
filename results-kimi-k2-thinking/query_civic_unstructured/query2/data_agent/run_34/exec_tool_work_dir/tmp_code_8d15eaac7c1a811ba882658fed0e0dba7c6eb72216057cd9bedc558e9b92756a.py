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
    
    # Look for project sections
    # Capital Improvement Projects (Construction) section often contains completed projects
    # Look for patterns like project names followed by updates and schedules
    
    # Find project name lines (typically start with a project name, sometimes followed by updates)
    # This is a simplified extraction - in reality, the parsing is more complex
    
    # Look for patterns indicating completed projects in 2022
    # Pattern: "Construction was completed" followed by a date containing 2022
    completed_pattern = r'(\n|^)([A-Za-z\s]+)\n\(cid:\d+\) Updates:\n\(cid:\d+\) Construction was completed,\s+([^\n]+2022)'
    
    matches = re.findall(completed_pattern, text, re.IGNORECASE)
    
    for match in matches:
        project_name = match[1].strip()
        completion_date = match[2].strip()
        
        # Check if it's park-related
        if 'park' in project_name.lower():
            projects.append({
                'project_name': project_name,
                'completion_date': completion_date,
                'filename': filename,
                'topic': 'park',
                'status': 'completed',
                'et': completion_date
            })

# Also look for other patterns
# Pattern for projects with explicit status and dates
lines = text.split('\n')
for i, line in enumerate(lines):
    line = line.strip()
    # Look for project names that are capitalized and followed by status indicators
    if len(line) > 10 and line == line.upper() and ' ' in line:
        # Check if this is likely a project name
        # Look ahead for status and date information
        for j in range(i+1, min(i+10, len(lines))):
            next_line = lines[j].strip().lower()
            if 'construction was completed' in next_line and '2022' in next_line:
                # Check if park-related
                if 'park' in line.lower():
                    # Extract date
                    date_match = re.search(r'(\b\w+\s+2022\b)', next_line)
                    if date_match:
                        completion_date = date_match.group(1)
                        projects.append({
                            'project_name': line.strip(),
                            'completion_date': completion_date,
                            'filename': filename,
                            'topic': 'park',
                            'status': 'completed',
                            'et': completion_date
                        })
                break

# Remove duplicates
unique_projects = []
seen_names = set()
for proj in projects:
    if proj['project_name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['project_name'])

print("Park-related projects completed in 2022:")
for proj in unique_projects:
    print(f"- {proj['project_name']}: {proj['completion_date']}")

print(f"\nFound {len(unique_projects)} park-related projects completed in 2022")

# Save to JSON for querying funding
with open('/tmp/park_projects_2022.json', 'w') as f:
    json.dump(unique_projects, f, indent=2)

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
