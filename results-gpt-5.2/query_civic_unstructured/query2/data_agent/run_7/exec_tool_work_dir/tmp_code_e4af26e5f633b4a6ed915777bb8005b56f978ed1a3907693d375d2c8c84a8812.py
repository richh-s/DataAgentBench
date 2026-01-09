code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

civic = load_json_maybe(var_call_lBcDgI8W8mLsI9aGj00ChE6w)
fund = load_json_maybe(var_call_VBXVmsVchk2DIP1SGofGouKN)

fund_df = pd.DataFrame(fund)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype(int)

# Parse projects from civic docs: look for lines like 'Project Name' followed by 'Updates'/'Project Schedule' and completion info.
proj_info = {}

# patterns for completion and park-related topics
park_kw = re.compile(r'\b(park|playground|bluffs|skate)\b', re.IGNORECASE)
completed_2022_kw = re.compile(r'completed[^\n]*\b(2022)\b|\b(2022)[^\n]*completed', re.IGNORECASE)

# Extract candidate project names by scanning lines; project names are often standalone lines without bullets.
for doc in civic:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln or len(ln) < 4:
            continue
        # Heuristic: project name line: not starting with bullet characters and not containing ':' and not 'Updates' etc.
        if re.match(r'^[\(\[\{\-•\*]|^(cid:)', ln, re.IGNORECASE):
            continue
        if any(kw.lower() in ln.lower() for kw in ['updates', 'project schedule', 'estimated schedule', 'project description', 'capital improvement projects', 'disaster recovery projects', 'page ', 'agenda item', 'recommended action', 'discussion']):
            continue
        # look ahead within next 10 lines for completion mention in 2022
        window = "\n".join(lines[i:i+15])
        if completed_2022_kw.search(window) and park_kw.search(ln):
            proj_info[ln] = True

park_completed_2022 = sorted(proj_info.keys())

# Join with funding amounts (exact match)
matched = fund_df[fund_df['Project_Name'].isin(park_completed_2022)]

result = {
    'park_projects_completed_2022': park_completed_2022,
    'matched_funding_records_count': int(matched.shape[0]),
    'total_funding_amount': int(matched['Amount'].sum())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lBcDgI8W8mLsI9aGj00ChE6w': 'file_storage/call_lBcDgI8W8mLsI9aGj00ChE6w.json', 'var_call_VBXVmsVchk2DIP1SGofGouKN': 'file_storage/call_VBXVmsVchk2DIP1SGofGouKN.json'}

exec(code, env_args)
