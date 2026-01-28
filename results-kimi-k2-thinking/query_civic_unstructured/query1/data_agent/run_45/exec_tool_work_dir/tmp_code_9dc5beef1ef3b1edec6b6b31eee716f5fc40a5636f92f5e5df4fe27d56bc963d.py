code = """import json, re

funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

projects = []
section_type = None

for doc in civic_docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
        if 'Capital Improvement Projects (Design)' in line:
            section_type = 'design'
        elif 'Capital Improvement Projects (Construction)' in line:
            section_type = 'construction'
        elif 'Capital Improvement Projects (Not Started)' in line:
            section_type = 'not_started'
        
        if section_type and len(line) > 10:
            skip = False
            for word in ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'TO:', 'PREPARED', 'APPROVED', 'DATE', 'Page', 'Agenda Item', 'Updates:', 'Schedule:']:
                if word in line.upper():
                    skip = True
            
            if not skip and not line.startswith('(') and not line.startswith('\u2022'):
                status = 'design' if section_type == 'design' else ('completed' if section_type == 'construction' else 'not_started')
                proj_type = 'disaster' if any(k in line for k in ['FEMA', 'CalOES', 'CalJPIA', 'fire']) else 'capital'
                
                projects.append({
                    'Project_Name': line,
                    'type': proj_type,
                    'status': status
                })

capital_design = [p for p in projects if p['type'] == 'capital' and p['status'] == 'design']

funding_gt_50k = [f for f in funding_data if float(f.get('Amount', 0)) > 50000]

matched = 0

for proj in capital_design:
    proj_name = proj['Project_Name']
    proj_clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj_name).strip()
    
    for fund in funding_gt_50k:
        fund_name = fund['Project_Name']
        fund_clean = re.sub(r'\s*\([^)]*\)\s*$', '', fund_name).strip()
        
        if proj_name == fund_name or proj_clean == fund_clean or fund_clean in proj_clean or proj_clean in fund_clean:
            matched += 1
            break

print('__RESULT__:') 
print(json.dumps({'count': matched}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
