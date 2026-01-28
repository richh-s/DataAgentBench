code = """import json, pandas as pd

# Load full civic docs
with open(var_call_vYDeysvt9buEJI35ksjVOQgi, 'r') as f:
    civic_docs = json.load(f)

# Load funding table
with open(var_call_svWhjDpG5R48mOEYBZyr18kS, 'r') as f:
    funding = json.load(f)

funding_df = pd.DataFrame(funding)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Very simple heuristic: look for lines mentioning a year-season pattern and a project name that matches Funding.Project_Name
spring_keywords = ['Spring 2022', '2022-Spring']

projects_spring_2022 = set()
for doc in civic_docs:
    text = doc.get('text','')
    if '2022' not in text:
        continue
    # split into lines
    for line in text.split('\n'):
        if '2022' in line and any(k in line for k in spring_keywords):
            # try to match any project name substring from funding table
            for name in funding_df['Project_Name']:
                if name in line:
                    projects_spring_2022.add(name)

# Fallback: also consider descriptions where schedule says 'Advertise: Spring 2022' or 'Begin Construction: Spring 2022' on nearby lines
for doc in civic_docs:
    lines = doc.get('text','').split('\n')
    for i, line in enumerate(lines):
        if 'Spring 2022' in line:
            window = '\n'.join(lines[max(0,i-5):i+6])
            for name in funding_df['Project_Name']:
                if name in window:
                    projects_spring_2022.add(name)

proj_list = sorted(projects_spring_2022)
subset = funding_df[funding_df['Project_Name'].isin(proj_list)]

result = {
    'projects_started_spring_2022': proj_list,
    'count': int(len(subset)),
    'total_funding': int(subset['Amount'].sum()) if len(subset)>0 else 0
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_vYDeysvt9buEJI35ksjVOQgi': 'file_storage/call_vYDeysvt9buEJI35ksjVOQgi.json', 'var_call_svWhjDpG5R48mOEYBZyr18kS': 'file_storage/call_svWhjDpG5R48mOEYBZyr18kS.json'}

exec(code, env_args)
