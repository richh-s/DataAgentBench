code = """import json
from pathlib import Path

# file paths from storage
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

# helper for status extraction
def extract_status_from_doc(text, project_base):
    low = text.lower()
    idx = low.find(project_base.lower())
    if idx == -1:
        # try to find near parentheses variations
        idx = 0
    window = text[idx: idx+800]
    wlow = window.lower()
    # look for 'updates:'
    u = wlow.find('updates:')
    if u != -1:
        seg = window[u+8:]
        # cut at 'Project Schedule' or 'Project Schedule:'
        p = seg.lower().find('project schedule')
        if p != -1:
            seg = seg[:p]
        # cut at double newline
        dn = seg.find('\n\n')
        if dn != -1:
            seg = seg[:dn]
        return ' '.join(seg.split())
    # look for common phrases
    phrases = ['under construction','construction was completed','complete construction','complete design','estimated schedule','project is in the preliminary design phase','awaiting final fema','awaiting final fema/caloes approval','awaiting final fema/caloes approval','awaiting final fema/ caloes approval','awaiting final caloes approval']
    for ph in phrases:
        pidx = wlow.find(ph)
        if pidx != -1:
            snippet = window[pidx:pidx+300]
            return ' '.join(snippet.split())
    # fallback: return small window
    return ' '.join(window.strip().split()) or '(status not found)'

combined_text = '\n\n'.join(d.get('text','') for d in civic)
combined_low = combined_text.lower()

results = []
seen_keys = set()

# process funding records
for f in funding:
    pname = f.get('Project_Name','')
    psource = f.get('Funding_Source')
    pamount = f.get('Amount')
    plow = pname.lower()
    base = pname.split('(')[0].strip()
    related = False
    # direct name contains fema or emergency
    if 'fema' in plow or 'emergency' in plow:
        related = True
    # if base appears in civic docs that mention fema/emergency
    if base and base.lower() in combined_low:
        for doc in civic:
            t = doc.get('text','')
            if base.lower() in t.lower():
                if 'fema' in t.lower() or 'emergency' in t.lower() or 'sirens' in t.lower() or 'outdoor warning' in t.lower():
                    related = True
                    status = extract_status_from_doc(t, base)
                    break
    if related:
        # determine status if not set
        status = locals().get('status', None)
        if status is None:
            # try to find in combined text
            status = extract_status_from_doc(combined_text, base)
        key = (pname, psource, pamount)
        if key not in seen_keys:
            results.append({'Project_Name': pname, 'Funding_Source': psource, 'Amount': pamount, 'Status': status})
            seen_keys.add(key)

# find civic-only projects near FEMA/emergency
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
                while j >= 0 and i-j <= 6:
                    if lines[j].strip():
                        candidate = lines[j].strip()
                        break
                    j -= 1
                if candidate:
                    base = candidate.split('(')[0].strip()
                    # skip if in results
                    if any(r['Project_Name'].split('(')[0].strip().lower() == base.lower() for r in results):
                        continue
                    status = extract_status_from_doc(t, base)
                    results.append({'Project_Name': candidate, 'Funding_Source': None, 'Amount': None, 'Status': status})

# sort and deduplicate by project base name
final = []
seen_base = set()
for r in sorted(results, key=lambda x: x['Project_Name'].lower() if x['Project_Name'] else ''):
    base = r['Project_Name'].split('(')[0].strip().lower()
    if base in seen_base:
        continue
    seen_base.add(base)
    # ensure Amount is int or None
    if isinstance(r.get('Amount'), (int,)):
        amt = r['Amount']
    else:
        try:
            amt = int(r['Amount'])
        except Exception:
            amt = None
    final.append({'Project_Name': r.get('Project_Name'), 'Funding_Source': r.get('Funding_Source'), 'Amount': amt, 'Status': r.get('Status')})

import json
print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_O41YPgIMwwpDQ0mDeNFIYiWp': 'file_storage/call_O41YPgIMwwpDQ0mDeNFIYiWp.json', 'var_call_nwCBWIyTNPQah9PPbJJOWmRT': 'file_storage/call_nwCBWIyTNPQah9PPbJJOWmRT.json', 'var_call_aYt4NsGlTLq0WSd9YxToc5f3': {'civic_var': 'file_storage/call_O41YPgIMwwpDQ0mDeNFIYiWp.json', 'funding_var': 'file_storage/call_nwCBWIyTNPQah9PPbJJOWmRT.json'}}

exec(code, env_args)
