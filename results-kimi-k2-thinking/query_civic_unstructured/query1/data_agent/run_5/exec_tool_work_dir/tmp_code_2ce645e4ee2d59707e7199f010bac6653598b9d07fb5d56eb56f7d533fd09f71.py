code = """import json

with open(locals()['var_functions.query_db:44']) as f:
    funding = json.load(f)

with open(locals()['var_functions.query_db:2']) as f:
    docs = json.load(f)

funding_names = set([rec['Project_Name'] for rec in funding])
print('Funding records count:', len(funding_names))

design_list = []
for doc in docs:
    txt = doc.get('text', '')
    dstart = txt.find('Capital Improvement Projects (Design)')
    if dstart >= 0:
        cstart = txt.find('Capital Improvement Projects (Construction)', dstart)
        if cstart < 0:
            cstart = len(txt)
        section = txt[dstart:cstart]
        parts = section.split('\n\n')
        for part in parts:
            part = part.strip()
            if len(part) > 15:
                lines = [L.strip() for L in part.split('\n') if L.strip()]
                if lines and len(lines[0]) > 5:
                    name = lines[0]
                    if 'Updates' not in name and 'Schedule' not in name and not name.isupper():
                        design_list.append(name)

print('Design projects found:', len(design_list))

matched = 0
for design_name in design_list:
    d_clean = design_name.split('(')[0].strip().lower()
    d_clean = d_clean.replace('project', '').strip()
    
    for fund_name in list(funding_names):
        f_clean = fund_name.split('(')[0].strip().lower()
        f_clean = f_clean.replace('project', '').strip()
        
        if d_clean in f_clean or f_clean in d_clean:
            matched += 1
            funding_names.discard(fund_name)
            break

result = {'count': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
