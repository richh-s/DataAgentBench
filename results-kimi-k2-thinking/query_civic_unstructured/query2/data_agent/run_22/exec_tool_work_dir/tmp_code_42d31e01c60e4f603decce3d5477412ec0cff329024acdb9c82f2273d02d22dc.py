code = """import json, re

filepath1 = locals()['var_functions.query_db:6']
with open(filepath1, 'r') as f:
    civic_docs = json.load(f)

filepath2 = locals()['var_functions.query_db:8']
with open(filepath2, 'r') as f:
    funding_data = json.load(f)

park_completed_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    curr_project = None
    
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Simple heuristic for project name (not status/update/desc lines)
        if (line and not line.startswith('(cid:') and not line.startswith('(') 
            and 'Updates:' not in line and 'Schedule:' not in line 
            and 'Description:' not in line and len(line) < 150 
            and not line.startswith('Page') and not line.startswith('Agenda')
            and 'Recommended Action:' not in line and 'Discussion:' not in line):
            curr_project = line
        
        if curr_project and ('completed' in line.lower() or 'Complete Construction' in line) and '2022' in line:
            if 'park' in curr_project.lower():
                park_completed_2022.append(curr_project)

# Match funding
funding_matches = []
for project in park_completed_2022:
    proj_lower = project.lower()
    for fund in funding_data:
        fund_lower = fund['Project_Name'].lower()
        if proj_lower == fund_lower or fund_lower.startswith(proj_lower) or proj_lower.startswith(fund_lower):
            funding_matches.append({'name': project, 'amount': int(fund['Amount'])})

total = sum(f['amount'] for f in funding_matches)
result = json.dumps({'total_funding': total, 'count': len(funding_matches)})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
