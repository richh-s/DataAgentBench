code = """import re, json, pandas as pd, os, pathlib

# Load full civic docs
path = var_call_YlZstWe5xuBniJt18FLlxfTy
with open(path, 'r') as f:
    civic_docs = json.load(f)

# Heuristic extraction: build a map from project name to inferred type and (st, et) if year present
project_info = {}
for doc in civic_docs:
    text = doc.get('text','')
    # Split on line breaks; many project names are standalone lines
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        # consider lines that look like project titles (contain 'Project' or 'Improvements' etc.)
        if len(line) > 200: 
            continue
        if not re.search(r'Project|Improvements|Repairs|Canyon|Park|Road|Street|Bridge|Warning|Median|Culvert|Drain', line):
            continue
        name = line
        # search local window around line for type indicators and dates
        window = '\n'.join(lines[max(0,i-5):min(len(lines), i+10)])
        t = None
        if re.search(r'FEMA|CalOES|CalJPIA|Woolsey|disaster', window, re.I):
            t = 'disaster'
        elif re.search(r'Capital Improvement Project|Capital Improvement Program', window, re.I):
            t = 'capital'
        # find any "Start" or schedule lines with a 4-digit year
        m = re.search(r'(Begin Construction|Start|Project Schedule).*?(20\d{2})', window, re.I|re.S)
        st = None
        if m:
            st = m.group(2)
        info = project_info.get(name, {})
        if t and 'type' not in info:
            info['type'] = t
        if st and 'st' not in info:
            info['st'] = st
        project_info[name] = info

# Now load funding table
funding_path = var_call_9GWM7ZYos6a4Vn5PSyg9ZfQO
with open(funding_path,'r') as f:
    funding = json.load(f)

# Join funding with project_info on Project_Name using simple exact match or prefix match
rows = []
for row in funding:
    pname = row['Project_Name']
    info = project_info.get(pname)
    # try to match by stripping disaster suffixes
    if not info:
        base = re.sub(r'\s*\((FEMA|CalOES|CalJPIA|FEMA/CalOES) Project\)','', pname)
        base = base.strip()
        info = project_info.get(base)
    if info:
        row2 = row.copy()
        row2.update(info)
        rows.append(row2)

df = pd.DataFrame(rows)

# Filter for disaster type and start year 2022 (using substring '2022' in st if present, or infer from name like '2022 ...')
mask_disaster = df['type'].eq('disaster')
mask_2022 = False
if 'st' in df.columns:
    mask_2022 = df['st'].fillna('').astype(str).str.contains('2022')
# additionally, treat projects whose Project_Name starts with '2022 ' as 2022
mask_name_2022 = df['Project_Name'].str.contains('2022')
mask = mask_disaster & (mask_2022 | mask_name_2022)

total = df.loc[mask, 'Amount'].astype(int).sum()

result = json.dumps(total)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_YlZstWe5xuBniJt18FLlxfTy': 'file_storage/call_YlZstWe5xuBniJt18FLlxfTy.json', 'var_call_9GWM7ZYos6a4Vn5PSyg9ZfQO': 'file_storage/call_9GWM7ZYos6a4Vn5PSyg9ZfQO.json'}

exec(code, env_args)
