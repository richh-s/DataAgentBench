code = """import json
# Load stored JSON file paths from provided variables
with open(var_call_IkHKtTihYjPSZo8aZpBDmyFU, 'r') as f:
    funding = json.load(f)
with open(var_call_c6lEJx4mdV92C2C8eH4Z8cxt, 'r') as f:
    civic_docs = json.load(f)

# Combine civic texts
combined_text = '\n\n'.join(d.get('text','') for d in civic_docs).lower()

# Helper to strip trailing parenthetical
def strip_paren(name):
    if not name:
        return ''
    idx = name.rfind('(')
    if idx != -1:
        return name[:idx].strip()
    return name.strip()

keywords = ['fema', 'emergency', 'sirens', 'outdoor warning', 'warning']
results = []
seen = set()

# Find funding records whose Project_Name mentions keywords
for rec in funding:
    pname = rec.get('Project_Name') or ''
    pname_l = pname.lower()
    pname_strip = strip_paren(pname).lower()
    if any(k in pname_l for k in keywords) or any(k in pname_strip for k in keywords):
        status = 'design'
        if pname_strip and pname_strip in combined_text:
            window = combined_text
            if 'completed' in window or 'notice of completion' in window:
                status = 'completed'
            elif 'not started' in window or 'not begun' in window:
                status = 'not started'
            else:
                status = 'design'
        results.append({'Project_Name': pname, 'Funding_Source': rec.get('Funding_Source'), 'Amount': int(rec.get('Amount')) if rec.get('Amount') not in (None, '') else None, 'Status': status})
        seen.add(pname)

# Scan civic docs for lines with keywords and grab preceding lines as names
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if any(k in low for k in keywords):
            # look up to 3 lines above
            candidate = None
            for j in range(1,4):
                if i-j >= 0:
                    cand = lines[i-j].strip()
                    if 3 < len(cand) < 120:
                        candidate = cand
                        break
            if not candidate:
                candidate = line.strip()
            display = ' '.join(w.capitalize() for w in candidate.split())
            if display not in seen:
                # determine status crudely
                status = 'design'
                lowtext = text.lower()
                if 'completed' in lowtext or 'notice of completion' in lowtext:
                    status = 'completed'
                elif 'not started' in lowtext or 'not begun' in lowtext:
                    status = 'not started'
                results.append({'Project_Name': display, 'Funding_Source': None, 'Amount': None, 'Status': status})
                seen.add(display)

# Deduplicate by Project_Name preserving first
final = []
added = set()
for r in results:
    key = r['Project_Name'] or ''
    if key not in added:
        final.append(r)
        added.add(key)

# Sort
final_sorted = sorted(final, key=lambda x: (x['Project_Name'] or '').lower())

print('__RESULT__:')
print(json.dumps(final_sorted))"""

env_args = {'var_call_IkHKtTihYjPSZo8aZpBDmyFU': 'file_storage/call_IkHKtTihYjPSZo8aZpBDmyFU.json', 'var_call_c6lEJx4mdV92C2C8eH4Z8cxt': 'file_storage/call_c6lEJx4mdV92C2C8eH4Z8cxt.json'}

exec(code, env_args)
