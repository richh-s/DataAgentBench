code = """import json, re

funding_data = json.load(open('/tmp/tmp4q6n_5e0.json'))
civic_docs = json.load(open('/tmp/tmp3d0s1x5g.json'))

projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    marker = 'Capital Improvement Projects (Design)'
    if marker in text:
        start = text.find(marker)
        end = text.find('Capital Improvement Projects (Construction)', start)
        if end == -1: end = text.find('Capital Improvement Projects (Not Started)', start)
        if end == -1: end = text.find('Disaster Recovery Projects', start)
        if end == -1: end = len(text)
        
        section = text[start:end]
        for line in section.split('\n'):
            line = line.strip()
            if not line or line.isupper() or len(line) < 10: continue
            skip_terms = ['cid:', 'Updates:', 'Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', '(', 'Spring', 'Summer', 'Fall', 'Winter', '2023', '2024']
            if any(term in line for term in skip_terms): continue
            clean_line = line.strip(':-•')
            if clean_line: projects.append({'Project_Name': clean_line, 'type': 'capital', 'status': 'design'})

matches = []
used = set()
for proj in projects:
    proj_lower = proj['Project_Name'].lower()
    for fund in funding_data:
        fid = fund['Funding_ID']
        if fid in used: continue
        fund_name = fund['Project_Name']
        fund_lower = fund_name.lower()
        amount = int(fund['Amount'])
        if proj_lower in fund_lower or fund_lower in proj_lower:
            matches.append({'Project_Name': fund_name, 'Amount': amount})
            used.add(fid)
            break

print('__RESULT__:')
print(json.dumps({'count': len(matches), 'projects': matches}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
