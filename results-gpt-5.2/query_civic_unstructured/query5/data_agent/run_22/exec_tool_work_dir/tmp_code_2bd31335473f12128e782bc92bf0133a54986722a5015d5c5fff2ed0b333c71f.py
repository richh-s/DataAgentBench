code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_pvJShtqIdgjHoyyWmysUP8iU)
fund = load_records(var_call_9cXbeBzbNaOXIHYfXpfQYeX9)

projects = []
for d in docs:
    text = d.get('text','')
    if 'Disaster Recovery Projects' not in text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    cur_type = None
    cur_section = None
    for idx, ln in enumerate(lines):
        if re.match(r'^Disaster Recovery Projects\b', ln):
            cur_type = 'disaster'
            cur_section = None
            continue
        if re.match(r'^Capital Improvement Projects\b', ln):
            cur_type = 'capital'
            cur_section = None
            continue
        m = re.search(r'\((Design|Construction|Not Started)\)', ln)
        if m:
            cur_section = m.group(1).lower()
            continue
        if cur_type != 'disaster':
            continue
        if not ln or ln.startswith('(cid'):
            continue
        # candidate project line if next non-empty line looks like a bullet header
        j = idx + 1
        nxt = ''
        while j < len(lines) and nxt == '':
            nxt = lines[j].strip()
            j += 1
        if ('Updates' in nxt) or ('Project Description' in nxt) or nxt.startswith('(cid:190)'):
            low = ln.lower()
            if low in {'disaster recovery projects', 'disaster recovery projects (design)', 'disaster recovery projects (construction)', 'disaster recovery projects (not started)'}:
                continue
            projects.append({'Project_Name': ln, 'type': 'disaster', 'section': cur_section, 'source_file': d.get('filename')})

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

started_2022 = set()
for pname in proj_df['Project_Name'].tolist():
    for d in docs:
        txt = d.get('text','')
        pos = txt.find(pname)
        if pos == -1:
            continue
        window = txt[pos:pos+2500]
        # look for explicit begin/start in 2022
        if re.search(r'Begin\s+(?:Construction|Work)\s*:\s*[^\n]{0,80}2022', window, flags=re.IGNORECASE):
            started_2022.add(pname); break
        if re.search(r'Start\s*:\s*[^\n]{0,80}2022', window, flags=re.IGNORECASE):
            started_2022.add(pname); break
        if re.search(r'Start(?:ed)?\b[^\n]{0,80}2022', window, flags=re.IGNORECASE):
            started_2022.add(pname); break

started_2022 = sorted(started_2022)

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

total = int(fund_df[fund_df['Project_Name'].isin(started_2022)]['total_amount'].sum())

out = {'total_funding_started_2022_disaster_projects': total, 'projects_count': len(started_2022), 'projects': started_2022}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WforWNGckDLZNcgvbG8AKAU6': ['Funding'], 'var_call_QfAvDZ3qPtBCuw0ojwVBpNT6': ['civic_docs'], 'var_call_pvJShtqIdgjHoyyWmysUP8iU': 'file_storage/call_pvJShtqIdgjHoyyWmysUP8iU.json', 'var_call_9cXbeBzbNaOXIHYfXpfQYeX9': 'file_storage/call_9cXbeBzbNaOXIHYfXpfQYeX9.json'}

exec(code, env_args)
