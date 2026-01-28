code = """import json

with open(locals()['var_functions.query_db:44']) as f:
    funding = json.load(f)

with open(locals()['var_functions.query_db:2']) as f:
    docs = json.load(f)

funding_names = set([rec['Project_Name'] for rec in funding])
print('Funding projects count:', len(funding_names))

design_cands = []
for rec in docs:
    txt = rec.get('text', '')
    dstart = txt.find('Capital Improvement Projects (Design)')
    if dstart < 0:
        continue
    cstart = txt.find('Capital Improvement Projects (Construction)', dstart)
    if cstart < 0:
        cstart = len(txt)
    section = txt[dstart:cstart]
    blocks = section.split('\n\n')
    for block in blocks:
        block = block.strip()
        if block and 'Design)' not in block and len(block) > 20:
            lines = [line.strip() for line in block.split('\n') if line.strip()]
            if lines:
                first_line = lines[0]
                if first_line and 'Updates' not in first_line and 'Schedule' not in first_line and not first_line.isupper():
                    design_cands.append(first_line)

print('Design candidates found:', len(design_cands))

matched_cnt = 0
for dname in design_cands:
    dclean = dname.split('(')[0].strip().lower().replace('project', '').strip()
    for fund_name in list(funding_names):
        fclean = fund_name.split('(')[0].strip().lower().replace('project', '').strip()
        if dclean in fclean or fclean in dclean:
            matched_cnt += 1
            funding_names.discard(fund_name)
            break

print('Matched count:', matched_cnt)

final = {'count': matched_cnt}
print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
