code = """import json
import re

# Load the tool results from storage variables
path_funding = var_call_T8BHlZ9tQf77BgFKlNo1MHHl
path_civic = var_call_N83ujLeP76Yi7NfYvJUwtHH5

with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)

with open(path_civic, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Normalize funding entries and filter amounts > 50000 (they should already be filtered)
for rec in funding:
    # Ensure Amount is numeric
    try:
        rec['Amount'] = int(rec['Amount'])
    except:
        # remove non-digits
        s = re.sub(r"[^0-9]", "", str(rec.get('Amount', '0')))
        rec['Amount'] = int(s) if s else 0

# Combine all civic texts
all_text = "\n".join(d.get('text','') for d in civic_docs)

# Find the 'Capital Improvement Projects (Design)' section
m = re.search(r'Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Capital Improvement Projects \(Construction\)|$)', all_text, flags=re.S|re.I)
if m:
    design_section = m.group(1)
else:
    # fallback: find between header and next major header 'Capital Improvement Projects' occurrences
    parts = re.split(r'Capital Improvement Projects', all_text, flags=re.I)
    design_section = parts[1] if len(parts) > 1 else all_text

# Split into lines and pick candidate project name lines
lines = [ln.strip() for ln in design_section.splitlines()]
# Filter out empty and lines that are clearly not project names
candidates = []
for ln in lines:
    if not ln:
        continue
    low = ln.lower()
    # skip lines that are narrative or markers
    if any(x in low for x in ['updates:', 'project schedule', 'page', 'agenda', 'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject:', 'recommended action', '(cid:', 'item', 'discussion', 'public works', 'meeting']):
        continue
    # Skip lines that are short like single words unlikely to be project names
    if len(ln) < 5:
        continue
    # Skip lines that are headers like 'Capital Improvement Projects (Design)'
    if 'capital improvement' in low:
        continue
    # If line ends with 'Project' or contains common keywords, keep
    candidates.append(ln)

# Deduplicate while preserving order
seen = set()
design_projects = []
for c in candidates:
    key = re.sub(r"\s+", " ", c).strip()
    if key.lower() not in seen:
        seen.add(key.lower())
        design_projects.append(key)

# Normalize function
def normalize(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

funding_names = [rec['Project_Name'] for rec in funding]
funding_norm = [(rec['Project_Name'], normalize(rec['Project_Name'])) for rec in funding]

matched = []
for dp in design_projects:
    dn = normalize(dp)
    for fname, fnorm in funding_norm:
        if dn and (dn in fnorm or fnorm in dn):
            # ensure amount > 50000
            # find the record(s)
            for rec in funding:
                if rec['Project_Name'] == fname and rec['Amount'] > 50000:
                    matched.append((dp, fname, rec['Amount']))
            break

# Additionally, try matching by token overlap for any design project not matched
for dp in design_projects:
    if any(m[0]==dp for m in matched):
        continue
    dn = set(normalize(dp).split())
    for rec in funding:
        fn = set(normalize(rec['Project_Name']).split())
        # consider match if more than half of tokens in design appear in funding name or vice versa
        if len(dn & fn) >= max(1, min(len(dn), len(fn))//2):
            if rec['Amount'] > 50000:
                matched.append((dp, rec['Project_Name'], rec['Amount']))
                break

# Get unique design project names that have funding > 50k
unique_design_matched = sorted({m[0] for m in matched})
count = len(unique_design_matched)

output = {'count': count, 'matched_projects': unique_design_matched, 'matches_details': matched}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_rqBzkI0CJk86xb78roGc5I8P': ['civic_docs'], 'var_call_wqKExuccBtopMDlIMCAbedXd': ['Funding'], 'var_call_T8BHlZ9tQf77BgFKlNo1MHHl': 'file_storage/call_T8BHlZ9tQf77BgFKlNo1MHHl.json', 'var_call_N83ujLeP76Yi7NfYvJUwtHH5': 'file_storage/call_N83ujLeP76Yi7NfYvJUwtHH5.json'}

exec(code, env_args)
