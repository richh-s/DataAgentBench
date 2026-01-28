code = """import re, json, pathlib

res = var_call_FblSdvFQbESOdA84gPeKNNJn
if isinstance(res, str) and res.endswith('.json'):
    res = json.loads(pathlib.Path(res).read_text())

docs = res
completed_2022_parks = set()

pat = re.compile(r'(?i)\bconstruction\s+was\s+completed\b[^\n]*2022')
for d in docs:
    text = d.get('text','')
    if '2022' not in text:
        continue
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if pat.search(line):
            # walk back to find preceding project name line (non-empty, not bullet header)
            j = i-1
            while j >= 0 and (lines[j].strip()=='' or re.search(r'(?i)updates|project schedule|capital improvement projects', lines[j])):
                j -= 1
            if j >= 0:
                # sometimes project name is two lines above (e.g. after blank)
                name = lines[j].strip()
                # if line is 'Updates:' then go further back
                if re.search(r'(?i)updates', name):
                    k = j-1
                    while k>=0 and lines[k].strip()=='':
                        k-=1
                    if k>=0:
                        name = lines[k].strip()
                if re.search(r'(?i)\bpark\b', name):
                    name = re.sub(r'\s+', ' ', name)
                    completed_2022_parks.add(name)

print('__RESULT__:')
print(json.dumps({'projects': sorted(completed_2022_parks), 'count': len(completed_2022_parks)}))"""

env_args = {'var_call_pZYPMVicdmBSCYrwRtbA6ApW': ['Funding'], 'var_call_W7LR9U57MoPAvg0vnr3DxBQ2': ['civic_docs'], 'var_call_2wio0siV2Oiezi44FZZJWnUI': 'file_storage/call_2wio0siV2Oiezi44FZZJWnUI.json', 'var_call_GA1kZuYM4iPHeHOTLsOa19MX': {'projects': [], 'count': 0}, 'var_call_FblSdvFQbESOdA84gPeKNNJn': 'file_storage/call_FblSdvFQbESOdA84gPeKNNJn.json'}

exec(code, env_args)
