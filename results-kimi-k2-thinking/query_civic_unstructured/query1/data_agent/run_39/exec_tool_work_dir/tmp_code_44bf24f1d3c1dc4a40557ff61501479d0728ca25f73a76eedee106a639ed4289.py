code = """import json
import re

# Load the funding data from the file
funding_file_path = var_functions.query_db:0
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Load the civic documents data from the file
civic_file_path = var_functions.query_db:2
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Extract the text from the first document (based on the preview, it contains the project status report)
text = civic_docs[0]['text']

# Initialize list to store extracted projects
projects = []

# Find all capital projects with design status
# Look for the section "Capital Improvement Projects (Design)"
design_section = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|DISASTER RECOVERY PROJECTS|$)', text, re.DOTALL)

if design_section:
    design_text = design_section.group(1)
    
    # Find project names - they typically appear as bolded or titled items
    # Look for patterns where project names are on their own line or followed by updates
    project_patterns = [
        r'([A-Z][^\n]+?)(?=\n\(cid:\d+\) Updates:|\n\(cid:\d+\) Project Schedule:|\n\(cid:\d+\) Estimated Schedule:|\n[A-Z][^\n]+?\n\(cid:\d+\) )',
        r'([A-Z][^\n]{5,100})(?=\n\(cid:\d+\) Updates:|\n\(cid:\d+\) Project Description:|\n\(cid:\d+\) Project Schedule:|\n\(cid:\d+\) Estimated Schedule:)'
    ]
    
    # Extract project names
    lines = design_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Skip empty lines and lines that look like bullet points or contain cid markers
        if (line and 
            not line.startswith('(cid:') and 
            not line.startswith('Page') and
            not line.startswith('Agenda Item') and
            not line.startswith('RECOMMENDED ACTION') and
            not line.startswith('DISCUSSION') and
            len(line) > 5 and
            (line[0].isupper() or line[0].isdigit())):
            
            # Check if this looks like a project name (not a status update line)
            if not any(keyword in line.lower() for keyword in ['updates:', 'schedule:', 'description:', 'advertise:', 'begin construction', 'complete design']):
                # Look ahead to see if this is followed by project markers
                if i + 1 < len(lines) and ('(cid:' in lines[i+1] or '(Updates:)' in lines[i+1] or '(Project' in lines[i+1]):
                    projects.append({
                        'Project_Name': line,
                        'status': 'design',
                        'type': 'capital'
                    })
        i += 1

# Also check for any disaster recovery projects with design status
disaster_section = re.search(r'DISASTER RECOVERY PROJECTS(.*?)(?=\Z|$)', text, re.DOTALL)
if disaster_section:
    disaster_text = disaster_section.group(1)
    # Look for disaster projects in design phase
    if 'Design' in disaster_text:
        lines = disaster_text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if (line and 
                not line.startswith('(cid:') and 
                len(line) > 5 and 
                line[0].isupper() and
                'Design' in disaster_text.split('\n')[min(i+1, len(lines)-1)]):
                projects.append({
                    'Project_Name': line,
                    'status': 'design',
                    'type': 'disaster'
                })
            i += 1

# Clean up project names and remove duplicates
seen = set()
unique_projects = []
for p in projects:
    name = p['Project_Name'].strip()
    if name and name not in seen:
        seen.add(name)
        unique_projects.append({
            'Project_Name': name,
            'status': p['status'],
            'type': p['type']
        })

print('__RESULT__:')
print(json.dumps({
    'extracted_projects': unique_projects,
    'funding_count': len(funding_data)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs']}

exec(code, env_args)
