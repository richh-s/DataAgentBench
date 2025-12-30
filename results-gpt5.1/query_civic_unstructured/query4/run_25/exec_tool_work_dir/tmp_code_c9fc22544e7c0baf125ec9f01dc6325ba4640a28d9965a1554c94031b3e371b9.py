code = """import re, json, pandas as pd

path_docs = var_call_RDTCDpCDo1FlPHok28GfiOqE
with open(path_docs, 'r') as f:
    docs = json.load(f)

projects = []
for d in docs:
    text = d.get('text','')
    text = re.sub(r"[\r\f]","\n", text)
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        if ':' in line:
            continue
        if len(line) < 10 or len(line) > 120:
            continue
        if not re.search(r"[A-Za-z]", line):
            continue
        if not re.search(r"(Project|Improvements|Repairs|Park|Facility|Study|Signs|Siren|Road|Bridge|Drain|Water|Traffic|Playground|Walkway|Roof|Median|Canyon|Highway|Signal|Street|Slope|Green Streets|Biofilter)", line):
            continue
        context = '\n'.join(lines[i:i+6])
        if re.search(r"2022[- ]?(Spring|March|April|May)", context, re.IGNORECASE):
            projects.append({"Project_Name": line, "context": context})

uniq = {}
for p in projects:
    uniq.setdefault(p['Project_Name'], p)
projects_uniq = list(uniq.values())

path_funding = var_call_pynlZXoX9ZtDSfWMKsk0F78l
with open(path_funding, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

proj_names = [p['Project_Name'] for p in projects_uniq]
matched = fund_df[fund_df['Project_Name'].isin(proj_names)].copy()

result = {
    "projects_started_spring_2022": int(matched['Project_Name'].nunique()),
    "total_funding": int(matched['Amount'].sum()),
    "matched_projects": matched['Project_Name'].unique().tolist()
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_RDTCDpCDo1FlPHok28GfiOqE': 'file_storage/call_RDTCDpCDo1FlPHok28GfiOqE.json', 'var_call_pynlZXoX9ZtDSfWMKsk0F78l': 'file_storage/call_pynlZXoX9ZtDSfWMKsk0F78l.json'}

exec(code, env_args)
