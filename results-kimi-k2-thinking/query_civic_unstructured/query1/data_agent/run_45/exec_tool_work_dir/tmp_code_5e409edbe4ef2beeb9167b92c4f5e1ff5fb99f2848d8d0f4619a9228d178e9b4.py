code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Loaded data')
print(f'Funding records: {len(funding_data)}')
print(f'Civic documents: {len(civic_docs)}')

# Extract projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    section_type = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Detect project status categories
        if 'Capital Improvement Projects (Design)' in line:
            section_type = 'design'
            continue
        elif 'Capital Improvement Projects (Construction)' in line:
            section_type = 'construction'
            continue
        elif 'Capital Improvement Projects (Not Started)' in line:
            section_type = 'not started'
            continue
        elif 'Disaster Recovery Projects' in line:
            section_type = 'disaster'
            continue
            
        # Look for project names
        if section_type and line and not line.startswith('(') and not line.startswith('\u2022') and 
           'Updates:' not in line and 'Schedule:' not in line and 
           len(line) > 10 and 'Page' not in line and 'Agenda Item' not in line:
            
            # Skip headings
            skip_keywords = ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'TO:', 'PREPARED', 'APPROVED', 'DATE']
            if any(keyword in line.upper() for keyword in skip_keywords):
                continue
                
            # Determine status
            if section_type == 'design':
                status = 'design'
            elif section_type == 'construction':
                status = 'completed'
            elif section_type == 'not started':
                status = 'not started'
            else:
                status = 'unknown'
            
            # Determine type
            proj_type = 'capital'
            if any(keyword in line for keyword in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                proj_type = 'disaster'
            
            # Determine topics
            topics = []
            lower_line = line.lower()
            if 'park' in lower_line:
                topics.append('park')
            if 'road' in lower_line or 'drive' in lower_line or 'lane' in lower_line:
                topics.append('road')
            if 'drain' in lower_line:
                topics.append('drainage')
            if 'storm' in lower_line:
                topics.append('storm drain')
            if 'bridge' in lower_line:
                topics.append('bridge')
            if 'traffic' in lower_line:
                topics.append('traffic')
            if 'warning' in lower_line or 'siren' in lower_line:
                topics.append('emergency warning')
            if 'water' in lower_line:
                topics.append('water treatment')
            if 'playground' in lower_line:
                topics.append('playground')
            if 'median' in lower_line:
                topics.append('highway')
            
            projects.append({
                'Project_Name': line,
                'type': proj_type,
                'status': status,
                'topic': ', '.join(topics)
            })

print(f'Extracted {len(projects)} projects')

# Clean project names
cleaned_projects = []
for proj in projects:
    name = proj['Project_Name']
    clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
    cleaned_projects.append({
        'Project_Name': name,
        'Clean_Name': clean_name,
        'type': proj['type'],
        'status': proj['status'],
        'topic': proj['topic']
    })

# Filter for capital design projects
capital_design_projects = [p for p in cleaned_projects if p['type'] == 'capital' and p['status'] == 'design']
print(f'Capital design projects: {len(capital_design_projects)}')

# Filter funding > 50000
funding_gt_50k = [f for f in funding_data if float(f.get('Amount', 0)) > 50000]
print(f'Funding records > $50k: {len(funding_gt_50k)}')

# Match projects with funding
matched_projects = []
for proj in capital_design_projects:
    proj_name = proj['Project_Name']
    proj_clean = proj['Clean_Name']
    
    for fund in funding_gt_50k:
        fund_name = fund['Project_Name']
        fund_clean = re.sub(r'\s*\([^)]*\)\s*$', '', fund_name).strip()
        
        # Match logic
        if (proj_name == fund_name or proj_clean == fund_clean or
            fund_clean in proj_clean or proj_clean in fund_clean):
            matched_projects.append({
                'Project_Name': proj_name,
                'Funding_Amount': float(fund['Amount']),
                'Funding_Source': fund['Funding_Source']
            })
            break

result = {
    'count': len(matched_projects),
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
