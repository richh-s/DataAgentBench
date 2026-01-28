code = """import json
import re

# Load files from storage
path_funding = var_call_T8BHlZ9tQf77BgFKlNo1MHHl
path_civic = var_call_N83ujLeP76Yi7NfYvJUwtHH5

with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(path_civic, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Normalize funding amounts to integers
for rec in funding:
    amt = rec.get('Amount', 0)
    try:
        rec['Amount'] = int(amt)
    except Exception:
        s = re.sub('[^0-9]', '', str(amt))
        rec['Amount'] = int(s) if s else 0

# Combine all civic document texts
all_text = '\n'.join(d.get('text', '') for d in civic_docs)
low_text = all_text.lower()

start_marker = 'capital improvement projects (design)'
start = low_text.find(start_marker)
if start != -1:
    # find next markers
    idx1 = low_text.find('capital improvement projects (construction)', start+1)
    idx2 = low_text.find('capital improvement projects (not started)', start+1)
    ends = [i for i in [idx1, idx2] if i != -1]
    end = min(ends) if ends else len(all_text)
    design_section = all_text[start:end]
else:
    parts = re.split('capital improvement projects', all_text, flags=re.IGNORECASE)
    design_section = parts[1] if len(parts) > 1 else all_text

# Heuristic extraction of project-like lines
lines = [ln.strip() for ln in design_section.splitlines()]
keywords = ['project', 'repair', 'improv', 'study', 'walkway', 'park', 'median', 'road', 'drain', 'playground', 'biofilter', 'skate', 'treatment', 'signals', 'warning', 'traffic', 'culvert', 'retaining', 'roof', 'sirens', 'speed', 'curb', 'paver', 'slope', 'storm']
ignore_tokens = ['updates:', 'project schedule', 'complete design', 'advertise', 'begin construction', 'page', 'agenda', 'recommended action', 'discussion', 'item', 'to:', 'prepared by', 'approved by', '(cid:', 'staff', 'estimated schedule']
projects = []
for ln in lines:
    if not ln or len(ln) < 5:
        continue
    low = ln.lower()
    if any(tok in low for tok in ignore_tokens):
        continue
    if any(k in low for k in keywords):
        # cleanup leading bullets or numbers
        ln2 = ln
        while ln2 and ln2[0] in '0123456789-*. )':
            ln2 = ln2[1:].lstrip()
        projects.append(ln2)

# Deduplicate preserving order
seen = set(); design_projects = []
for p in projects:
    key = re.sub('\s+', ' ', p).strip()
    kl = key.lower()
    if kl not in seen:
        seen.add(kl)
        design_projects.append(key)

# Normalization function without regex escapes
import string
keep_chars = string.ascii_lowercase + string.digits + ' '
def normalize(s):
    s2 = s.lower()
    # replace any char not alnum with space
    s3 = []
    for ch in s2:
        if ch in keep_chars:
            s3.append(ch)
        else:
            s3.append(' ')
    s4 = ''.join(s3)
    return ' '.join(s4.split())

funding_filtered = [rec for rec in funding if rec['Amount'] > 50000]
fund_norm = [(rec['Project_Name'], normalize(rec['Project_Name']), rec['Amount']) for rec in funding_filtered]

matched = []
for dp in design_projects:
    dn = normalize(dp)
    found = False
    for fname, fnorm, amt in fund_norm:
        if dn and (dn in fnorm or fnorm in dn):
            matched.append((dp, fname, amt))
            found = True
            break
    if not found:
        dn_tokens = set(dn.split())
        for fname, fnorm, amt in fund_norm:
            fn_tokens = set(fnorm.split())
            if len(dn_tokens & fn_tokens) >= max(1, min(len(dn_tokens), len(fn_tokens))//2):
                matched.append((dp, fname, amt))
                break

unique_design_matched = sorted({m[0] for m in matched})
count = len(unique_design_matched)

output = {'count': count, 'matched_projects': unique_design_matched, 'matches_details': matched}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_rqBzkI0CJk86xb78roGc5I8P': ['civic_docs'], 'var_call_wqKExuccBtopMDlIMCAbedXd': ['Funding'], 'var_call_T8BHlZ9tQf77BgFKlNo1MHHl': 'file_storage/call_T8BHlZ9tQf77BgFKlNo1MHHl.json', 'var_call_N83ujLeP76Yi7NfYvJUwtHH5': 'file_storage/call_N83ujLeP76Yi7NfYvJUwtHH5.json'}

exec(code, env_args)
