code = """import json, re
# Load the full civic docs query result from the provided file path
path = var_call_kESzRD6axEvtHVPDcXvLTW1P
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

candidates = {}

def infer_status(snippet):
    s = snippet.lower()
    if 'construction was completed' in s or 'complete construction' in s or 'notice of completion' in s or 'completed' in s:
        return 'completed'
    if 'not started' in s or 'not begun' in s or 'identified' in s:
        return 'not started'
    if 'design' in s or 'preliminary design' in s or 'complete design' in s or 'working with the consultant' in s or 'finalize the design' in s:
        return 'design'
    # if under construction but not complete
    if 'under construction' in s or 'begin construction' in s or 'begin construction' in s:
        return 'design'
    return 'design'

for doc in docs:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    # find lines containing fema or emergency
    for i, ln in enumerate(lines):
        if re.search(r'\b(fema|emergency)\b', ln, re.I):
            # look up to 4 previous non-empty lines for a title-like line
            for j in range(1,5):
                idx = i-j
                if idx < 0: break
                cand = lines[idx]
                if not cand: continue
                # heuristics: title-like contains words and not too long
                words = cand.split()
                if 2 <= len(words) <= 10:
                    # filter out generic headers
                    if any(k in cand.lower() for k in ['agenda','page','meeting','item','report','updates','discussion','prepared','approved']):
                        continue
                    # also prefer lines that contain Project or words like Repairs, Improvements, Facility, Park, Road, Drainage, Warning, Signal
                    if re.search(r'project|repairs|improvements|facility|park|road|drainage|warning|signal|project:', cand, re.I) or cand.isupper() or cand.istitle():
                        title = re.sub(r"\s+"," ", cand).strip(' :\n')
                        # capture snippet around title for status inference
                        # take subsequent up to 6 lines as snippet
                        snippet_lines = []
                        for k in range(i, min(i+6, len(lines))):
                            if lines[k]: snippet_lines.append(lines[k])
                        snippet = ' '.join(snippet_lines)
                        status = infer_status(snippet + ' ' + cand)
                        candidates[title] = status
                        break
            # also try to find nearest preceding line that contains 'Project' explicitly
            # (if above didn't capture)
    # Additionally, look for lines that mention FEMA in same paragraph as project name with parentheses
    # find patterns like 'Latigo Canyon Road Retaining Wall Repair Project' with 'FEMA/CalOES' nearby
    for m in re.finditer(r'([A-Z][A-Za-z0-9 &'"\-/,]{5,80}?Project|Repairs|Improvements|Facility|Park|Road)[\s\S]{0,200}?\b(FEMA|CalOES|emergency)\b', text, re.I):
        title = m.group(1).strip(' :\n')
        snippet = text[m.start():m.end()]
        status = infer_status(snippet)
        candidates[title] = status

# If no candidates found, fall back to scanning for known FEMA mentions with nearby project titles like 'Latigo Canyon Road Retaining Wall Repair Project'

# Prepare output list of dicts
out = []
for name, status in candidates.items():
    out.append({'Project_Name': name, 'Status': status})

# sort for consistency
out = sorted(out, key=lambda x: x['Project_Name'])
import json
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WKtxU0jxPJ15joDyaPmwBSnF': ['civic_docs'], 'var_call_jGUa9xleKbwSjDyorm3VrObQ': ['Funding'], 'var_call_kESzRD6axEvtHVPDcXvLTW1P': 'file_storage/call_kESzRD6axEvtHVPDcXvLTW1P.json'}

exec(code, env_args)
