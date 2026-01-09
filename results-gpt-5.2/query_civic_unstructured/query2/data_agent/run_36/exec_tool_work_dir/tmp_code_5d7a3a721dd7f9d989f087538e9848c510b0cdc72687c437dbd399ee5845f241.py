code = """import re, json, pathlib

res = var_call_2wio0siV2Oiezi44FZZJWnUI
if isinstance(res, str) and res.endswith('.json'):
    res = json.loads(pathlib.Path(res).read_text())

docs = res
projects = set()
for d in docs:
    text = d.get('text','')
    if re.search(r'(?i)\bpark\b', text) is None:
        continue
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r'(?i)\bpark\b', line):
            start = max(0, i-5)
            end = min(len(lines), i+12)
            window = "\\n".join(lines[start:end])
            if re.search(r'(?i)completed', window) and re.search(r'2022', window):
                name = re.sub(r'\s+', ' ', line.strip())
                name = re.sub(r'^\(?cid:\d+\)?\s*', '', name)
                projects.add(name)

projects = sorted(projects)
print('__RESULT__:')
print(json.dumps({'projects': projects, 'count': len(projects)}))"""

env_args = {'var_call_pZYPMVicdmBSCYrwRtbA6ApW': ['Funding'], 'var_call_W7LR9U57MoPAvg0vnr3DxBQ2': ['civic_docs'], 'var_call_2wio0siV2Oiezi44FZZJWnUI': 'file_storage/call_2wio0siV2Oiezi44FZZJWnUI.json'}

exec(code, env_args)
