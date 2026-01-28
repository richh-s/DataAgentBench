code = """import json, re

path = var_call_4kyFbfoBMGRtUpextA1f4p3h
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

project_starts = {}

spring2022_patterns = [
    re.compile(r'\bBegin\s+Construction\s*:\s*Spring\s*,?\s*2022\b', re.IGNORECASE),
    re.compile(r'\bAdvertise\s*:\s*Spring\s*,?\s*2022\b', re.IGNORECASE),
    re.compile(r'\bBegin\s+Project\s*:\s*Spring\s*,?\s*2022\b', re.IGNORECASE),
]

name_re = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 ,&\-\(\)\/'\.]+$")

skip_prefixes = (
    'page ', 'agenda', 'to:', 'to ', 'prepared', 'approved', 'date ', 'meeting',
    'subject', 'recommended', 'discussion', 'updates', 'project schedule',
    'estimated schedule', 'capital improvement projects', 'disaster recovery projects'
)

for d in docs:
    lines = [ln.strip() for ln in d.get('text','').splitlines()]
    for i, ln in enumerate(lines):
        if (not ln) or (':' in ln):
            continue
        if (len(ln) < 4) or (len(ln) > 120):
            continue
        low = ln.lower()
        if low.startswith(skip_prefixes):
            continue
        if ln.startswith('(cid') or ln.startswith('•') or ln.startswith('-') or ln.startswith('–'):
            continue
        if not name_re.match(ln):
            continue
        window = "\n".join(lines[i+1:i+25])
        if any(p.search(window) for p in spring2022_patterns):
            project_starts.setdefault(ln, set()).add('Spring 2022')

projects = sorted(project_starts.keys())

print('__RESULT__:')
print(json.dumps({'projects': projects, 'count': len(projects)}))"""

env_args = {'var_call_GU7TOrWp60QnSxcfBDDbjJb3': ['civic_docs'], 'var_call_oT345mwgQj4Nim0YXkOkj7b9': ['Funding'], 'var_call_4kyFbfoBMGRtUpextA1f4p3h': 'file_storage/call_4kyFbfoBMGRtUpextA1f4p3h.json'}

exec(code, env_args)
