code = """import json, re

# Open files
f1 = open(var_functions.query_db:2)
funding = json.load(f1)
f1.close()

f2 = open(var_functions.query_db:6)
civic = json.load(f2)
f2.close()

# Funding map for projects > 50000
fund = {}
for r in funding:
    a = float(r['Amount'])
    if a > 50000:
        n = r['Project_Name']
        c = re.sub(r'\s*\([^)]*\)\s*$', '', n).strip()
        fund[n] = a
        fund[c] = a

# Find capital design projects
design = []

for d in civic:
    t = d.get('text', '')
    if '(Design)' in t:
        # Extract lines between Design and Construction sections
        start = t.find('(Design)')
        end = t.find('(Construction)', start)
        if end > start:
            section = t[start:end]
        else:
            section = t[start:]
        
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 15:
                if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line:
                    if 'Page' not in line and 'Agenda' not in line:
                        if 'Updates:' not in line and 'Schedule:' not in line:
                            if 'RECOMMENDED' not in line.upper():
                                design.append(line)

# Count matches
count = 0
for p in design:
    pc = re.sub(r'\s*\([^)]*\)\s*$', '', p).strip()
    if p in fund or pc in fund:
        count += 1

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
