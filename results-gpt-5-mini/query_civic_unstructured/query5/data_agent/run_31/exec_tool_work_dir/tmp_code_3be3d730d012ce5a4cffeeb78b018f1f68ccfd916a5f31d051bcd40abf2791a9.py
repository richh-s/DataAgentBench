code = """import json

# Load data from provided storage file paths
civic_docs_path = var_call_u2rbXVXNdDlHVrOYeNDHqgLC
funding_path = var_call_yaXynPJfCQUvxCixdzIq96mD

with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding amounts
for r in funding:
    amt = r.get('Amount')
    try:
        if isinstance(amt, int):
            r['Amount'] = amt
        else:
            r['Amount'] = int(str(amt))
    except Exception:
        digits = ''.join(ch for ch in str(amt) if ch.isdigit())
        r['Amount'] = int(digits) if digits else 0

# disaster keywords
kws = ['fema','caloes','caljpia','disaster','fire','woolsey','flood','flooding','emergency']

def has_kw(s):
    if not s:
        return False
    sl = s.lower()
    for k in kws:
        if k in sl:
            return True
    return False

# concat civic texts using chr(10) to avoid escape issues
all_text = chr(10).join(((d.get('text') or '').lower()) for d in civic_docs)

matches = []
for row in funding:
    pname = row.get('Project_Name') or ''
    pname_l = pname.lower()
    base = pname.split('(')[0].strip().lower()

    disaster_flag = False
    started_2022_flag = False
    matched_in_doc = False

    if has_kw(pname):
        disaster_flag = True
    if '2022' in pname_l:
        started_2022_flag = True

    if base and base in all_text:
        matched_in_doc = True
        start = 0
        while True:
            idx = all_text.find(base, start)
            if idx == -1:
                break
            wstart = idx-300
            if wstart < 0:
                wstart = 0
            wend = idx + len(base) + 300
            if wend > len(all_text):
                wend = len(all_text)
            window = all_text[wstart:wend]
            if has_kw(window):
                disaster_flag = True
            if '2022' in window:
                started_2022_flag = True
            start = idx + 1

    fs = row.get('Funding_Source') or ''
    if has_kw(fs):
        disaster_flag = True

    if disaster_flag and started_2022_flag:
        fid = row.get('Funding_ID')
        try:
            fid_val = int(fid)
        except Exception:
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

total = 0
for m in matches:
    try:
        total += int(m.get('Amount') or 0)
    except:
        pass

out = {'total_funding': total, 'matching_projects_count': len(matches), 'matching_projects': matches}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_vS9gy0vFh4LI5uPIdDoV2wTB': [], 'var_call_rwY2Dv1fsAs8eBL1BI0D9WQf': ['civic_docs'], 'var_call_u2rbXVXNdDlHVrOYeNDHqgLC': 'file_storage/call_u2rbXVXNdDlHVrOYeNDHqgLC.json', 'var_call_yaXynPJfCQUvxCixdzIq96mD': 'file_storage/call_yaXynPJfCQUvxCixdzIq96mD.json'}

exec(code, env_args)
