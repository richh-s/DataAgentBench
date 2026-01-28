code = """import json
import re
import pandas as pd

with open('var_function-call-7750960758477245626.json', 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

def clean_name(name):
    name = re.sub(r'\s*\((?:FEMA|CalOES|CalJPIA|FEMA/CalOES).*?\)$', '', name)
    name = re.sub(r'\s*\((?:FEMA|CalOES)\)$', '', name)
    return name.strip()

df_funding['Base_Name'] = df_funding['Project_Name'].apply(clean_name)

with open('var_function-call-3106554336237263291.json', 'r') as f:
    civic_docs = json.load(f)

extracted = []

for doc in civic_docs:
    text = doc['text'].replace('\r\n', '\n')
    parts = re.split(r'(Capital Improvement Projects \((?:Design|Construction|Not Started)\))', text)
    current_status = 'unknown'
    for i in range(len(parts)):
        p = parts[i].strip()
        if not p: continue
        if 'Capital Improvement Projects' in p:
            if '(Design)' in p: current_status = 'design'
            elif '(Construction)' in p: current_status = 'construction'
            elif '(Not Started)' in p: current_status = 'not started'
        else:
            blocks = re.split(r'\n(?=[^\n]+\n\(cid:190\))', p)
            for b in blocks:
                b = b.strip()
                if not b: continue
                lines = b.split('\n')
                if len(lines) > 1 and '(cid:190)' in lines[1]:
                    raw_name = lines[0].strip()
                    base = clean_name(raw_name)
                    st = current_status
                    if st == 'construction' and ('Construction was completed' in b or 'Notice of completion' in b):
                        st = 'completed'
                    
                    txt_lower = (raw_name + ' ' + b).lower()
                    is_rel = 'emergency' in txt_lower or 'fema' in txt_lower
                    
                    extracted.append({'Base_Name': base, 'status': st, 'is_rel': is_rel})

df_ext = pd.DataFrame(extracted)
merged = pd.merge(df_funding, df_ext, on='Base_Name', how='inner')
final = merged[merged['is_rel'] | merged['Project_Name'].str.contains('FEMA|emergency', case=False, regex=True)]
final = final[['Project_Name', 'Funding_Source', 'Amount', 'status']].drop_duplicates()

print('__RESULT__:')
print(final.to_json(orient='records'))"""

env_args = {'var_function-call-10239882962867119811': ['civic_docs'], 'var_function-call-10239882962867121006': ['Funding'], 'var_function-call-7750960758477245626': 'file_storage/function-call-7750960758477245626.json', 'var_function-call-7750960758477242945': 'file_storage/function-call-7750960758477242945.json', 'var_function-call-3106554336237263291': 'file_storage/function-call-3106554336237263291.json'}

exec(code, env_args)
