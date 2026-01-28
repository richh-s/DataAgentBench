code = """import json
import re

# Load data from storage file paths provided by previous tool calls
with open(var_call_CHWKaz9CJKOfQ2VL3FnKxhnX, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_0EQqnWVhr6zNhR7UcxXNBDd9, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding amounts to integers where possible
for r in funding:
    amt = r.get('Amount')
    try:
        r['Amount'] = int(amt)
    except Exception:
        try:
            r['Amount'] = int(float(amt))
        except Exception:
            r['Amount'] = None

# Helper functions
def normalize_name(name):
    if not name:
        return ''
    # remove parenthetical suffixes like (FEMA Project)
    s = re.sub(r"\s*\([^)]*\)", '', name)
    # remove non-alphanumeric
    s = re.sub(r"[^\w\s]", ' ', s)
    s = re.sub(r"\s+", ' ', s).strip().lower()
    return s

# Build list of documents with lowercased text for searching
docs = []
for d in civic_docs:
    docs.append({'filename': d.get('filename',''), 'text': d.get('text','').lower()})

# Search criteria
results = []
for rec in funding:
    pname = rec.get('Project_Name','')
    pname_norm = normalize_name(pname)
    included = False
    status = None

    # Criterion A: project name contains 'fema'
    if re.search(r'fema', pname, re.IGNORECASE):
        included = True
        reason = 'name contains FEMA'

    # Criterion B: project name contains emergency-related keywords
    if not included and re.search(r'emergenc|warning|siren', pname, re.IGNORECASE):
        included = True
        reason = 'name suggests emergency/warning'

    # Criterion C: project name appears in any civic doc that mentions emergency or fema
    if not included:
        for d in docs:
            if 'fema' in d['text'] or 'emergency' in d['text']:
                if pname_norm and pname_norm in d['text']:
                    included = True
                    reason = 'found in civic doc with emergency/FEMA'
                    # extract nearby context to guess status
                    idx = d['text'].find(pname_norm)
                    start = max(0, idx-200)
                    end = min(len(d['text']), idx+200)
                    ctx = d['text'][start:end]
                    # look for status keywords
                    m = re.search(r'(complete|completed|under construction|construction|design|not started|preliminary design|awaiting)', ctx)
                    if m:
                        status = m.group(1)
                    break

    if included:
        # if no status found yet, search any doc for project name to find status
        if not status:
            for d in docs:
                if pname_norm and pname_norm in d['text']:
                    idx = d['text'].find(pname_norm)
                    start = max(0, idx-200)
                    end = min(len(d['text']), idx+200)
                    ctx = d['text'][start:end]
                    m = re.search(r'(complete|completed|under construction|construction|design|not started|preliminary design|awaiting)', ctx)
                    if m:
                        status = m.group(1)
                        break
        results.append({'Project_Name': rec.get('Project_Name'), 'Funding_Source': rec.get('Funding_Source'), 'Amount': rec.get('Amount'), 'Status': status})

# Also include projects whose names mention warning/siren even if not yet included
for rec in funding:
    pname = rec.get('Project_Name','')
    if re.search(r'warning|siren', pname, re.IGNORECASE):
        if not any(r['Project_Name']==rec.get('Project_Name') for r in results):
            # try to find status
            pname_norm = normalize_name(pname)
            status = None
            for d in docs:
                if pname_norm and pname_norm in d['text']:
                    idx = d['text'].find(pname_norm)
                    start = max(0, idx-200)
                    end = min(len(d['text']), idx+200)
                    ctx = d['text'][start:end]
                    m = re.search(r'(complete|completed|under construction|construction|design|not started|preliminary design|awaiting)', ctx)
                    if m:
                        status = m.group(1)
                        break
            results.append({'Project_Name': rec.get('Project_Name'), 'Funding_Source': rec.get('Funding_Source'), 'Amount': rec.get('Amount'), 'Status': status})

# Deduplicate
seen = set()
final = []
for r in results:
    key = (r['Project_Name'], r['Funding_Source'], r['Amount'])
    if key in seen:
        continue
    seen.add(key)
    final.append(r)

# Sort by project name
final_sorted = sorted(final, key=lambda x: (x['Project_Name'] or '').lower())

print("__RESULT__:")
print(json.dumps(final_sorted))"""

env_args = {'var_call_CHWKaz9CJKOfQ2VL3FnKxhnX': 'file_storage/call_CHWKaz9CJKOfQ2VL3FnKxhnX.json', 'var_call_0EQqnWVhr6zNhR7UcxXNBDd9': 'file_storage/call_0EQqnWVhr6zNhR7UcxXNBDd9.json'}

exec(code, env_args)
