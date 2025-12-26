code = """import json
import pandas as pd
with open(var_call_M5WB5deY7REsm7gEQ2IqlM4Q, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_Rp5VVDEy0XKOcKG6atWrw8IL, 'r') as f:
    funding = json.load(f)
park_names = set()
for doc in civic_docs:
    t = doc['text'].lower()
    if '2022' in t:
        lines = t.split('\n')
        for i,line in enumerate(lines):
            if ('park' in line and 'completed' in line and '2022' in line) or ('park' in line and 'construction was completed' in line and '2022' in line):
                park_names.add(line.strip())
            if 'construction was completed' in line and '2022' in line:
                for o in range(1,4):
                    if i-o >= 0 and 'park' in lines[i-o]:
                        park_names.add(lines[i-o].strip())
parks_norm = set([n.lower().replace('project','').replace('repairs','').replace('repair','').replace('structure','').replace('walkway','').replace('renovation','').replace(':','').strip() for n in park_names])
df = pd.DataFrame(funding)
df['norm_name'] = df['Project_Name'].str.lower().replace({':':'','project':'','repairs':'','repair':'','structure':'','walkway':'','renovation':''},regex=True).str.strip()
matched = df[df['norm_name'].apply(lambda x: any(nx in x for nx in parks_norm))]
total = matched['Amount'].astype(float).sum()
print('__RESULT__:')
print(json.dumps(int(total)))"""

env_args = {'var_call_M5WB5deY7REsm7gEQ2IqlM4Q': 'file_storage/call_M5WB5deY7REsm7gEQ2IqlM4Q.json', 'var_call_Rp5VVDEy0XKOcKG6atWrw8IL': 'file_storage/call_Rp5VVDEy0XKOcKG6atWrw8IL.json'}

exec(code, env_args)
