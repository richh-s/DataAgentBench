code = """import re, json, pandas as pd

path_docs = var_call_XJwkMaCSLkqhIBrkxrkhMDa5
with open(path_docs, 'r') as f:
    docs = json.load(f)

texts = [d['text'] for d in docs]
full_text = '\n'.join(texts)

pattern = r'([^\n]+?)\n(?:.*?)(Begin Construction|Start)[^\n]*?:\s*(Spring 2022)'
matches = re.findall(pattern, full_text, flags=re.IGNORECASE|re.DOTALL)

project_names = set()
for name, _, _ in matches:
    cleaned = name.strip()
    cleaned = re.sub(r'^[\u2022\-\(cid:190\)\*\s]+', '', cleaned)
    if cleaned:
        project_names.add(cleaned)

pattern2 = r'([A-Z0-9].+?)\n[\s\S]{0,200}?Begin Construction[^\n]*Spring 2022'
for m in re.finditer(pattern2, full_text, flags=re.IGNORECASE):
    cleaned = m.group(1).strip()
    cleaned = re.sub(r'^[\u2022\-\(cid:190\)\*\s]+', '', cleaned)
    if cleaned:
        project_names.add(cleaned)

path_funding = var_call_y4GWep2vXAxHDFJSRJBCJ1Qq
with open(path_funding, 'r') as f:
    funding = json.load(f)

df_f = pd.DataFrame(funding)

mask = df_f['Project_Name'].isin(project_names)
selected = df_f[mask].copy()

selected['Amount'] = selected['Amount'].astype(int)

result = {
    'project_names_identified': sorted(project_names),
    'count_projects_with_funding_and_start_spring_2022': int(selected['Project_Name'].nunique()),
    'total_funding_for_those_projects': int(selected['Amount'].sum())
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_XJwkMaCSLkqhIBrkxrkhMDa5': 'file_storage/call_XJwkMaCSLkqhIBrkxrkhMDa5.json', 'var_call_y4GWep2vXAxHDFJSRJBCJ1Qq': 'file_storage/call_y4GWep2vXAxHDFJSRJBCJ1Qq.json'}

exec(code, env_args)
