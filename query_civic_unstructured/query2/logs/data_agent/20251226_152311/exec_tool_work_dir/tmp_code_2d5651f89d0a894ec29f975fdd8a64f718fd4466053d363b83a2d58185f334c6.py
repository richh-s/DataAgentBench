code = """import json
import pandas as pd

with open(var_call_M5WB5deY7REsm7gEQ2IqlM4Q, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_Rp5VVDEy0XKOcKG6atWrw8IL, 'r') as f:
    funding = json.load(f)

# Extract likely park-related completed projects from 2022
project_candidates = set()
for doc in civic_docs:
    text = doc['text'].lower()
    if '2022' in text:
        sections = text.split('\n')
        for i, line in enumerate(sections):
            if 'park' in line and 'completed' in line and '2022' in line:
                project_candidates.add(line.strip(': ').strip())
            if 'construction was completed' in line and '2022' in line:
                for lag in range(1,4):
                    if i-lag >= 0 and 'park' in sections[i-lag]:
                        project_candidates.add(sections[i-lag].strip(': ').strip())
project_filters = [n.lower().replace('project','').replace('repairs','').replace('repair','').replace('structure','').replace('walkway','').replace('renovation','').replace(':','').strip() for n in project_candidates]
df = pd.DataFrame(funding)
df['name_norm'] = df['Project_Name'].str.lower().replace({':':'','project':'','repairs':'','repair':'','structure':'','walkway':'','renovation':''},regex=True).str.strip()
mask = df['name_norm'].apply(lambda x: any(k in x for k in project_filters))
final = df[mask]
total = final['Amount'].astype(float).sum()
print('__RESULT__:')
print(json.dumps(int(total)))"""

env_args = {'var_call_M5WB5deY7REsm7gEQ2IqlM4Q': 'file_storage/call_M5WB5deY7REsm7gEQ2IqlM4Q.json', 'var_call_Rp5VVDEy0XKOcKG6atWrw8IL': 'file_storage/call_Rp5VVDEy0XKOcKG6atWrw8IL.json'}

exec(code, env_args)
