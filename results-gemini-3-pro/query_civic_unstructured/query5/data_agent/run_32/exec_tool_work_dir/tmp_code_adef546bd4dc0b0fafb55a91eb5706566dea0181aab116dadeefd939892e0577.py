code = """import json
import pandas as pd

# Avoid backslash n
NEWLINE = chr(10)

path_docs = locals()['var_function-call-10835669272488718990']
path_fund = locals()['var_function-call-10835669272488721645']

with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

with open(path_fund, 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

def get_base_name(name):
    if '(' in name:
        return name.split('(')[0].strip()
    return name.strip()

base_name_groups = {}
for _, row in df_funding.iterrows():
    base = get_base_name(row['Project_Name'])
    if base not in base_name_groups:
        base_name_groups[base] = []
    base_name_groups[base].append(row)

full_text = ""
for doc in civic_docs:
    full_text += doc['text'] + NEWLINE

total_amount = 0
matched_details = []

for base_name, rows in base_name_groups.items():
    idx = full_text.find(base_name)
    if idx != -1:
        context = full_text[idx:idx+1500]
        
        marker = 'Begin Construction:'
        st = None
        if marker in context:
            after = context.split(marker)[1]
            st = after.split(NEWLINE)[0].strip()
        
        is_disaster = False
        for row in rows:
            rn = row['Project_Name'].lower()
            if 'fema' in rn or 'caloes' in rn or 'disaster' in rn:
                is_disaster = True
                break
        
        c_lower = context.lower()
        if not is_disaster:
            if 'fema' in c_lower or 'caloes' in c_lower or 'disaster' in c_lower:
                is_disaster = True
        
        if st and '2022' in st:
            if is_disaster:
                group_total = sum(r['Amount'] for r in rows)
                total_amount += group_total
                matched_details.append({'name': base_name, 'amount': group_total, 'start': st})

print('__RESULT__:')
print(json.dumps({'total_amount': total_amount, 'projects': matched_details}))"""

env_args = {'var_function-call-10835669272488718990': 'file_storage/function-call-10835669272488718990.json', 'var_function-call-10835669272488721645': 'file_storage/function-call-10835669272488721645.json', 'var_function-call-474033538740406040': {'status': 'loaded', 'docs_count': 5, 'funding_count': 500}}

exec(code, env_args)
