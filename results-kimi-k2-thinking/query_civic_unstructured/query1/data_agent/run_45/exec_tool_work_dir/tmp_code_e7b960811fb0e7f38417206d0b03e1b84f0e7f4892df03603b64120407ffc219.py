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

print('Data loaded')

# Extract projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    section_type = None
    
    for line in lines:
        line = line.strip()
        
        # Detect project status categories
        if 'Capital Improvement Projects (Design)' in line:
            section_type = 'design'
            continue
        elif 'Capital Improvement Projects (Construction)' in line:
            section_type = 'construction'
            continue
        elif 'Capital Improvement Projects (Not Started)' in line:
            section_type = 'not_started'
            continue
            
        # Look for project names - they appear after section headers and before Updates/Schedule
        if section_type and line and len(line) > 10:
            # Skip meta lines
            skip_words = ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'TO:', 'PREPARED', 'APPROVED', 'DATE', 'Page', 'Agenda Item']
            should_skip = any(word in line.upper() for word in skip_words)
            
            if not should_skip and 'Updates:' not in line and 'Schedule:' not in line:
                # Determine status
                if section_type == 'design':
                    status = 'design'
                elif section_type == 'construction':
                    status = 'completed'
                elif section_type == 'not_started':
                    status = 'not_started'
                else:
                    status = 'unknown'
                
                # Determine type
                proj_type = 'capital'
                if any(keyword in line for keyword in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                    proj_type = 'disaster'
                
                projects.append({
                    'Project_Name': line,
                    'type': proj_type,
                    'status': status,
                    'topic': ''
                })

print(f'Projects extracted: {len(projects)}')

# Clean project names for matching
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
capital_design = [p for p in cleaned_projects if p['type'] == 'capital' and p['status'] == 'design']
print(f'Capital design projects: {len(capital_design)}')

# Filter funding > 50000
funding_gt_50k = [f for f in funding_data if float(f.get('Amount', 0)) > 50000]
print(f'Funding > $50k: {len(funding_gt_50k)}')

# Match projects
matched = []
for proj in capital_design:
    proj_name = proj['Project_Name']
    proj_clean = proj['Clean_Name']
    
    for fund in funding_gt_50k:
        fund_name = fund['Project_Name']
        fund_clean = re.sub(r'\s*\([^)]*\)\s*$', '', fund_name).strip()
        
        # Match if names are similar
        if proj_name == fund_name or proj_clean == fund_clean:
            matched.append({
                'Project_Name': proj_name,
                'Funding_Amount': float(fund['Amount']),
                'Funding_Source': fund['Funding_Source']
            })
            break
        elif fund_clean in proj_clean or proj_clean in fund_clean:
            # Partial match for similar names
            matched.append({
                'Project_Name': proj_name,
                'Funding_Amount': float(fund['Amount']),
                'Funding_Source': fund['Funding_Source']
            })
            break

result = {
    'count': len(matched),
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
