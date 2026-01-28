code = """import json, re
import pandas as pd

# Load civic docs (may be a filepath)
docs = var_call_tusdBk6MktgfX48BczKJWKck
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

texts = [(d.get('filename',''), d.get('text','') or '') for d in docs]

# Extract project names under 'Capital Improvement Projects (Design)'
projects_design = set()

header_pat = re.compile(r'Capital Improvement Projects\s*\(\s*Design\s*\)', re.IGNORECASE)
stop_pat = re.compile(r'Capital Improvement Projects\s*\(\s*(Construction|Not Started)\s*\)|Disaster Recovery Projects', re.IGNORECASE)

for fn, text in texts:
    for m in header_pat.finditer(text):
        start = m.end()
        rest = text[start:]
        sm = stop_pat.search(rest)
        section = rest[:sm.start()] if sm else rest
        # Normalize bullets artifacts
        lines = [ln.strip() for ln in section.splitlines()]
        # Candidate lines: non-empty, not starting with bullets/updates/schedule/page/etc.
        for ln in lines:
            if not ln:
                continue
            low = ln.lower()
            if low.startswith(('(cid', '•', '-', 'updates', 'project schedule', 'estimated schedule', 'project description', 'page ', 'agenda item', 'begin construction', 'advertise', 'complete design', 'final design', 'project updates', 'discussion', 'recommended action')):
                continue
            if ':' in ln and low.split(':',1)[0] in {'to','prepared by','approved by','date prepared','meeting date','subject','recommended action','discussion'}:
                continue
            # project name heuristic: mostly words, not too long, no sentence punctuation
            if len(ln) > 3 and len(ln) <= 120 and not re.search(r'[\.\?]$', ln):
                # exclude headings
                if re.search(r'capital improvement projects', low):
                    continue
                if re.search(r'\(design\)|\(construction\)|\(not started\)', low):
                    continue
                # Avoid schedule lines like 'Complete Design: Summer 2023'
                if re.match(r'^(complete|begin|advertise|final)\s', low):
                    continue
                # Avoid generic terms
                if low in {'updates'}:
                    continue
                projects_design.add(ln)

# Query funding: projects with any funding amount > 50000 (or sum? use any record > 50000 per question)
# We'll compute from Funding table via earlier count-only isn't enough; re-query names.

print('__RESULT__:')
print(json.dumps({'design_projects_extracted_count': len(projects_design), 'sample': sorted(list(projects_design))[:30]}))"""

env_args = {'var_call_eAygeFmmLDqweYUC98CP3LRU': [{'cnt': '276'}], 'var_call_tusdBk6MktgfX48BczKJWKck': 'file_storage/call_tusdBk6MktgfX48BczKJWKck.json'}

exec(code, env_args)
