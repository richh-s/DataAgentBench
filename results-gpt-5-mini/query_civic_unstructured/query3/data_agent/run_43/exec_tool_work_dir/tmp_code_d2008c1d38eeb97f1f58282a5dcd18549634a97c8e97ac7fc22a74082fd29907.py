code = """import json
import re
from pathlib import Path

civic_docs_path = Path(var_call_owt1CJlXOW5XHdAgyXm7RWEF)
funding_path = Path(var_call_nGx2atNIB0SdTXF5VUqvFXNi)

with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

funding_records = funding

keywords = ['fema', 'emergency', 'outdoor warning', 'warning', 'emergency warning']

candidates = []
for rec in funding_records:
    name = rec.get('Project_Name','') or ''
    source = rec.get('Funding_Source','') or ''
    lname = name.lower()
    lsource = source.lower()
    if any(k in lname for k in keywords) or any(k in lsource for k in ['federal assistance','fema']):
        candidates.append(rec)

for rec in funding_records:
    name = rec.get('Project_Name','') or ''
    lname = name.lower()
    if '(fema' in lname or 'fema/' in lname or ('fema' in lname and rec not in candidates):
        if rec not in candidates:
            candidates.append(rec)

# Deduplicate
unique = {}
for rec in candidates:
    unique[rec['Project_Name']] = rec
candidates = list(unique.values())

# helper to infer status
def infer_status_from_context(text, idx_start):
    window_start = max(0, idx_start - 2000)
    context = text[window_start: idx_start + 2000]
    lc = context.lower()
    if 'design' in lc and 'construction' not in lc:
        return 'design'
    if 'construction' in lc:
        if 'construction was completed' in lc or 'notice of completion' in lc or 'complete construction' in lc:
            return 'completed'
        if 'currently under construction' in lc:
            return 'completed'
        if 'begin construction' in lc:
            return 'not started'
    if 'not started' in lc or 'will be' in lc or 'identified' in lc or 'waiting' in lc or 'awaiting' in lc:
        return 'not started'
    if 'working with the consultant' in lc or 'finalize the design' in lc or 'finalizing the design' in lc or 'final design' in lc or 'preliminary design' in lc:
        return 'design'
    if 'completed' in lc or 'notice of completion' in lc:
        return 'completed'
    return None

all_texts = "\n\n".join(d.get('text','') for d in civic_docs)
lower_text = all_texts.lower()

results = []
for rec in candidates:
    pname = rec.get('Project_Name','')
    lname = pname.lower()
    status = None
    idx = lower_text.find(lname)
    if idx != -1:
        status = infer_status_from_context(all_texts, idx)
    else:
        simple = re.sub(r'\(.*?\)', '', lname).strip()
        if simple and simple in lower_text:
            idx = lower_text.find(simple)
            status = infer_status_from_context(all_texts, idx)
        else:
            tokens = [t for t in ['outdoor warning','warning','emergency','latigo canyon','clover heights','encinal canyon','guardrail','outdoor warning sirens'] if t in lname]
            for t in tokens:
                idx = lower_text.find(t)
                if idx != -1:
                    status = infer_status_from_context(all_texts, idx)
                    break
    try:
        amount = int(str(rec.get('Amount')))
    except:
        try:
            amount = int(float(str(rec.get('Amount'))))
        except:
            amount = None
    results.append({'Project_Name': pname, 'Funding_Source': rec.get('Funding_Source'), 'Amount': amount, 'Status': status})

results = sorted(results, key=lambda x: x['Project_Name'] or '')

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_owt1CJlXOW5XHdAgyXm7RWEF': 'file_storage/call_owt1CJlXOW5XHdAgyXm7RWEF.json', 'var_call_nGx2atNIB0SdTXF5VUqvFXNi': 'file_storage/call_nGx2atNIB0SdTXF5VUqvFXNi.json'}

exec(code, env_args)
