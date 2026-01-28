code = """import re, json, pandas as pd

path_docs = var_call_H990rB8ZcX9xgp1oP2yuKt7n
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = [d['text'] for d in docs]
full_text = "\n".join(texts)

lines = full_text.split('\n')
project_lines = []
for i, line in enumerate(lines):
    clean = line.strip()
    if not clean:
        continue
    if re.search(r"Park|Playground|Skate Park", clean, re.IGNORECASE):
        if len(clean) < 200:
            project_lines.append(clean)

project_names = sorted(set(project_lines))

funding = var_call_8IHsNiJsGRcwYURuwiwvnazD
fdf = pd.DataFrame(funding)
fdf['Amount'] = pd.to_numeric(fdf['Amount'])

mask_park = fdf['Project_Name'].str.contains(r"Park|Playground|Skate", case=False, regex=True)
park_funding = fdf[mask_park].copy()

completed_2022_projects = set()
for pn in park_funding['Project_Name'].unique():
    pattern = re.escape(pn)
    for m in re.finditer(pattern, full_text):
        start = max(0, m.start()-400)
        end = min(len(full_text), m.end()+400)
        ctx = full_text[start:end]
        if re.search(r"Construction was completed[^\n]*2022|completed,?\s*November 2022|completed,?\s*December 2022|completed November 2022", ctx):
            completed_2022_projects.add(pn)
            break

mask_completed = park_funding['Project_Name'].isin(completed_2022_projects)
completed_park_funding_2022 = park_funding[mask_completed]

total_funding = int(completed_park_funding_2022['Amount'].sum())

result = {
    "completed_2022_projects_detected": sorted(list(completed_2022_projects)),
    "total_funding_completed_park_2022": total_funding
}

res_json = json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_H990rB8ZcX9xgp1oP2yuKt7n': 'file_storage/call_H990rB8ZcX9xgp1oP2yuKt7n.json', 'var_call_8IHsNiJsGRcwYURuwiwvnazD': 'file_storage/call_8IHsNiJsGRcwYURuwiwvnazD.json'}

exec(code, env_args)
