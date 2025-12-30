code = """import json
import pandas as pd

# Files
funding_file = locals()['var_function-call-2782363778885918640']
docs_file = locals()['var_function-call-9895724899221676838']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    txt = doc['text']
    lines = txt.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'Updates:' in line:
            # Name is previous non-empty line
            name_idx = i - 1
            while name_idx >= 0 and not lines[name_idx].strip():
                name_idx -= 1
            if name_idx < 0: continue
            name = lines[name_idx].strip()
            
            # Find start date
            start_date = None
            for j in range(i+1, min(i+20, len(lines))):
                subline = lines[j].strip()
                if 'Begin Construction:' in subline:
                    start_date = subline.split('Begin Construction:')[1].strip()
                    break
                if 'Start Date:' in subline:
                    start_date = subline.split('Start Date:')[1].strip()
                    break
            
            if start_date:
                projects.append({'name': name, 'start': start_date})

# Filter Spring 2022
matches = []
for p in projects:
    s = p['start'].lower()
    if 'spring 2022' in s or 'spring, 2022' in s:
        matches.append(p['name'])
    elif '2022' in s:
        if 'march' in s or 'april' in s or 'may' in s:
            matches.append(p['name'])

matches = list(set(matches))

# Funding
matches_norm = [m.lower().strip() for m in matches]
funding_df['name_norm'] = funding_df['Project_Name'].str.lower().str.strip()
res_df = funding_df[funding_df['name_norm'].isin(matches_norm)]

print('__RESULT__:')
print(json.dumps({
    'count': int(res_df['name_norm'].nunique()),
    'total': float(res_df['Amount'].astype(float).sum()),
    'projects': matches
}))"""

env_args = {'var_function-call-4138183868648967311': ['civic_docs'], 'var_function-call-15559280801211844213': 'file_storage/function-call-15559280801211844213.json', 'var_function-call-2782363778885918640': 'file_storage/function-call-2782363778885918640.json', 'var_function-call-9895724899221676838': 'file_storage/function-call-9895724899221676838.json'}

exec(code, env_args)
