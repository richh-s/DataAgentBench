code = """import json
import re

# Load files
path_funding = var_call_T8BHlZ9tQf77BgFKlNo1MHHl
path_civic = var_call_N83ujLeP76Yi7NfYvJUwtHH5

with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(path_civic, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Normalize funding amounts
for rec in funding:
    try:
        rec['Amount'] = int(rec['Amount'])
    except:
        s = re.sub(r"[^0-9]", "", str(rec.get('Amount','0')))
        rec['Amount'] = int(s) if s else 0

# Combine civic texts
all_text = "\n".join(d.get('text','') for d in civic_docs)

# Extract Design section
m = re.search(r"Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|$)", all_text, flags=re.S|re.I)
if m:
    design_section = m.group(1)
else:
    design_section = all_text

# Heuristically extract project titles: lines that look like titles (start of line, capitalized)
lines = [ln.strip() for ln in design_section.splitlines()]
projects = []
for ln in lines:
    if not ln:
        continue
    low = ln.lower()
    if any(x in low for x in ['updates:', 'project schedule', 'complete design', 'advertise', 'begin construction', 'page', 'agenda', 'recommended action', 'discussion', 'item', 'to:', 'prepared by', 'approved by']):
        continue
    # If line contains 'project' or 'project:' or 'repair' or 'improvements' or 'study' or 'walkway' or 'park' or 'traffic' or 'median' etc, consider it
    if re.search(r"\b(project|repair|improv|study|walkway|park|median|road|drain|walkway|playground|biofilter|skate|treatment|signals|warning|traffic)\b", low):
        # Remove leading bullets/markers
        ln2 = re.sub(r"^[\-\u2022\*\d\.\)\s]+", "", ln)
        projects.append(ln2)

# Deduplicate
seen = set(); design_projects = []
for p in projects:
    key = p.strip()
    kl = re.sub(r"\s+"," ", key).lower()
    if kl not in seen:
        seen.add(kl)
        design_projects.append(key)

# Normalization function for matching
def normalize(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]"," ", s)
    s = re.sub(r"\s+"," ", s).strip()
    return s

funding_filtered = [rec for rec in funding if rec['Amount'] > 50000]
fund_norm = [(rec['Project_Name'], normalize(rec['Project_Name']), rec['Amount']) for rec in funding_filtered]

matched = []
for dp in design_projects:
    dn = normalize(dp)
    for fname, fnorm, amt in fund_norm:
        if dn and (dn in fnorm or fnorm in dn):
            matched.append((dp, fname, amt))
            break

# Token overlap matching for unmatched
for dp in design_projects:
    if any(m[0]==dp for m in matched):
        continue
    dn_tokens = set(normalize(dp).split())
    for fname, fnorm, amt in fund_norm:
        fn_tokens = set(fnorm.split())
        if len(dn_tokens & fn_tokens) >= max(1, min(len(dn_tokens), len(fn_tokens))//2):
            matched.append((dp, fname, amt))
            break

unique_design_matched = sorted({m[0] for m in matched})
count = len(unique_design_matched)

output = {'count': count, 'matched_projects': unique_design_matched, 'matches_details': matched}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_rqBzkI0CJk86xb78roGc5I8P': ['civic_docs'], 'var_call_wqKExuccBtopMDlIMCAbedXd': ['Funding'], 'var_call_T8BHlZ9tQf77BgFKlNo1MHHl': 'file_storage/call_T8BHlZ9tQf77BgFKlNo1MHHl.json', 'var_call_N83ujLeP76Yi7NfYvJUwtHH5': 'file_storage/call_N83ujLeP76Yi7NfYvJUwtHH5.json'}

exec(code, env_args)
