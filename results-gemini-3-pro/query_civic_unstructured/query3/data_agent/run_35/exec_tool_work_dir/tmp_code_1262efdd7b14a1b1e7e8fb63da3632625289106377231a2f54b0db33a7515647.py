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
    lines = doc['text'].replace('\r\n', '\n').split('\n')
    current_status = 'unknown'
    current_project_name = None
    current_project_text = []
    
    def save_project(name, text_lines, status):
        if not name: return
        full_text = '\n'.join(text_lines)
        st = status
        if st == 'construction' and ('Construction was completed' in full_text or 'Notice of completion' in full_text):
            st = 'completed'
        
        base = clean_name(name)
        txt_lower = (name + ' ' + full_text).lower()
        is_rel = 'emergency' in txt_lower or 'fema' in txt_lower
        extracted.append({'Base_Name': base, 'status': st, 'is_rel': is_rel})

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        if "Capital Improvement Projects" in line:
            save_project(current_project_name, current_project_text, current_status)
            current_project_name = None
            current_project_text = []
            
            if "(Design)" in line: current_status = "design"
            elif "(Construction)" in line: current_status = "construction"
            elif "(Not Started)" in line: current_status = "not started"
            else: current_status = "unknown"
            i += 1
            continue
            
        is_new_project = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line.startswith('(cid:190)'):
                is_new_project = True
        
        if is_new_project:
            save_project(current_project_name, current_project_text, current_status)
            current_project_name = line
            current_project_text = []
            i += 1
            continue
            
        if current_project_name:
            current_project_text.append(line)
        
        i += 1
    
    save_project(current_project_name, current_project_text, current_status)

df_ext = pd.DataFrame(extracted)
merged = pd.merge(df_funding, df_ext, on='Base_Name', how='inner')
final = merged[merged['is_rel'] | merged['Project_Name'].str.contains('FEMA|emergency', case=False, regex=True)]
final = final[['Project_Name', 'Funding_Source', 'Amount', 'status']].drop_duplicates()

print('__RESULT__:')
print(final.to_json(orient='records'))"""

env_args = {'var_function-call-10239882962867119811': ['civic_docs'], 'var_function-call-10239882962867121006': ['Funding'], 'var_function-call-7750960758477245626': 'file_storage/function-call-7750960758477245626.json', 'var_function-call-7750960758477242945': 'file_storage/function-call-7750960758477242945.json', 'var_function-call-3106554336237263291': 'file_storage/function-call-3106554336237263291.json'}

exec(code, env_args)
