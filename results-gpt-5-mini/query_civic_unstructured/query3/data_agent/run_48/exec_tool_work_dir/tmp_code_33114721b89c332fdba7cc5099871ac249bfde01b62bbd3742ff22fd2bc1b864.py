code = """import json

# Load files from storage-provided paths
with open(var_call_doKwQqZMvpmPnawdjdbN3n3o, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_wBrhbjFYhMnA5OtJjyPFnbnZ, 'r') as f:
    funding = json.load(f)

# Combine all civic docs text
all_text = '\n\n'.join(d.get('text','') for d in civic_docs)
all_text_lower = all_text.lower()

# Helper to remove parenthetical suffixes
def remove_parenthetical(s):
    if not isinstance(s, str):
        return ''
    if '(' in s:
        return s.split('(',1)[0].strip()
    return s.strip()

# Status keyword lists
design_kws = ['complete design', 'final design', 'preliminary design', 'preliminary design phase', 'working with the consultant to finalize the design', 'design plans', 'in the preliminary design phase']
completed_kws = ['construction was completed', 'project is currently under construction', 'complete construction', 'notice of completion', 'awarded the contract', 'begin construction', 'begin construction:']
notstarted_kws = ['not started', 'not begun', 'identified but not begun', 'not yet started']

results = []
seen = set()
for rec in funding:
    pname = rec.get('Project_Name','')
    lname = pname.lower()
    base = remove_parenthetical(pname).lower()
    include = False
    # include by name containing fema or emergency
    if 'fema' in lname or 'emergency' in lname:
        include = True
    # include if base appears in civic docs
    if base and base in all_text_lower:
        include = True
    # include if any long token from name appears in civic docs
    if not include:
        for tok in base.split():
            if len(tok) > 4 and tok in all_text_lower:
                include = True
                break
    if not include:
        continue
    # Infer status by searching for base or tokens in civic text
    status = 'unknown'
    idx = -1
    if base:
        idx = all_text_lower.find(base)
    if idx == -1:
        # try tokens
        for tok in base.split():
            if len(tok) > 4:
                p = all_text_lower.find(tok)
                if p != -1:
                    idx = p
                    break
    if idx != -1:
        start = max(0, idx - 400)
        end = min(len(all_text_lower), idx + 400)
        window = all_text_lower[start:end]
        # check explicit section headings before idx
        heading_start = max(0, idx - 1200)
        heading_segment = all_text_lower[heading_start:idx]
        if 'capital improvement projects (design)' in heading_segment or 'capital improvement projects (design)' in window:
            status = 'design'
        elif 'capital improvement projects (construction)' in heading_segment or 'capital improvement projects (construction)' in window:
            status = 'completed'
        elif 'capital improvement projects (not started)' in heading_segment or 'capital improvement projects (not started)' in window:
            status = 'not started'
        else:
            for kw in design_kws:
                if kw in window:
                    status = 'design'
                    break
            if status == 'unknown':
                for kw in completed_kws:
                    if kw in window:
                        status = 'completed'
                        break
            if status == 'unknown':
                for kw in notstarted_kws:
                    if kw in window:
                        status = 'not started'
                        break
    # Prepare amount
    try:
        amount = int(rec.get('Amount', 0))
    except:
        try:
            amount = int(float(rec.get('Amount', 0)))
        except:
            amount = 0
    if pname not in seen:
        results.append({'Project_Name': pname, 'Funding_Source': rec.get('Funding_Source',''), 'Amount': amount, 'Status': status})
        seen.add(pname)

# Sort results
results = sorted(results, key=lambda x: x['Project_Name'].lower())

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_doKwQqZMvpmPnawdjdbN3n3o': 'file_storage/call_doKwQqZMvpmPnawdjdbN3n3o.json', 'var_call_wBrhbjFYhMnA5OtJjyPFnbnZ': 'file_storage/call_wBrhbjFYhMnA5OtJjyPFnbnZ.json'}

exec(code, env_args)
