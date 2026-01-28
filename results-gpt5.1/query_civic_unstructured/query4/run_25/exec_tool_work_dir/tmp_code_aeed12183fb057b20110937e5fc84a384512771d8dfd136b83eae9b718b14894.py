code = """import re, json, pandas as pd

# Load full civic docs
path_docs = var_call_RDTCDpCDo1FlPHok28GfiOqE
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Very rough heuristic: project lines are those that look like titles (no colon, not too short) followed by schedules.
projects = []
for d in docs:
    text = d.get('text','')
    # Normalize whitespace
    text = re.sub(r"[\r\f]","\n", text)
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        # candidate project name if it contains keywords like 'Project', 'Improvements', 'Repairs', 'Park', 'Facility', 'Study', 'Signs', 'Siren', 'Road', 'Bridge', 'Drain', 'Water', 'Traffic' etc.
        if ':' in line:
            continue
        if len(line) < 10 or len(line) > 120:
            continue
        if not re.search(r"[A-Za-z]", line):
            continue
        if not re.search(r"(Project|Improvements|Repairs|Park|Facility|Study|Signs|Siren|Road|Bridge|Drain|Water|Traffic|Playground|Walkway|Roof|Median|Canyon|Highway|Signal|Street|Slope|Green Streets|Biofilter)", line):
            continue
        # look ahead a few lines for start date patterns like 'Begin Construction: 2022-Spring' or similar
        context = '\n'.join(lines[i:i+6])
        # search for st/et like strings with 2022 and Spring (March-May)
        if re.search(r"2022[- ]?(Spring|March|April|May)", context, re.IGNORECASE):
            projects.append({"Project_Name": line, "context": context})

# Deduplicate by project name
uniq = {}
for p in projects:
    uniq.setdefault(p['Project_Name'], p)
projects_uniq = list(uniq.values())

# Load funding table
path_funding = var_call_pynlZXoX9ZtDSfWMKsk0F78l
with open(path_funding, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Join by exact project name
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
