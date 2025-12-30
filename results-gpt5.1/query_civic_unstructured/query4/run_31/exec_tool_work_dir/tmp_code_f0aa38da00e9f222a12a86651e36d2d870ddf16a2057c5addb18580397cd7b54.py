code = """import re, json, pandas as pd

path_civic = var_call_6Kl4Y7L1h1fmXv4eFFhNjhRi
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]
full_text = "\n".join(texts)

lines = [l.strip() for l in full_text.split('\n') if l.strip()]

spring_projects = set()
for i, line in enumerate(lines):
    if re.search(r"2022[- ]?(Spring|March|April|May)", line, re.IGNORECASE):
        for j in range(max(0, i-5), i):
            if any(k in lines[j] for k in ['Project', 'Improvements', 'Repairs', 'Resurfacing', 'Playground', 'Shade Structure', 'Water Treatment', 'Warning Signs', 'Warning Sirens']):
                spring_projects.add(lines[j])

spring_projects_clean = set()
for p in spring_projects:
    p_clean = re.sub(r"\s*\(cid:[0-9]+\)", '', p)
    p_clean = re.sub(r"\s*Updates:.*", '', p_clean)
    p_clean = p_clean.replace('Project Description:', '').strip(' :\t')
    spring_projects_clean.add(p_clean)

path_funding = var_call_cIQxgNROgtM6eIZvSYNhTDrD
with open(path_funding, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

spring_funding_rows = []
for _, row in fund_df.iterrows():
    name = row['Project_Name']
    for sp in spring_projects_clean:
        if sp and (sp.lower() in name.lower() or name.lower() in sp.lower()):
            spring_funding_rows.append(row)
            break

spring_funding_df = pd.DataFrame(spring_funding_rows)

if spring_funding_df.empty:
    result = {"project_count": 0, "total_funding": 0}
else:
    result = {"project_count": int(spring_funding_df['Project_Name'].nunique()),
              "total_funding": int(spring_funding_df['Amount'].sum())}

res_json = json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_6Kl4Y7L1h1fmXv4eFFhNjhRi': 'file_storage/call_6Kl4Y7L1h1fmXv4eFFhNjhRi.json', 'var_call_cIQxgNROgtM6eIZvSYNhTDrD': 'file_storage/call_cIQxgNROgtM6eIZvSYNhTDrD.json'}

exec(code, env_args)
