code = """import json
import re

def extract_project_info(text):
    projects = []
    project_pattern = re.compile(r'\n\n([A-Za-z0-9][A-Za-z0-9\s&,-]+?)(?:\n\n\(cid:190\)|\n\(cid:190\)|\nProject Description:|\nUpdates:|\nProject Schedule:|\nEstimated Schedule:|\nRECOMMENDED ACTION:)', re.DOTALL)
    
    # Split the document into potential project sections
    sections = project_pattern.split(text)
    
    # The first section is usually general intro, skip it or handle if needed
    # Then, sections are name, details, name, details, etc.
    for i in range(1, len(sections), 2):
        project_name = sections[i].strip()
        details = sections[i+1] if i+1 < len(sections) else ''

        # Initialize default values
        topic = 'N/A'
        project_type = 'N/A'
        status = 'N/A'
        et = 'N/A'

        # Extracting Topic (simple keyword check for 'park')
        if re.search(r'park', project_name, re.IGNORECASE) or re.search(r'park', details, re.IGNORECASE):
            topic = 'park'

        # Extracting Type (capital or disaster)
        if re.search(r'Capital Improvement Projects', details, re.IGNORECASE):
            project_type = 'capital'
        elif re.search(r'Disaster Recovery Projects', details, re.IGNORECASE):
            project_type = 'disaster'

        # Extracting Status
        if re.search(r'construction was completed|complete construction|notice of completion filed', details, re.IGNORECASE):
            status = 'completed'
        elif re.search(r'project is currently under construction', details, re.IGNORECASE):
            status = 'under construction'
        elif re.search(r'preliminary design phase|complete design|design plans for this project|final design', details, re.IGNORECASE):
            status = 'design'
        elif re.search(r'not started', details, re.IGNORECASE):
            status = 'not started'
        
        # Extracting End Time (et)
        et_match = re.search(r'(?:Complete Construction|construction was completed|Complete design|advertise|begin construction):\s*(.*?)(?:\n|$)', details, re.IGNORECASE)
        if et_match:
            et = et_match.group(1).strip()
            
        projects.append({
            'Project_Name': project_name,
            'topic': topic,
            'type': project_type,
            'status': status,
            'et': et
        })
    return projects

all_projects = []
with open(locals()['var_function-call-10538662838025527717'], 'r') as f:
    data = json.load(f)
    for doc in data:
        all_projects.extend(extract_project_info(doc['text']))

# Filter for park-related, completed projects in 2022
filtered_projects = [
    p for p in all_projects 
    if p['topic'] == 'park' and 
       p['status'] == 'completed' and 
       '2022' in p['et']
]

# Get unique project names to avoid duplicates
unique_project_names = list(set([p['Project_Name'] for p in filtered_projects]))

print('__RESULT__:')
print(json.dumps(unique_project_names)))"""

env_args = {'var_function-call-6798812027977815214': ['civic_docs'], 'var_function-call-10538662838025527717': 'file_storage/function-call-10538662838025527717.json'}

exec(code, env_args)
