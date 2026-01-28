code = """import json
from pathlib import Path

# Load files from storage-provided paths
with open(var_call_owt1CJlXOW5XHdAgyXm7RWEF, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_nGx2atNIB0SdTXF5VUqvFXNi, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Find funding records related to FEMA or emergency
keywords = ['fema', 'emergency', 'outdoor warning', 'warning']
related = []
for rec in funding:
    name = (rec.get('Project_Name') or '').lower()
    source = (rec.get('Funding_Source') or '').lower()
    if any(k in name for k in keywords) or any(k in source for k in ['federal assistance', 'fema']):
        related.append(rec)
    else:
        # include if project name contains '(fema' or 'fema/'
        if '(fema' in name or 'fema/' in name:
            related.append(rec)

# Deduplicate by Project_Name
seen = set()
unique_related = []
for r in related:
    pn = r.get('Project_Name')
    if pn not in seen:
        seen.add(pn)
        unique_related.append(r)

# Combine all civic docs text
all_text = "\n\n".join(d.get('text','') for d in civic_docs)
lt = all_text.lower()

# Helper to infer status by looking for phrases near the project name or keywords
def infer_status(project_name):
    pn = (project_name or '').lower()
    # search for exact project name
    idx = lt.find(pn)
    if idx == -1:
        # try without parenthetical suffix
        if '(' in pn:
            pn_simple = pn.split('(')[0].strip()
            idx = lt.find(pn_simple)
    if idx != -1:
        context = lt[max(0, idx-200): idx+200]
        if 'complete design' in context or 'final design' in context or 'preliminary design' in context or 'finalize the design' in context:
            return 'design'
        if 'construction was completed' in context or 'notice of completion' in context or 'complete construction' in context:
            return 'completed'
        if 'currently under construction' in context:
            return 'completed'
        if 'begin construction' in context or 'advertise' in context or 'will begin' in context:
            return 'not started'
        if 'not started' in context or 'identified' in context or 'waiting' in context or 'awaiting' in context:
            return 'not started'
    # if project name not found, check keywords
    for kw in ['outdoor warning', 'outdoor warning sirens', 'fema', 'emergency', 'latigo canyon', 'clover heights', 'encinal canyon', 'guardrail']:
        if kw in pn or kw in lt:
            idx2 = lt.find(kw)
            if idx2 != -1:
                context = lt[max(0, idx2-200): idx2+200]
                if 'complete design' in context or 'final design' in context or 'preliminary design' in context:
                    return 'design'
                if 'construction was completed' in context or 'notice of completion' in context or 'complete construction' in context:
                    return 'completed'
                if 'currently under construction' in context:
                    return 'completed'
                if 'begin construction' in context or 'advertise' in context or 'will begin' in context:
                    return 'not started'
                if 'not started' in context or 'identified' in context or 'waiting' in context or 'awaiting' in context:
                    return 'not started'
    return None

results = []
for r in unique_related:
    pn = r.get('Project_Name')
    fs = r.get('Funding_Source')
    amt = r.get('Amount')
    try:
        amount = int(str(amt))
    except:
        try:
            amount = int(float(str(amt)))
        except:
            amount = None
    status = infer_status(pn)
    results.append({'Project_Name': pn, 'Funding_Source': fs, 'Amount': amount, 'Status': status})

# Sort results
results = sorted(results, key=lambda x: x['Project_Name'] or '')

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_owt1CJlXOW5XHdAgyXm7RWEF': 'file_storage/call_owt1CJlXOW5XHdAgyXm7RWEF.json', 'var_call_nGx2atNIB0SdTXF5VUqvFXNi': 'file_storage/call_nGx2atNIB0SdTXF5VUqvFXNi.json'}

exec(code, env_args)
