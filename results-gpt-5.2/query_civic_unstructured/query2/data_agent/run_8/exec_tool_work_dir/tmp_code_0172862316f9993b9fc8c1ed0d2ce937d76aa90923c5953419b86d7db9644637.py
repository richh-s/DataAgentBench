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

completed_line_re = re.compile(r"completed[^0-9]{0,40}2022|completed\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+2022|completed\s+\w+\s+2022", re.IGNORECASE)

completed_park_projects=set()

for d in docs:
    text=d.get('text','') or ''
    if '2022' not in text and '2022' not in text.lower():
        continue
    lines=text.splitlines()
    for i,line in enumerate(lines):
        if not completed_line_re.search(line):
            continue
        # window: previous 5 lines to include project name line
        window='\n'.join(lines[max(0,i-6):i+1])
        wlow=window.lower()
        if 'park' not in wlow:
            continue
        for pn in proj_names:
            plow=str(pn).lower()
            if plow and plow in wlow:
                completed_park_projects.add(pn)

sel=fund_df[fund_df['Project_Name'].isin(completed_park_projects)]

total=int(sel['Amount'].sum())
out={'total':total,'projects':sel.groupby('Project_Name',as_index=False)['Amount'].sum().sort_values('Project_Name').to_dict(orient='records')}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_U1uywrQCDDYMENcY6WTiiEB8': 'file_storage/call_U1uywrQCDDYMENcY6WTiiEB8.json', 'var_call_JlYa1nV6qjPm3RbXQiAVSwd8': 'file_storage/call_JlYa1nV6qjPm3RbXQiAVSwd8.json', 'var_call_PZIOILv8Cu5Q94BVI6eZAvFL': 'ok', 'var_call_WXlvbgHynpMdTje0n4nTeilq': 'ok', 'var_call_MhiEqTHEy6VXGfCSiRc5jowa': {'total_funding_completed_park_projects_2022': 0, 'projects': []}, 'var_call_B9ufVPIgX5SOucftRt2lim2K': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion'}, {'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed November 2022.'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed November 2022'}], 'var_call_Lvy7fC5ubckVaRgLJEU2lP8K': {'filename': 'malibucity_agenda_03222023-2060.txt', 'snippet': 'Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n'}, 'var_call_62aGBAoXurN21RfkiGhImN01': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': 21000}]}

exec(code, env_args)
