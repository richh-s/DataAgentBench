code = """import json, re

mongo_path = var_call_U1uywrQCDDYMENcY6WTiiEB8
with open(mongo_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# search for park-related completion 2022 lines
hits=[]
for d in docs:
    text=d.get('text','') or ''
    if '2022' not in text:
        continue
    if ('completed' not in text.lower()) and ('Construction was completed' not in text):
        continue
    if 'Park' not in text and 'park' not in text:
        continue
    for line in text.splitlines():
        ll=line.lower()
        if '2022' in ll and ('completed' in ll):
            if 'park' in ll:
                hits.append({'filename':d.get('filename'), 'line':line.strip()})
        if 'construction was completed' in ll and '2022' in ll:
            hits.append({'filename':d.get('filename'), 'line':line.strip()})

print('__RESULT__:')
print(json.dumps(hits[:50]))"""

env_args = {'var_call_U1uywrQCDDYMENcY6WTiiEB8': 'file_storage/call_U1uywrQCDDYMENcY6WTiiEB8.json', 'var_call_JlYa1nV6qjPm3RbXQiAVSwd8': 'file_storage/call_JlYa1nV6qjPm3RbXQiAVSwd8.json', 'var_call_PZIOILv8Cu5Q94BVI6eZAvFL': 'ok', 'var_call_WXlvbgHynpMdTje0n4nTeilq': 'ok', 'var_call_MhiEqTHEy6VXGfCSiRc5jowa': {'total_funding_completed_park_projects_2022': 0, 'projects': []}}

exec(code, env_args)
