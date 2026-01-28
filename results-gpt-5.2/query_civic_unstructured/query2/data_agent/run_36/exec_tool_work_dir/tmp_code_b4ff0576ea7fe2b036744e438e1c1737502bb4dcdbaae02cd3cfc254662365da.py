code = """import re, json, pathlib
res = var_call_HDL0pK8SePyYKGzqjrXyyb7G
if isinstance(res, str) and res.endswith('.json'):
    res = json.loads(pathlib.Path(res).read_text())

docs=res
projects=set()
for d in docs:
    text=d.get('text','')
    # Find project blocks where project name line contains 'Park' and somewhere within next ~15 lines has 'completed' and '2022'
    lines=text.splitlines()
    for i,line in enumerate(lines):
        if re.search(r'(?i)\bpark\b', line):
            name=re.sub(r'\s+',' ',line.strip())
            window=' '.join(lines[i:i+20])
            if re.search(r'(?i)completed', window) and re.search(r'2022', window):
                projects.add(name)

print('__RESULT__:')
print(json.dumps({'projects': sorted(projects), 'count': len(projects)}))"""

env_args = {'var_call_pZYPMVicdmBSCYrwRtbA6ApW': ['Funding'], 'var_call_W7LR9U57MoPAvg0vnr3DxBQ2': ['civic_docs'], 'var_call_2wio0siV2Oiezi44FZZJWnUI': 'file_storage/call_2wio0siV2Oiezi44FZZJWnUI.json', 'var_call_GA1kZuYM4iPHeHOTLsOa19MX': {'projects': [], 'count': 0}, 'var_call_FblSdvFQbESOdA84gPeKNNJn': 'file_storage/call_FblSdvFQbESOdA84gPeKNNJn.json', 'var_call_vF95wa5K8urB8NQcMZ0MiJbH': {'projects': [], 'count': 0}, 'var_call_HDL0pK8SePyYKGzqjrXyyb7G': 'file_storage/call_HDL0pK8SePyYKGzqjrXyyb7G.json'}

exec(code, env_args)
