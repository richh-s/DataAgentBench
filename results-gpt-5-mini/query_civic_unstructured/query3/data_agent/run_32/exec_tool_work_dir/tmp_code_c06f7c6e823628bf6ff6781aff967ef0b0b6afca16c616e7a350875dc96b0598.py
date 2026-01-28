code = """import json
# Load stored results
with open(var_call_IkHKtTihYjPSZo8aZpBDmyFU, 'r') as f:
    funding = json.load(f)
with open(var_call_c6lEJx4mdV92C2C8eH4Z8cxt, 'r') as f:
    civic_docs = json.load(f)

# normalize amount to int where possible
for rec in funding:
    amt = rec.get('Amount')
    try:
        rec['Amount'] = int(amt) if amt is not None and str(amt) != '' else None
    except:
        try:
            rec['Amount'] = int(float(amt))
        except:
            rec['Amount'] = None

# helper to strip trailing parenthetical
def strip_paren(s):
    if s is None:
        return s
    i = s.rfind('(')
    if i != -1:
        return s[:i].strip()
    return s.strip()

# combine civic texts
combined = "\n\n".join(d.get('text','') for d in civic_docs).lower()

keywords = ['fema', 'emergency', 'sirens', 'outdoor warning', 'warning']
results = []
seen = set()

# first, find funding records whose project names include keywords
for rec in funding:
    pname = rec.get('Project_Name') or ''
    pname_l = pname.lower()
    pname_strip = strip_paren(pname).lower()
    if any(k in pname_l for k in keywords) or any(k in pname_strip for k in keywords):
        # determine status by finding pname_strip in combined text
        status = 'design'
        if pname_strip and pname_strip in combined:
            idx = combined.find(pname_strip)
            window = combined[max(0, idx-200): idx+200]
            if 'construction was completed' in window or 'notice of completion' in window or 'completed' in window:
                status = 'completed'
            elif 'not started' in window or 'not begun' in window:
                status = 'not started'
            else:
                status = 'design'
        results.append({'Project_Name': pname, 'Funding_Source': rec.get('Funding_Source'), 'Amount': rec.get('Amount'), 'Status': status})
        seen.add(pname)

# Next, scan civic docs for lines mentioning keywords and grab nearby headings
lines = combined.splitlines()
for i, line in enumerate(lines):
    if any(k in line for k in keywords):
        # look up to 3 lines above for a candidate name
        candidate = None
        for j in range(1,4):
            if i-j >=0:
                cand = lines[i-j].strip()
                if len(cand) > 3 and len(cand) < 120:
                    candidate = cand
                    break
        if not candidate:
            candidate = line.strip()
        # title case for display
        display = ' '.join(w.capitalize() for w in candidate.split())
        # if not already in results, try to match to funding table by stripped name
        matched = False
        for rec in funding:
            fn = rec.get('Project_Name') or ''
            if strip_paren(fn).lower() == candidate.strip():
                matched = True
                if fn not in seen:
                    # determine status from window
                    idx = combined.find(candidate)
                    status = 'design'
                    if idx != -1:
                        window = combined[max(0, idx-200): idx+200]
                        if 'construction was completed' in window or 'notice of completion' in window or 'completed' in window:
                            status = 'completed'
                        elif 'not started' in window or 'not begun' in window:
                            status = 'not started'
                    results.append({'Project_Name': fn, 'Funding_Source': rec.get('Funding_Source'), 'Amount': rec.get('Amount'), 'Status': status})
                    seen.add(fn)
                break
        if not matched and display not in seen:
            # determine status
            idx = combined.find(candidate)
            status = 'design'
            if idx != -1:
                window = combined[max(0, idx-200): idx+200]
                if 'construction was completed' in window or 'notice of completion' in window or 'completed' in window:
                    status = 'completed'
                elif 'not started' in window or 'not begun' in window:
                    status = 'not started'
            results.append({'Project_Name': display, 'Funding_Source': None, 'Amount': None, 'Status': status})
            seen.add(display)

# deduplicate by Project_Name
final = []
added = set()
for r in results:
    key = r['Project_Name'] or ''
    if key not in added:
        final.append(r)
        added.add(key)

# sort
final_sorted = sorted(final, key=lambda x: (x['Project_Name'] or '').lower())

print('__RESULT__:')
print(json.dumps(final_sorted))"""

env_args = {'var_call_IkHKtTihYjPSZo8aZpBDmyFU': 'file_storage/call_IkHKtTihYjPSZo8aZpBDmyFU.json', 'var_call_c6lEJx4mdV92C2C8eH4Z8cxt': 'file_storage/call_c6lEJx4mdV92C2C8eH4Z8cxt.json'}

exec(code, env_args)
