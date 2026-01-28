code = """import json
import re

# Load data
with open(var_call_doKwQqZMvpmPnawdjdbN3n3o, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_wBrhbjFYhMnA5OtJjyPFnbnZ, 'r') as f:
    funding = json.load(f)

# Helper functions
def remove_parenthetical(s):
    return re.sub(r"\s*\(.*?\)", "", s).strip()

def normalize(s):
    if not isinstance(s, str):
        return ''
    s2 = remove_parenthetical(s)
    s2 = s2.replace('&', ' and ')
    s2 = re.sub(r"[^0-9a-zA-Z ]+", " ", s2)
    s2 = re.sub(r"\s+", " ", s2)
    return s2.strip().lower()

# Prepare a combined civic text for searching
all_text = "\n\n".join(doc.get('text','') for doc in civic_docs)
all_text_lower = all_text.lower()

# Status detection keywords mapping
status_map_keywords = [
    (['complete design', 'final design', 'preliminary design', 'in the preliminary design phase', 'working with the consultant to finalize the design', 'design plans'], 'design'),
    (['begin construction', 'construction was completed', 'project is currently under construction', 'complete construction', 'complete construction:','notice of completion','awarded the contract','begin construction:'], 'completed'),
    (['not started', 'not begun', 'identified but not begun', 'not yet started'], 'not started')
]

# A helper to infer status by context window
def infer_status_by_context(name_variants):
    # name_variants: list of strings to search (lowercase)
    for nv in name_variants:
        idx = all_text_lower.find(nv)
        if idx != -1:
            # extract window
            start = max(0, idx-400)
            end = min(len(all_text_lower), idx+400)
            window = all_text_lower[start:end]
            # check headings before idx within 2000 chars for explicit section headings
            heading_start = max(0, idx-2000)
            heading_segment = all_text_lower[heading_start:idx]
            if 'capital improvement projects (design)' in heading_segment or 'capital improvement projects (design)' in window:
                return 'design'
            if 'capital improvement projects (construction)' in heading_segment or 'capital improvement projects (construction)' in window:
                return 'completed'
            if 'capital improvement projects (not started)' in heading_segment or 'capital improvement projects (not started)' in window:
                return 'not started'
            # check keyword lists
            for kws, st in status_map_keywords:
                for kw in kws:
                    if kw in window:
                        return st
    return 'unknown'

results = []
seen = set()
for rec in funding:
    pname = rec.get('Project_Name','')
    pname_lower = pname.lower()
    base = remove_parenthetical(pname)
    norm = normalize(pname)
    include = False
    # include by name containing fema or emergency
    if 'fema' in pname_lower or 'emergency' in pname_lower:
        include = True
    # include if base appears in civic docs text
    base_lower = base.lower()
    if base_lower and base_lower in all_text_lower:
        include = True
    # include if normalized name fragments appear in civic text
    if not include:
        for part in norm.split():
            if len(part) > 4 and part in all_text_lower:
                include = True
                break
    if include:
        # infer status
        name_variants = [pname.lower(), base_lower, norm]
        status = infer_status_by_context([nv for nv in name_variants if nv])
        # Append result
        if pname not in seen:
            try:
                amount = int(rec.get('Amount',0))
            except:
                try:
                    amount = int(float(rec.get('Amount',0)))
                except:
                    amount = 0
            results.append({
                'Project_Name': pname,
                'Funding_Source': rec.get('Funding_Source',''),
                'Amount': amount,
                'Status': status
            })
            seen.add(pname)

# Sort results
results = sorted(results, key=lambda x: x['Project_Name'].lower())

import json as _json
print("__RESULT__:")
print(_json.dumps(results))"""

env_args = {'var_call_doKwQqZMvpmPnawdjdbN3n3o': 'file_storage/call_doKwQqZMvpmPnawdjdbN3n3o.json', 'var_call_wBrhbjFYhMnA5OtJjyPFnbnZ': 'file_storage/call_wBrhbjFYhMnA5OtJjyPFnbnZ.json'}

exec(code, env_args)
