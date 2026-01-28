code = """import json
from pathlib import Path

# load file paths from storage variables
path_civic = Path(var_call_O41YPgIMwwpDQ0mDeNFIYiWp)
path_funding = Path(var_call_nwCBWIyTNPQah9PPbJJOWmRT)

civic = json.loads(path_civic.read_text())
funding = json.loads(path_funding.read_text())

# normalize amounts
for f in funding:
    amt = f.get('Amount')
    try:
        f['Amount'] = int(amt)
    except Exception:
        try:
            f['Amount'] = int(float(amt))
        except Exception:
            f['Amount'] = None

# helper functions
def find_status_in_text(text, project_name):
    low = text.lower()
    name = project_name.lower()
    idx = low.find(name)
    if idx == -1:
        base = project_name.split('(')[0].strip().lower()
        idx = low.find(base)
        if idx == -1:
            idx = 0
    window = text[idx: idx+1500]
    wlow = window.lower()
    # look for 'updates:'
    u = wlow.find('updates:')
    if u != -1:
        seg = window[u+8:]
        p = seg.lower().find('project schedule')
        if p != -1:
            seg = seg[:p]
        dbl = seg.find('\n\n')
        if dbl != -1:
            seg = seg[:dbl]
        return ' '.join(seg.split())
    # common status phrases
    phrases = ['under construction','construction was completed','complete construction','complete design','project is in the preliminary design phase','project is in the preliminary design']
    for ph in phrases:
        pidx = wlow.find(ph)
        if pidx != -1:
            return '...'+window[pidx:pidx+200].strip().replace('\n',' ')
    # look for section headers before occurrence
    back = text[max(0, idx-400): idx].lower()
    headers = ['capital improvement projects (design)','capital improvement projects (construction)','capital improvement projects (not started)','disaster recovery projects']
    for h in headers:
        if h in back:
            return h
    return '(status not found)'

# combined civic text
combined = '\n\n'.join(d.get('text','') for d in civic)
combined_low = combined.lower()

results = []
seen = set()

# check funding records
for f in funding:
    pname = f.get('Project_Name','')
    plow = pname.lower()
    base = pname.split('(')[0].strip()
    related = False
    if 'fema' in plow or 'emergency' in plow:
        related = True
    # check if base appears in any civic doc that mentions fema/emergency
    if base and base.lower() in combined_low:
        # find docs containing base
        for doc in civic:
            t = doc.get('text','')
            if base.lower() in t.lower():
                if 'fema' in t.lower() or 'emergency' in t.lower() or 'outdoor warning' in t.lower() or 'sirens' in t.lower():
                    related = True
                    break
    # also check keywords like 'sirens' or 'warning'
    if any(k in plow for k in ['sirens','warning','outdoor warning']):
        if 'emergency' in combined_low or 'fema' in combined_low:
            related = True
    if related:
        # find status
        status = '(status not found)'
        found = False
        if base and base.lower() in combined_low:
            for doc in civic:
                if base.lower() in doc.get('text','').lower():
                    status = find_status_in_text(doc.get('text',''), pname)
                    found = True
                    break
        if not found:
            status = find_status_in_text(combined, pname)
        rec = {'Project_Name': pname, 'Funding_Source': f.get('Funding_Source'), 'Amount': f.get('Amount'), 'Status': status}
        key = (pname, f.get('Funding_Source'))
        if key not in seen:
            results.append(rec)
            seen.add(key)

# search civic-only projects near FEMA/emergency
for doc in civic:
    t = doc.get('text','')
    low = t.lower()
    if 'fema' in low or 'emergency' in low:
        lines = t.split('\n')
        for i,line in enumerate(lines):
            if 'updates:' in line.lower():
                # previous non-empty up to 5 lines
                j = i-1
                candidate = None
                while j>=0 and i-j<=5:
                    if lines[j].strip():
                        candidate = lines[j].strip()
                        break
                    j -=1
                if candidate:
                    base = candidate.split('(')[0].strip()
                    # skip if already in results
                    if any(r['Project_Name'].split('(')[0].strip().lower() == base.lower() for r in results):
                        continue
                    status = find_status_in_text(t, candidate)
                    results.append({'Project_Name': candidate, 'Funding_Source': None, 'Amount': None, 'Status': status})

# sort results by project name
results = sorted(results, key=lambda x: x['Project_Name'].lower())

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_O41YPgIMwwpDQ0mDeNFIYiWp': 'file_storage/call_O41YPgIMwwpDQ0mDeNFIYiWp.json', 'var_call_nwCBWIyTNPQah9PPbJJOWmRT': 'file_storage/call_nwCBWIyTNPQah9PPbJJOWmRT.json'}

exec(code, env_args)
