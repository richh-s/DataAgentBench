code = """import json

# Load civic documents
civic_docs_file = '/tmp/tmpz5hptp8z.json'
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_file = '/tmp/tmphs_qx5r1.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    project_info = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Detect new project by looking ahead for project content
        if len(line) > 5 and not line.startswith('('):
            # Check if this is followed by project-related content
            is_project = False
            for j in range(i+1, min(i+6, len(lines))):
                next_line = lines[j].lower()
                if 'updates:' in next_line or 'project schedule:' in next_line or 'complete construction:' in next_line or '(cid:' in next_line:
                    is_project = True
                    break
            
            if is_project:
                # Save previous project
                if current_project and project_info:
                    status = project_info.get('status')
                    et = project_info.get('et', '')
                    topic = project_info.get('topic', '').lower()
                    if status == 'completed' and '2022' in et and 'park' in topic:
                        park_projects.append(project_info)
                
                # Start new project
                current_project = line
                project_info = {
                    'Project_Name': line,
                    'status': '',
                    'et': '',
                    'topic': ''
                }
                
                # Determine topic
                pl = line.lower()
                if 'park' in pl:
                    project_info['topic'] = 'park'
                elif 'playground' in pl:
                    project_info['topic'] = 'playground'
        
        # Check for completion status and dates
        if current_project and project_info:
            ll = line.lower()
            
            if 'completed' in ll or 'complete construction' in ll or 'construction was completed' in ll or 'notice of completion' in ll:
                project_info['status'] = 'completed'
                
                # Extract year
                if '2022' in line:
                    project_info['et'] = '2022'
    
    # Save last project
    if current_project and project_info:
        status = project_info.get('status')
        et = project_info.get('et', '')
        topic = project_info.get('topic', '').lower()
        if status == 'completed' and '2022' in et and 'park' in topic:
            park_projects.append(project_info)

# Match with funding data
matches = []
for proj in park_projects:
    proj_name = proj['Project_Name'].lower()
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        # Check for matches (exact or partial)
        if fund_name == proj_name or fund_name in proj_name or proj_name in fund_name:
            matches.append({
                'project_name': proj['Project_Name'],
                'funding_name': fund['Project_Name'],
                'amount': int(fund['Amount'])
            })

# Calculate total funding
total_funding = sum(m['amount'] for m in matches)

result = {
    'park_projects_completed_2022': park_projects,
    'funding_matches': matches,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
