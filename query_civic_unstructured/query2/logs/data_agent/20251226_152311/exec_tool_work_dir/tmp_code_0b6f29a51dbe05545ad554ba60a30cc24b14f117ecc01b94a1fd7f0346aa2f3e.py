code = """import json
import pandas as pd

with open(var_call_M5WB5deY7REsm7gEQ2IqlM4Q, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_Rp5VVDEy0XKOcKG6atWrw8IL, 'r') as f:
    funding = json.load(f)

# Grab possible park project names from civic docs mentioning completion in 2022
park_project_names = set()
for doc in civic_docs:
    text = doc.get('text', '').lower()
    if '2022' not in text:
        continue
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if ('park' in line) and ('completed' in line and '2022' in line or 'construction was completed' in line and '2022' in line):
            # Use the line as project name
            pname = line.split(':')[0].strip() if ':' in line else line.strip()
            if len(pname) > 3:
                park_project_names.add(pname)
        # Look back for earlier line mentioning park
        if 'construction was completed' in line and '2022' in line:
            for offset in range(1,4):
                if i-offset >= 0 and 'park' in lines[i-offset]:
                    prev_name = lines[i-offset].split(':')[0].strip() if ':' in lines[i-offset] else lines[i-offset].strip()
                    if len(prev_name) > 3:
                        park_project_names.add(prev_name)

# Build a simple normalized set for fuzzy matching
norm_names = set([n.lower().replace('project','').replace('repairs','').replace('repair','').replace('structure','').replace('walkway','').replace('renovation','').replace(':','').strip() for n in park_project_names])

funding_df = pd.DataFrame(funding)
funding_df['norm_project_name'] = funding_df['Project_Name'].str.lower().replace({':':'','project':'','repairs':'','repair':'','structure':'','walkway':'','renovation':''},regex=True).str.strip()

# Filter those projects whose normalized names match
matched = funding_df[funding_df['norm_project_name'].apply(lambda x: any(nx in x for nx in norm_names))]

# Sum the Amount column
total_funding = matched['Amount'].astype(float).sum()
print('__RESULT__:')
print(json.dumps(int(total_funding)))"""

env_args = {'var_call_M5WB5deY7REsm7gEQ2IqlM4Q': 'file_storage/call_M5WB5deY7REsm7gEQ2IqlM4Q.json', 'var_call_Rp5VVDEy0XKOcKG6atWrw8IL': 'file_storage/call_Rp5VVDEy0XKOcKG6atWrw8IL.json'}

exec(code, env_args)
