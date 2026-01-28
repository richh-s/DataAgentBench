code = """import json, re
# Load data from storage paths
with open(var_call_IkHKtTihYjPSZo8aZpBDmyFU, 'r') as f:
    funding = json.load(f)
with open(var_call_c6lEJx4mdV92C2C8eH4Z8cxt, 'r') as f:
    civic_docs = json.load(f)

# normalize amounts
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount') or 0)
    except:
        try:
            r['Amount'] = int(float(r.get('Amount')))
        except:
            r['Amount'] = None

# helper to remove trailing parenthetical
def normalize_name(name):
    if not name:
        return ''
    return re.sub(r"\s*\([^)]*\)\s*$", "", name).strip()

combined_text = "\n".join(d.get('text','') for d in civic_docs).lower()

keywords = ['fema', 'emergency', 'sirens', 'outdoor warning', 'warning']
relevant = []
seen_names = set()

for r in funding:
    pname = r.get('Project_Name','')
    pname_l = pname.lower()
    norm = normalize_name(pname).lower()
    match = False
    for k in keywords:
        if k in pname_l or k in norm:
            match = True
            break
    # also check for explicit '(FEMA' substring in original
    if '(fema' in pname_l:
        match = True
    if match:
        # determine status from civic docs by searching normalized name
        status = 'design'
        search_name = norm if norm else pname_l
        idx = combined_text.find(search_name)
        if idx == -1:
            # try shorter tokens from name
            parts = [p.strip() for p in re.split(r'[,:\-()]', norm) if p.strip()]
            for part in parts:
                if len(part) > 6 and part in combined_text:
                    idx = combined_text.find(part)
                    break
        if idx != -1:
            window = combined_text[max(0, idx-300): idx+300]
            if any(x in window for x in ['construction was completed', 'complete construction', 'notice of completion', 'completed,', 'completed']):
                status = 'completed'
            elif any(x in window for x in ['not started', 'not begun', 'identified but not begun']):
                status = 'not started'
            else:
                status = 'design'
        relevant.append({'Project_Name': r.get('Project_Name'), 'Funding_Source': r.get('Funding_Source'), 'Amount': r.get('Amount'), 'Status': status})
        seen_names.add(r.get('Project_Name'))

# add projects mentioned in civic docs even if not in funding table
# look for lines mentioning keywords and extract short project names nearby
lines = combined_text.splitlines()
for i, line in enumerate(lines):
    for k in keywords:
        if k in line:
            # try to get a candidate name from previous non-empty line
            name = None
            # look back up to 3 lines for a heading-like line
            for j in range(1,4):
                if i-j >= 0:
                    cand = lines[i-j].strip()
                    if len(cand) > 3 and len(cand) < 120:
                        name = cand
                        break
            if not name:
                # fallback to the line itself capitalized
                name = line.strip()
            # clean name
            name = name.strip()
            # title case it
            name_display = ' '.join(w.capitalize() for w in name.split())
            if name_display not in seen_names:
                # determine status
                idx = combined_text.find(name)
                status = 'design'
                if idx != -1:
                    window = combined_text[max(0, idx-300): idx+300]
                    if any(x in window for x in ['construction was completed', 'complete construction', 'notice of completion', 'completed,', 'completed']):
                        status = 'completed'
                    elif any(x in window for x in ['not started', 'not begun', 'identified but not begun']):
                        status = 'not started'
                    else:
                        status = 'design'
                relevant.append({'Project_Name': name_display, 'Funding_Source': None, 'Amount': None, 'Status': status})
                seen_names.add(name_display)

# deduplicate by Project_Name preserving first occurrence
final = []
seen = set()
for r in relevant:
    key = r['Project_Name'] or ''
    if key not in seen:
        seen.add(key)
        final.append(r)

# sort by Project_Name
final = sorted(final, key=lambda x: (x['Project_Name'] or '').lower())

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_IkHKtTihYjPSZo8aZpBDmyFU': 'file_storage/call_IkHKtTihYjPSZo8aZpBDmyFU.json', 'var_call_c6lEJx4mdV92C2C8eH4Z8cxt': 'file_storage/call_c6lEJx4mdV92C2C8eH4Z8cxt.json'}

exec(code, env_args)
