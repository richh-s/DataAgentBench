code = """import json

mongo_path = var_call_U1uywrQCDDYMENcY6WTiiEB8
with open(mongo_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

res = None
for d in docs:
    text = d.get('text','') or ''
    if 'Bluffs Park Shade Structure' in text:
        lines = text.splitlines()
        for i,l in enumerate(lines):
            if 'Bluffs Park Shade Structure' in l:
                snippet='\\n'.join(lines[i:i+12])
                res={'filename':d.get('filename'),'snippet':snippet}
                break
    if res:
        break

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_U1uywrQCDDYMENcY6WTiiEB8': 'file_storage/call_U1uywrQCDDYMENcY6WTiiEB8.json', 'var_call_JlYa1nV6qjPm3RbXQiAVSwd8': 'file_storage/call_JlYa1nV6qjPm3RbXQiAVSwd8.json', 'var_call_PZIOILv8Cu5Q94BVI6eZAvFL': 'ok', 'var_call_WXlvbgHynpMdTje0n4nTeilq': 'ok', 'var_call_MhiEqTHEy6VXGfCSiRc5jowa': {'total_funding_completed_park_projects_2022': 0, 'projects': []}, 'var_call_B9ufVPIgX5SOucftRt2lim2K': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion'}, {'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed November 2022.'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed November 2022'}]}

exec(code, env_args)
