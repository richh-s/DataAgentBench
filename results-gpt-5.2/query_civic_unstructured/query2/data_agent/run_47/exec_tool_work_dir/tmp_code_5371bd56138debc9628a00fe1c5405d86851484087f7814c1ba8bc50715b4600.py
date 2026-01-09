code = """import json, re
import pandas as pd

def load_tool_result(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

docs = load_tool_result(var_call_Qnz8631zTgIET1P1nCy1dME9)
fund = load_tool_result(var_call_kkzM7d1OdECbngMczMndwQkA)

projects = []

for d in docs:
    text = d.get('text', '')
    t = text.replace('\r', '\n')
    lines = [ln.strip() for ln in t.split('\n')]

    current_project = None
    buf = []

    def flush(name, buf_lines):
        if not name:
            return
        block = "\n".join(buf_lines)
        low = block.lower()
        park_related = any(k in (name.lower() + "\n" + low) for k in ["park", "parks", "playground", "bluffs", "skate", "legacy", "trancas"])
        completed_2022 = False
        if "completed" in low:
            if re.search(r"completed[^\n]{0,80}2022", low) or re.search(r"2022[^\n]{0,80}completed", low):
                completed_2022 = True
            if re.search(r"construction was completed[^\n]{0,80}november 2022", low):
                completed_2022 = True
            if re.search(r"construction was completed[^\n]{0,80}2022", low):
                completed_2022 = True
            if re.search(r"complete construction[^\n]{0,80}2022", low):
                completed_2022 = True
        if park_related and completed_2022:
            projects.append({"Project_Name": name})

    for ln in lines:
        if not ln:
            continue
        lowln = ln.lower()
        if lowln in [
            'capital improvement projects (design)',
            'capital improvement projects (construction)',
            'capital improvement projects (not started)',
            'disaster recovery projects (design)',
            'disaster recovery projects (construction)',
            'disaster recovery projects (not started)',
            'project updates:', 'updates:', 'project schedule:', 'estimated schedule:'
        ]:
            continue
        if re.match(r"^[A-Za-z0-9].{3,}$", ln) and not ln.startswith('(cid') and not ln.startswith('Page ') and not ln.startswith('Agenda'):
            if current_project is not None:
                flush(current_project, buf)
            current_project = ln
            buf = []
        else:
            if current_project is not None:
                buf.append(ln)

    flush(current_project, buf)

proj_names = sorted(set(p['Project_Name'] for p in projects))

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = fund_df['total_amount'].astype(float)
sel = fund_df[fund_df['Project_Name'].isin(proj_names)]

total = float(sel['total_amount'].sum())

out = {
    "total_funding": total,
    "project_count": int(sel.shape[0]),
    "projects": sel.sort_values('Project_Name').to_dict(orient='records'),
    "matched_project_names": proj_names
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FHupFkqHl4OgYoZHCOffbKXN': ['Funding'], 'var_call_eyeG8LC6azKhVNC26QjWhYTj': ['civic_docs'], 'var_call_Qnz8631zTgIET1P1nCy1dME9': 'file_storage/call_Qnz8631zTgIET1P1nCy1dME9.json', 'var_call_kkzM7d1OdECbngMczMndwQkA': 'file_storage/call_kkzM7d1OdECbngMczMndwQkA.json'}

exec(code, env_args)
