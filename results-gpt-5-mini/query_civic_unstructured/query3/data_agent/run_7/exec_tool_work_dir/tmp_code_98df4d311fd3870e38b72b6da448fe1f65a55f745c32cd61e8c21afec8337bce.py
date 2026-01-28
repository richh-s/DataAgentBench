code = """import json
from pathlib import Path

civic_path = Path(var_call_O41YPgIMwwpDQ0mDeNFIYiWp)
funding_path = Path(var_call_nwCBWIyTNPQah9PPbJJOWmRT)

civic = json.loads(civic_path.read_text())
funding = json.loads(funding_path.read_text())

combined = ' '.join(d.get('text','') for d in civic)
combined_low = combined.lower()

keywords = ['fema','emergency','sirens','outdoor warning','warning']

results = []

for f in funding:
    pname = f.get('Project_Name','')
    plow = pname.lower()
    base = pname.split('(')[0].strip().lower()
    include = False
    # direct name match
    if any(k in plow for k in keywords):
        include = True
    # if base mentioned in civic docs and docs mention fema/emergency
    if base and base in combined_low and ('fema' in combined_low or 'emergency' in combined_low):
        include = True
    if include:
        # extract status
        status = 'status not found'
        if base and base in combined_low:
            idx = combined_low.find(base)
            window = combined[idx: idx+600]
            wlow = window.lower()
            phrases = ['under construction','construction was completed','complete construction','complete design','design','not started','preliminary design','awaiting final','project is delayed','advertise','begin construction']
            found = None
            for p in phrases:
                if p in wlow:
                    found = p
                    break
            if found:
                status = found
            else:
                # attempt to find heading before
                # find substring before base up to 200 chars
                start = max(0, idx-200)
                heading = combined[start: idx].strip().split('.')[-1]
                if len(heading) < 100 and len(heading) > 0:
                    status = heading
        results.append({'Project_Name': pname, 'Funding_Source': f.get('Funding_Source'), 'Amount': int(f.get('Amount')) if str(f.get('Amount')).isdigit() else None, 'Status': status})

# dedupe by project name
seen = set()
final = []
for r in results:
    if r['Project_Name'] in seen:
        continue
    seen.add(r['Project_Name'])
    final.append(r)

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_O41YPgIMwwpDQ0mDeNFIYiWp': 'file_storage/call_O41YPgIMwwpDQ0mDeNFIYiWp.json', 'var_call_nwCBWIyTNPQah9PPbJJOWmRT': 'file_storage/call_nwCBWIyTNPQah9PPbJJOWmRT.json', 'var_call_aYt4NsGlTLq0WSd9YxToc5f3': {'civic_var': 'file_storage/call_O41YPgIMwwpDQ0mDeNFIYiWp.json', 'funding_var': 'file_storage/call_nwCBWIyTNPQah9PPbJJOWmRT.json'}}

exec(code, env_args)
