code = """import json, re

# Load mongo docs
path = var_call_4kyFbfoBMGRtUpextA1f4p3h
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Heuristic parsing: find lines that look like project names followed shortly by a schedule line containing 'Begin' and 'Spring 2022' or 'Spring, 2022'
# We'll scan each document and build mapping project->start_token(s)
project_starts = {}

spring2022_patterns = [
    re.compile(r'\bBegin\s+Construction\s*:\s*Spring\s*,?\s*2022\b', re.IGNORECASE),
    re.compile(r'\bBegin\s+Construction\s*:\s*Spring\s+2022\b', re.IGNORECASE),
    re.compile(r'\bBegin\s+Construction\s*:\s*Spring\s*2022\b', re.IGNORECASE),
    re.compile(r'\bAdvertise\s*:\s*Spring\s*,?\s*2022\b', re.IGNORECASE),
    re.compile(r'\bBegin\s+Project\s*:\s*Spring\s*,?\s*2022\b', re.IGNORECASE),
]

# project name line heuristic: a line with letters/numbers/&/()/' and not too long, not starting with bullets, and not containing ':'
name_re = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 ,&\-\(\)\/'\.]+$")

for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    # keep index mapping
    for i, ln in enumerate(lines):
        if not ln or ':' in ln:  # name lines often without colon
            continue
        if len(ln) < 4 or len(ln) > 120:
            continue
        if ln.lower().startswith(('page ', 'agenda', 'to ', 'prepared', 'approved', 'date ', 'meeting', 'subject', 'recommended', 'discussion', 'updates', 'project schedule', 'estimated schedule')):
            continue
        if ln.startswith(('(cid', '•', '-', '–')):
            continue
        if not name_re.match(ln):
            continue
        # look ahead a small window for spring 2022 begin construction etc
        window = "\n".join(lines[i+1:i+25])
        if any(p.search(window) for p in spring2022_patterns):
            project_starts.setdefault(ln, set()).add('Spring 2022')

projects = sorted(project_starts.keys())

print('__RESULT__:')
print(json.dumps({'projects': projects, 'count': len(projects)}))"""

env_args = {'var_call_GU7TOrWp60QnSxcfBDDbjJb3': ['civic_docs'], 'var_call_oT345mwgQj4Nim0YXkOkj7b9': ['Funding'], 'var_call_4kyFbfoBMGRtUpextA1f4p3h': 'file_storage/call_4kyFbfoBMGRtUpextA1f4p3h.json'}

exec(code, env_args)
