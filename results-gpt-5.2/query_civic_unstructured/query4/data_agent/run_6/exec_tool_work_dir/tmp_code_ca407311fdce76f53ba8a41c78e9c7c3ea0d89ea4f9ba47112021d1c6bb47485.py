code = """import json
from pathlib import Path

raw = var_call_R4XAkIbysGnUFFK0TcQb1VNg
if isinstance(raw, str) and raw.endswith('.json'):
    docs = json.loads(Path(raw).read_text())
else:
    docs = raw

# find any mention of 'Begin Construction: Spring 2022'
projects = set()
for d in docs:
    text = d.get('text','') or ''
    if 'Begin Construction: Spring 2022' in text:
        # take preceding line as project name for each occurrence
        lines = [ln.strip() for ln in text.splitlines()]
        for idx, ln in enumerate(lines):
            if 'Begin Construction: Spring 2022' in ln:
                # walk upward to find plausible project name (non-empty, not bullet)
                j = idx-1
                while j>=0 and (lines[j]=='' or lines[j].startswith('(cid') or lines[j].startswith('Page') or lines[j].startswith('Agenda Item') or lines[j].endswith(':') or lines[j].startswith('•') or lines[j].startswith('(cid')):
                    j-=1
                if j>=0:
                    projects.add(lines[j])

out = {'count': len(projects), 'projects': sorted(projects)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_4zbtptmslrFMDJ0pQvTXodbd': ['Funding'], 'var_call_tgfFKO10EfK4xI3P4ci9kBpY': ['civic_docs'], 'var_call_R4XAkIbysGnUFFK0TcQb1VNg': 'file_storage/call_R4XAkIbysGnUFFK0TcQb1VNg.json'}

exec(code, env_args)
