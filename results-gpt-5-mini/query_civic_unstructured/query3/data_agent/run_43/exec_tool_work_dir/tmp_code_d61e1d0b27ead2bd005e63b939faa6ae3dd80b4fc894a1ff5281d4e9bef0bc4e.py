code = """import json
from pathlib import Path

# Read the stored results files
civic_docs_file = Path(var_call_owt1CJlXOW5XHdAgyXm7RWEF)
funding_file = Path(var_call_nGx2atNIB0SdTXF5VUqvFXNi)

with open(civic_docs_file, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(funding_file, 'r', encoding='utf-8') as f:
    funding = json.load(f)

all_text = "\n\n".join(d.get('text','') for d in civic_docs)
lt = all_text.lower()

# Find funding records that mention FEMA or emergency in project name or funding source
related = []
for rec in funding:
    pn = (rec.get('Project_Name') or '')
    fs = (rec.get('Funding_Source') or '')
    lpn = pn.lower()
    lfs = fs.lower()
    if 'fema' in lpn or 'fema' in lfs or 'emergency' in lpn or 'emergency' in lfs or 'outdoor warning' in lpn or 'warning' in lpn:
        related.append(rec)

# Deduplicate by Project_Name
seen = set()
unique = []
for r in related:
    if r['Project_Name'] not in seen:
        seen.add(r['Project_Name'])
        unique.append(r)

# Infer status for these using simple heuristics
def infer_status_from_text(project_name):
    name = (project_name or '').lower()
    idx = lt.find(name)
    if idx != -1:
        context = lt[max(0, idx-300): idx+300]
        if 'complete design' in context or 'final design' in context or 'preliminary design' in context or 'finalize the design' in context:
            return 'design'
        if 'construction was completed' in context or 'notice of completion' in context or 'complete construction' in context:
            return 'completed'
        if 'currently under construction' in context:
            return 'completed'
        if 'begin construction' in context or 'advertise' in context or 'will begin' in context or 'begin construction:' in context:
            return 'not started'
        if 'not started' in context or 'identified' in context or 'waiting' in context or 'awaiting' in context:
            return 'not started'
    # fallback: check for keywords
    for kw in ['outdoor warning', 'outdoor warning sirens', 'fema', 'emergency', 'latigo canyon', 'clover heights', 'encinal canyon', 'guardrail']:
        idx2 = lt.find(kw)
        if idx2 != -1:
            context = lt[max(0, idx2-300): idx2+300]
            if 'complete design' in context or 'final design' in context or 'preliminary design' in context:
                return 'design'
            if 'construction was completed' in context or 'notice of completion' in context or 'complete construction' in context:
                return 'completed'
            if 'currently under construction' in context:
                return 'completed'
            if 'begin construction' in context or 'advertise' in context or 'will begin' in context or 'begin construction:' in context:
                return 'not started'
            if 'not started' in context or 'identified' in context or 'waiting' in context or 'awaiting' in context:
                return 'not started'
    return None

results = []
for r in unique:
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
    status = infer_status_from_text(pn)
    results.append({'Project_Name': pn, 'Funding_Source': fs, 'Amount': amount, 'Status': status})

results = sorted(results, key=lambda x: x['Project_Name'] or '')

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_owt1CJlXOW5XHdAgyXm7RWEF': 'file_storage/call_owt1CJlXOW5XHdAgyXm7RWEF.json', 'var_call_nGx2atNIB0SdTXF5VUqvFXNi': 'file_storage/call_nGx2atNIB0SdTXF5VUqvFXNi.json', 'var_call_575iBL723EDmXFioDtbQt63H': 'ok'}

exec(code, env_args)
