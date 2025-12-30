code = """import json
import re

with open(locals()['var_function-call-9226438263479244870'], 'r') as f:
    documents = json.load(f)

disaster_projects_2022_names = []

for doc in documents:
    text = doc['text']
    
    lines = text.split('\\n')
    
    for i, line in enumerate(lines):
        if "type: disaster" in line:
            # Found a disaster project type. Now look for 'st: 2022' in subsequent lines
            # and then a project name in preceding lines.
            
            # Search forward for 'st: 2022'
            found_2022_start = False
            for j in range(i, min(i + 10, len(lines))): # Look within next 10 lines
                if "st: 2022" in lines[j]:
                    found_2022_start = True
                    break
            
            if found_2022_start:
                # Search backward for Project Name
                # Project name is usually a capitalized line, not starting with bullet points, etc.
                for k in range(i - 1, -1, -1):
                    prev_line = lines[k].strip()
                    if prev_line and not prev_line.startswith('(cid:') and not re.match(r'^(Page \\d+ of \\d+|Agenda Item # \\d+\\.[A-Z]|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION:|DISCUSSION:)$', prev_line):
                        # This could be a project name. Add it and break.
                        disaster_projects_2022_names.append(prev_line)
                        break
                        
# Remove duplicates
disaster_projects_2022_names = list(set(disaster_projects_2022_names))

# Filter project names, remove generic headers that might be misidentified.
# Manual filtering based on observation of the extracted project names
# This is a heuristic and might need adjustment.
filtered_projects = []
for project in disaster_projects_2022_names:
    if not (project.lower().startswith('capital improvement projects') or
            project.lower().startswith('disaster recovery projects') or
            project.lower().startswith('public works commission') or
            project.lower().startswith('agenda report') or
            project.lower().startswith('public works') or
            project.lower().startswith('item') or
            project.lower().startswith('to:') or
            project.lower().startswith('prepared by:') or
            project.lower().startswith('approved by:') or
            project.lower().startswith('date prepared:') or
            project.lower().startswith('meeting date:') or
            project.lower().startswith('subject:') or
            project.lower().startswith('recommended action:') or
            project.lower().startswith('discussion:')):
        filtered_projects.append(project)

print("__RESULT__:")
print(json.dumps(filtered_projects))"""

env_args = {'var_function-call-14874373830466001573': ['civic_docs'], 'var_function-call-6587384332537770908': [], 'var_function-call-9226438263479244870': 'file_storage/function-call-9226438263479244870.json'}

exec(code, env_args)
