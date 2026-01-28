code = """import json
import re

# Read the files
civic_docs_path = '/tmp/tmp2d2u8k1a.json'
funding_path = '/tmp/tmp0k5s9q8h.json'

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Loaded files')
print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_data))

# Create a mapping of project names to funding amounts
funding_map = {}
for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_map[project_name] = amount

print('\nSample funding map entries:')
count = 0
for name, amount in funding_map.items():
    if count < 5:
        print(f"  {name}: ${amount}")
        count += 1
    else:
        break

# Look for disaster projects in civic documents
# We'll search for patterns that indicate disaster projects
print('\nAnalyzing civic documents for disaster projects...')

# Patterns that indicate disaster projects
disaster_indicators = [
    '(FEMA Project)',
    '(CalJPIA Project)',
    '(CalOES Project)',
    'FEMA',
    'disaster',
    'emergency',
    'fire recovery'
]

# We'll extract project information from the text
projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract project sections - they often start with project names
    # and contain schedule information
    lines = text.split('\n')
    
    current_project = None
    project_start = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for lines that look like project names (often title case, not bullet points)
        if (len(line) > 10 and 
            not line.startswith('(') and 
            not line.startswith('•') and
            not line.startswith('-') and
            not line.startswith('Page') and
            not line.startswith('Agenda') and
            ':' not in line[:20] and
            line == line.title()):
            
            # Check if this is a disaster project
            is_disaster = any(indicator.lower() in line.lower() for indicator in disaster_indicators)
            
            if is_disaster:
                current_project = line
                # Look for schedule information in following lines
                for j in range(i+1, min(i+10, len(lines))):
                    next_line = lines[j].strip()
                    if 'Project Schedule:' in next_line or 'Schedule:' in next_line:
                        # Look for start date
                        for k in range(j+1, min(j+5, len(lines))):
                            sched_line = lines[k].strip()
                            if 'st:' in sched_line.lower() or 'start' in sched_line.lower():
                                project_start = sched_line
                                break
                        break
                    elif 'st:' in next_line.lower():
                        project_start = next_line
                        break
                
                # If we found a project with 2022 start, add it
                if current_project and project_start and '2022' in project_start:
                    projects_2022.append({
                        'name': current_project,
                        'start': project_start,
                        'filename': filename
                    })

print(f'
Found {len(projects_2022)} disaster projects with 2022 start:')
for p in projects_2022:
    print(f"  - {p['name']}")
    print(f"    Start: {p['start']}")
    print(f"    File: {p['filename']}")
    print()"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
