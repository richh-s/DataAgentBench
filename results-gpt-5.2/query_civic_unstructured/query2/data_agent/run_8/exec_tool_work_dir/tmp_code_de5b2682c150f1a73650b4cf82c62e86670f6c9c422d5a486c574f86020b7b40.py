code = """import json, pandas as pd

funding_path = var_call_JlYa1nV6qjPm3RbXQiAVSwd8
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

df=pd.DataFrame(funding)
df['Amount']=pd.to_numeric(df['Amount'], errors='coerce').fillna(0).astype(int)
mask = df['Project_Name'].str.contains('Bluffs Park Shade Structure', case=False, na=False)
res=df[mask].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_U1uywrQCDDYMENcY6WTiiEB8': 'file_storage/call_U1uywrQCDDYMENcY6WTiiEB8.json', 'var_call_JlYa1nV6qjPm3RbXQiAVSwd8': 'file_storage/call_JlYa1nV6qjPm3RbXQiAVSwd8.json', 'var_call_PZIOILv8Cu5Q94BVI6eZAvFL': 'ok', 'var_call_WXlvbgHynpMdTje0n4nTeilq': 'ok', 'var_call_MhiEqTHEy6VXGfCSiRc5jowa': {'total_funding_completed_park_projects_2022': 0, 'projects': []}, 'var_call_B9ufVPIgX5SOucftRt2lim2K': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion'}, {'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed November 2022.'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed November 2022'}], 'var_call_Lvy7fC5ubckVaRgLJEU2lP8K': {'filename': 'malibucity_agenda_03222023-2060.txt', 'snippet': 'Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n'}}

exec(code, env_args)
