code = """import json
# Load files from storage variables
with open(var_call_IkHKtTihYjPSZo8aZpBDmyFU, 'r') as f:
    funding = json.load(f)
with open(var_call_c6lEJx4mdV92C2C8eH4Z8cxt, 'r') as f:
    civic_docs = json.load(f)

combined = "\n".join(d.get('text','') for d in civic_docs).lower()
keywords = ['fema','emergency','sirens','outdoor warning','warning']
results = []
seen = set()

for rec in funding:
    pname = rec.get('Project_Name') or ''
    pname_l = pname.lower()
    if any(k in pname_l for k in keywords):
        # amount to int if possible
        amt = rec.get('Amount')
        try:
            amt_i = int(amt) if amt not in (None, '') else None
        except:
            try:
                amt_i = int(float(amt))
            except:
                amt_i = None
        # determine status simply
        status = 'design'
        if pname_l in combined:
            if 'completed' in combined:
                status = 'completed'
            elif 'not started' in combined:
                status = 'not started'
            else:
                status = 'design'
        results.append({'Project_Name': pname, 'Funding_Source': rec.get('Funding_Source'), 'Amount': amt_i, 'Status': status})
        seen.add(pname)

# Add any civic doc mentions of outdoor warning or sirens
if 'outdoor warning' in combined or 'sirens' in combined or 'outdoor warning signs' in combined:
    name = 'Outdoor Warning Signs'
    if name not in seen:
        # try to find if funding table has matching entry
        matched = None
        for rec in funding:
            if rec.get('Project_Name') and rec.get('Project_Name').lower().startswith('outdoor warning'):
                matched = rec
                break
        if matched:
            try:
                amt = int(matched.get('Amount')) if matched.get('Amount') not in (None,'') else None
            except:
                amt = None
            # determine status
            status = 'design'
            if 'completed' in combined:
                status = 'completed'
            elif 'not started' in combined:
                status = 'not started'
            results.append({'Project_Name': matched.get('Project_Name'), 'Funding_Source': matched.get('Funding_Source'), 'Amount': amt, 'Status': status})
            seen.add(matched.get('Project_Name'))
        else:
            status = 'design'
            if 'completed' in combined:
                status = 'completed'
            elif 'not started' in combined:
                status = 'not started'
            results.append({'Project_Name': name, 'Funding_Source': None, 'Amount': None, 'Status': status})
            seen.add(name)

# Deduplicate
final = []
added = set()
for r in results:
    key = r.get('Project_Name') or ''
    if key not in added:
        final.append(r)
        added.add(key)

final_sorted = sorted(final, key=lambda x: (x['Project_Name'] or '').lower())

print('__RESULT__:')
print(json.dumps(final_sorted))"""

env_args = {'var_call_IkHKtTihYjPSZo8aZpBDmyFU': 'file_storage/call_IkHKtTihYjPSZo8aZpBDmyFU.json', 'var_call_c6lEJx4mdV92C2C8eH4Z8cxt': 'file_storage/call_c6lEJx4mdV92C2C8eH4Z8cxt.json'}

exec(code, env_args)
