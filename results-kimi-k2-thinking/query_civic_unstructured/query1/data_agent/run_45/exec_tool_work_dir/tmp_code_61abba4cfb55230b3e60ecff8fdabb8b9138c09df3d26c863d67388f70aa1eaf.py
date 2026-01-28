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
    for line in doc.get('text', '').split('\n'):
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            section_type = 'design'
        elif 'Capital Improvement Projects (Construction)' in line:
            section_type = 'construction' 
        elif 'Capital Improvement Projects (Not Started)' in line:
            section_type = 'not_started'
        
        if section_type and line and len(line) > 10:
            skip = False
            for word in ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'Page', 'Agenda']:
                if word in line.upper(): skip = True
            
            if not skip and 'Updates:' not in line and 'Schedule:' not in line:
                status = 'design' if section_type == 'design' else 'completed' if section_type == 'construction' else 'not_started'
                proj_type = 'capital'
                
                for k in ['FEMA', 'CalOES', 'CalJPIA', 'fire']:
                    if k in line: proj_type = 'disaster'
                
                projects.append({
                    'Project_Name': line,
                    'type': proj_type,
                    'status': status
                })

capital_design = [p for p in projects if p['type'] == 'capital' and p['status'] == 'design']

funding_gt_50k = [f for f in funding_data if float(f.get('Amount', 0)) > 50000]

matched = 0

for proj in capital_design:
    proj_clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj['Project_Name']).strip()
    
    for fund in funding_gt_50k:
        fund_clean = re.sub(r'\s*\([^)]*\)\s*$', '', fund['Project_Name']).strip()
        
        if proj['Project_Name'] == fund['Project_Name'] or proj_clean == fund_clean or fund_clean in proj_clean or proj_clean in fund_clean:
            matched += 1
            break

print('__RESULT__:')
print(json.dumps({'count': matched}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
