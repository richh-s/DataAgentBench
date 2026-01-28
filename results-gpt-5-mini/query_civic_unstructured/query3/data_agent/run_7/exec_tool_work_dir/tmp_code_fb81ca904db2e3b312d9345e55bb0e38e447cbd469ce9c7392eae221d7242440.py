code = """import json
from pathlib import Path

civic_path = Path(var_call_O41YPgIMwwpDQ0mDeNFIYiWp)
funding_path = Path(var_call_nwCBWIyTNPQah9PPbJJOWmRT)

civic = json.loads(civic_path.read_text())
funding = json.loads(funding_path.read_text())

combined = '\n\n'.join(d.get('text','') for d in civic)
combined_low = combined.lower()

def get_base(name):
    return name.split('(')[0].strip()

def extract_status(text, base):
    low = text.lower()
    idx = low.find(base.lower())
    if idx == -1:
        idx = 0
    window = text[idx: idx+800]
    wlow = window.lower()
    u = wlow.find('updates:')
    if u != -1:
        seg = window[u+8:]
        p = seg.lower().find('project schedule')
        if p != -1:
            seg = seg[:p]
        dn = seg.find('\n\n')
        if dn != -1:
            seg = seg[:dn]
        return ' '.join(seg.split())
    # look for keywords
    for kw in ['under construction','construction was completed','complete construction','complete design','project is in the preliminary design phase','awaiting final fema']:
        kidx = wlow.find(kw)
        if kidx != -1:
            return '...'+window[kidx:kidx+200].strip().replace('\n',' ')
    return '(status not found)'

results = []
seen = set()

# Check funding records
for f in funding:
    pname = f.get('Project_Name','')
    psource = f.get('Funding_Source')
    try:
        pamount = int(f.get('Amount'))
    except Exception:
        pamount = None
    base = get_base(pname)
    rel = False
    pl = pname.lower()
    if 'fema' in pl or 'emergency' in pl:
        rel = True
    if base and base.lower() in combined_low:
        for doc in civic:
            t = doc.get('text','')
            if base.lower() in t.lower():
                if 'fema' in t.lower() or 'emergency' in t.lower() or 'sirens' in t.lower() or 'outdoor warning' in t.lower():
                    rel = True
                    status = extract_status(t, base)
                    break
    if rel:
        if 'status' not in locals():
            status = extract_status(combined, base)
        key = (base.lower(), psource, pamount)
        if key not in seen:
            results.append({'Project_Name': pname, 'Funding_Source': psource, 'Amount': pamount, 'Status': status})
            seen.add(key)
        if 'status' in locals():
            del status

# Find civic-only projects near FEMA/emergency
for doc in civic:
    t = doc.get('text','')
    low = t.lower()
    if 'fema' in low or 'emergency' in low:
        lines = t.split('\n')
        for i,line in enumerate(lines):
            if 'updates:' in line.lower():
                j = i-1
                candidate = None
                while j>=0 and i-j<=6:
                    if lines[j].strip():
                        candidate = lines[j].strip()
                        break
                    j -= 1
                if candidate:
                    base = get_base(candidate)
                    if any(r['Project_Name'].split('(')[0].strip().lower()==base.lower() for r in results):
                        continue
                    status = extract_status(t, base)
                    results.append({'Project_Name': candidate, 'Funding_Source': None, 'Amount': None, 'Status': status})

# dedupe by base
final = []
seenb = set()
for r in results:
    b = get_base(r['Project_Name']).lower()
    if b in seenb:
        continue
    seenb.add(b)
    final.append({'Project_Name': r['Project_Name'], 'Funding_Source': r.get('Funding_Source'), 'Amount': r.get('Amount'), 'Status': r.get('Status')})

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_O41YPgIMwwpDQ0mDeNFIYiWp': 'file_storage/call_O41YPgIMwwpDQ0mDeNFIYiWp.json', 'var_call_nwCBWIyTNPQah9PPbJJOWmRT': 'file_storage/call_nwCBWIyTNPQah9PPbJJOWmRT.json', 'var_call_aYt4NsGlTLq0WSd9YxToc5f3': {'civic_var': 'file_storage/call_O41YPgIMwwpDQ0mDeNFIYiWp.json', 'funding_var': 'file_storage/call_nwCBWIyTNPQah9PPbJJOWmRT.json'}}

exec(code, env_args)
