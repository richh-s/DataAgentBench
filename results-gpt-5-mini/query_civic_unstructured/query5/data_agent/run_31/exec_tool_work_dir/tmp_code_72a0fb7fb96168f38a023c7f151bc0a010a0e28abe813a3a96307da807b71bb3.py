code = """import json
import re

# Load data from provided storage file paths
civic_docs_path = var_call_u2rbXVXNdDlHVrOYeNDHqgLC
funding_path = var_call_yaXynPJfCQUvxCixdzIq96mD

with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding amounts and ensure types
for r in funding:
    amt = r.get('Amount')
    try:
        r['Amount'] = int(amt) if isinstance(amt, int) else int(str(amt))
    except:
        s = ''.join(ch for ch in str(amt) if ch.isdigit())
        r['Amount'] = int(s) if s else 0

# Keywords indicating disaster-related projects
disaster_kws = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'flood', 'flooding', 'emergency']

def contains_kw(s, kws):
    s = (s or '').lower()
    return any(kw in s for kw in kws)

matches = []

# Pre-concatenate all civic text for faster search
all_texts = []
for d in civic_docs:
    txt = d.get('text', '') or ''
    all_texts.append(txt.lower())

all_text = "\n".join(all_texts)

for row in funding:
    pname = row.get('Project_Name', '') or ''
    pname_l = pname.lower()
    base = re.sub(r"\s*\(.*?\)", "", pname).strip()
    base_l = base.lower()

    disaster_flag = False
    started_2022_flag = False
    matched_in_doc = False

    # If project name itself contains disaster keywords, mark disaster
    if contains_kw(pname_l, disaster_kws):
        disaster_flag = True

    # Search for base name or full name in civic docs
    if base_l and base_l in all_text:
        matched_in_doc = True
        start = 0
        while True:
            idx = all_text.find(base_l, start)
            if idx == -1:
                break
            wstart = max(0, idx-300)
            wend = min(len(all_text), idx + len(base_l) + 300)
            window = all_text[wstart:wend]
            if contains_kw(window, disaster_kws):
                disaster_flag = True
            if '2022' in window:
                started_2022_flag = True
            start = idx + 1

    # Also check for explicit '2022' in project name
    if '2022' in pname_l:
        started_2022_flag = True

    # As an additional heuristic, if funding source mentions FEMA or Federal Assistance
    fs = (row.get('Funding_Source') or '').lower()
    if contains_kw(fs, disaster_kws):
        disaster_flag = True

    # If we detected disaster and started_2022, include
    if disaster_flag and started_2022_flag:
        fid = row.get('Funding_ID')
        try:
            fid_val = int(fid)
        except:
            fid_val = fid
        matches.append({
            'Funding_ID': fid_val,
            'Project_Name': row.get('Project_Name'),
            'Funding_Source': row.get('Funding_Source'),
            'Amount': row.get('Amount'),
            'disaster_detected': disaster_flag,
            'started_2022_detected': started_2022_flag,
            'matched_in_doc': matched_in_doc
        })

# Sum total
total = sum(m['Amount'] for m in matches)

output = {
    'total_funding': total,
    'matching_projects_count': len(matches),
    'matching_projects': matches
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_vS9gy0vFh4LI5uPIdDoV2wTB': [], 'var_call_rwY2Dv1fsAs8eBL1BI0D9WQf': ['civic_docs'], 'var_call_u2rbXVXNdDlHVrOYeNDHqgLC': 'file_storage/call_u2rbXVXNdDlHVrOYeNDHqgLC.json', 'var_call_yaXynPJfCQUvxCixdzIq96mD': 'file_storage/call_yaXynPJfCQUvxCixdzIq96mD.json'}

exec(code, env_args)
