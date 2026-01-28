code = """import json
import re

funding_result = var_functions.query_db:0
civic_result = var_functions.query_db:2

if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_result

if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

print('Funding records count:', len(funding_records))
print('Civic documents count:', len(civic_docs))

capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        line_clean = line.strip()
        if len(line_clean) < 10:
            continue
        
        line_lower = line_clean.lower()
        text_lower = text.lower()
        
        if 'capital improvement projects' in text_lower and 'design' in text_lower:
            skip_line = False
            skip_terms = ['updates', 'schedule', 'staff', 'city council', 'consultant', 'discussion', 'page ', 'complete design', 'advertise', 'construction']
            for term in skip_terms:
                if term in line_lower:
                    skip_line = True
                    break
            
            if skip_line:
                continue
            
            project_terms = ['road', 'avenue', 'drive', 'park', 'drain', 'storm', 'bridge', 'walkway', 'trail', 'sewer', 'water', 'traffic', 'signal', 'sign', 'median']
            for term in project_terms:
                if term in line_lower:
                    capital_projects.append(line_clean)
                    break

capital_projects = list(set(capital_projects))
print('Capital design projects extracted:', len(capital_projects))

matched = 0
for proj in capital_projects:
    proj_lower = proj.lower()
    for fund in funding_records:
        amount = int(fund['Amount'])
        if amount > 50000:
            fund_name_lower = fund['Project_Name'].lower()
            if proj_lower == fund_name_lower or proj_lower in fund_name_lower or fund_name_lower in proj_lower:
                matched += 1
                break

print('Final matched count:', matched)
result_json = json.dumps({'count': matched})
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
