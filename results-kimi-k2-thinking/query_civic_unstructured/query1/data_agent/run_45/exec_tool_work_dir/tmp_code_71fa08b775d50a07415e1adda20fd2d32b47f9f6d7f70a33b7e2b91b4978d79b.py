code = """import json, re

f_file = str(var_functions.query_db:2)
c_file = str(var_functions.query_db:6)

with open(f_file) as f:
    funding = json.load(f)

with open(c_file) as f:
    civic = json.load(f)

fund_dict = {}
for x in funding:
    if float(x['Amount']) > 50000:
        n = x['Project_Name']
        fund_dict[n] = float(x['Amount'])
        c = re.sub(r'\s*\([^)]*\)\s*$', '', n).strip()
        if c != n:
            fund_dict[c] = float(x['Amount'])

design_projects = []
for doc in civic:
    t = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in t:
        lines = t.split('\n')
        in_section = False
        for line in lines:
            line = line.strip()
            if 'Capital Improvement Projects (Design)' in line:
                in_section = True
            elif 'Capital Improvement Projects (Construction)' in line:
                in_section = False
            if in_section and line and len(line) > 15:
                if all(k not in line for k in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                    if all(w not in line.upper() for w in ['PAGE', 'AGENDA', 'RECOMMENDED']):
                        if all(p not in line for p in ['Updates:', 'Schedule:', 'Capital Improvement Projects']):
                            if not line.startswith('('):
                                design_projects.append(line)

count = sum(1 for p in design_projects if p in fund_dict or re.sub(r'\s*\([^)]*\)\s*$', '', p).strip() in fund_dict)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
