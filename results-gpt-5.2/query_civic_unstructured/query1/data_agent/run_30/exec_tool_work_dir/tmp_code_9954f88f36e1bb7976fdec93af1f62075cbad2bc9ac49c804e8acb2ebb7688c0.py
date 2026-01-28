code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

funding_over50 = load_records(var_call_G8YIn2X1XbS5zYzBHUtK9cwS)
project_set = {r['Project_Name'] for r in funding_over50}

# Load civic docs
civic_docs = load_records(var_call_XV0ezgGn05vwV7MbBcWjAzCX)

# Heuristic extraction of project names under 'Capital Improvement Projects (Design)'
# We will scan text blocks that start with that header, and then collect subsequent non-empty lines
# that look like project titles (not bullets/updates/schedule/section headers).
section_header = re.compile(r'^Capital Improvement Projects \(Design\)\s*$', re.IGNORECASE)
stop_header = re.compile(r'^(Capital Improvement Projects \((Construction|Not Started)\)|Disaster Recovery Projects|Page \d+ of \d+|Agenda Item|RECOMMENDED ACTION|DISCUSSION:)', re.IGNORECASE)

exclude_prefix = re.compile(r'^(\(cid:|\u2022|\*|\-|\(|Updates:|Project Schedule|Estimated Schedule|Project Description|Complete Design|Advertise|Begin Construction|Final Design|Receive and file|Staff|City|Consultant)', re.IGNORECASE)

possible_names = set()

for doc in civic_docs:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    in_design = False
    for ln in lines:
        if not in_design:
            if section_header.match(ln):
                in_design = True
            continue
        # in_design
        if stop_header.match(ln):
            in_design = False
            continue
        if not ln:
            continue
        # skip obvious non-title lines
        if exclude_prefix.match(ln):
            continue
        # skip if line is all caps section label-ish
        if re.fullmatch(r'[A-Z0-9\s\-&/]+', ln) and len(ln.split())<=6:
            continue
        # remove trailing punctuation
        name = re.sub(r'\s+$','',ln)
        # titles likely not too long and not sentences
        if len(name) > 3 and len(name) <= 120 and not name.endswith(':'):
            # stop if line looks like a sentence
            if name.count('.')==0 and not re.search(r'\bwill\b|\bis\b|\bare\b|\bto\b', name, flags=re.I):
                possible_names.add(name)

# Compute intersection with funded >50k
funded_design = sorted([n for n in possible_names if n in project_set])

result = {
    "count": len(funded_design),
    "projects": funded_design[:50],
    "projects_truncated": len(funded_design) > 50
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_TRnkZuZ3HVNk1Y8GB8ORWYBS': [{'cnt': '276'}], 'var_call_XV0ezgGn05vwV7MbBcWjAzCX': 'file_storage/call_XV0ezgGn05vwV7MbBcWjAzCX.json', 'var_call_G8YIn2X1XbS5zYzBHUtK9cwS': 'file_storage/call_G8YIn2X1XbS5zYzBHUtK9cwS.json', 'var_call_oM95ZrTWwSwXqETgn2HKBmSn': 'file_storage/call_oM95ZrTWwSwXqETgn2HKBmSn.json', 'var_call_rsivAWManI1eQqRH1ZLlLGqO': ['Funding'], 'var_call_cGSBEi6ANoThJ73JWueRaRfI': ['civic_docs']}

exec(code, env_args)
