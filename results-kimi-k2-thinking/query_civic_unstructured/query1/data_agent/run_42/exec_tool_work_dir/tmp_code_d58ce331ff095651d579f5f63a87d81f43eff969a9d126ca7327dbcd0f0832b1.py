code = """import json
import re

# Read the MongoDB query result
file_path = var_functions.query_db_2
with open(file_path, 'r') as f:
    civic_docs_data = json.load(f)

print('Number of documents:', len(civic_docs_data))

# Extract projects with design status
projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        stripped = line.strip()
        
        # Check if we're entering the design section
        if 'Capital Improvement Projects (Design)' in stripped:
            in_design_section = True
            continue
            
        # Check if we're leaving the design section
        if in_design_section and ('(Construction)' in stripped or '(Not Started)' in stripped):
            in_design_section = False
            continue
            
        if in_design_section and stripped:
            # Filter out lines that are not project names
            if not stripped.startswith('(') and not stripped.startswith('•'):
                if 'Updates:' not in stripped and 'Project Schedule:' not in stripped and 'Estimated Schedule:' not in stripped:
                    if 'Complete Design:' not in stripped and 'Advertise:' not in stripped and 'Begin Construction:' not in stripped:
                        if 'To:' not in stripped and 'Subject:' not in stripped and 'Page' not in stripped:
                            if 'Prepared by:' not in stripped and 'Approved by:' not in stripped and 'Date prepared:' not in stripped:
                                if len(stripped) > 5 and stripped != 'RECOMMENDED ACTION:' and 'DISCUSSION:' not in stripped:
                                    # Skip lines that are all uppercase or headers
                                    if not stripped.isupper():
                                        # Skip consultant/staff/city updates
                                        if not any(word in stripped for word in ['Consultant', 'Staff', 'City is', 'Staff is', 'City will', 'Project is', 'City has', 'Plans are', 'Bids are', 'Construction was', 'Scheduled for']):
                                            project_name = stripped.strip('•- ')
                                            projects.append({
                                                'project_name': project_name,
                                                'status': 'design',
                                                'type': 'capital'
                                            })

print('Total design projects found:', len(projects))
print('Sample projects:')
for p in projects[:20]:
    print('  -', p['project_name'])

__RESULT__:
print(json.dumps(projects))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
