code = """import json, re, pandas as pd

mongo_path = var_call_U1uywrQCDDYMENcY6WTiiEB8
with open(mongo_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

funding_path = var_call_JlYa1nV6qjPm3RbXQiAVSwd8
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype('int64')
proj_names = fund_df['Project_Name'].dropna().unique().tolist()

park_word_re = re.compile(r"\bpark\b", re.IGNORECASE)
pattern = r"(\\bcompleted\\b|Construction was completed|Complete\\s+Construction)[^\\n\\r]{0,120}?\\b2022\\b"
completed_2022_re = re.compile(pattern, re.IGNORECASE)

completed_park_projects = set()

for d in docs:
    text = d.get('text','') or ''
    tlow = text.lower()
    if '2022' not in tlow:
        continue
    if 'completed' not in tlow and 'construction was completed' not in tlow:
        continue
    if not park_word_re.search(text):
        continue
    lines = text.splitlines()
    for i, line in enumerate(lines):
        llow = line.lower()
        if ('2022' not in llow) and ('completed' not in llow) and ('construction was completed' not in llow):
            continue
        window = "\n".join(lines[max(0,i-2):min(len(lines), i+3)])
        if not (park_word_re.search(window) and completed_2022_re.search(window)):
            continue
        wlow = window.lower()
        for pn in proj_names:
            plow = str(pn).lower()
            if plow and (plow in wlow):
                if ('park' in plow) or park_word_re.search(window):
                    completed_park_projects.add(pn)

for d in docs:
    text = d.get('text','') or ''
    if '2022' not in text.lower():
        continue
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not park_word_re.search(line):
            continue
        line_low = line.lower()
        matched = [pn for pn in proj_names if str(pn).lower() in line_low]
        if not matched:
            continue
        window = "\n".join(lines[i:min(len(lines), i+4)])
        if completed_2022_re.search(window):
            for pn in matched:
                completed_park_projects.add(pn)

sel = fund_df[fund_df['Project_Name'].isin(completed_park_projects)].copy()
total = int(sel['Amount'].sum())

out = {
    'total_funding_completed_park_projects_2022': total,
    'projects': sel.groupby('Project_Name', as_index=False)['Amount'].sum().sort_values('Project_Name').to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_U1uywrQCDDYMENcY6WTiiEB8': 'file_storage/call_U1uywrQCDDYMENcY6WTiiEB8.json', 'var_call_JlYa1nV6qjPm3RbXQiAVSwd8': 'file_storage/call_JlYa1nV6qjPm3RbXQiAVSwd8.json', 'var_call_PZIOILv8Cu5Q94BVI6eZAvFL': 'ok', 'var_call_WXlvbgHynpMdTje0n4nTeilq': 'ok'}

exec(code, env_args)
