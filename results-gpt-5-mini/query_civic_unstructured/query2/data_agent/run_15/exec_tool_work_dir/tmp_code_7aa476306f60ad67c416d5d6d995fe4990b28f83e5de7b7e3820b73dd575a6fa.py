code = """import json, re
# Load data from storage files
with open(var_call_0fUjBApHRNYQRbT9gTd4fnWS, 'r') as f:
    funding = json.load(f)
with open(var_call_agSZO2Qc3Ku1gCpY4STNohpM, 'r') as f:
    docs = json.load(f)

# Normalize Amount to int
for r in funding:
    a = r.get('Amount')
    try:
        r['Amount'] = int(a)
    except Exception:
        s = re.sub('[^0-9]', '', str(a or ''))
        r['Amount'] = int(s) if s else 0

park_keywords = ['park', 'playground', 'walkway', 'benches', 'bench', 'trail', 'shade structure', 'plaza']

matches = []
seen_ids = set()

# Helper: check if doc likely indicates completion in 2022 near a project name
def doc_mentions_completed_2022(doc_text, proj_name):
    t = doc_text.lower()
    pn = proj_name.lower()
    if pn in t:
        # find index
        idx = t.find(pn)
        start = max(0, idx-500)
        end = min(len(t), idx+1500)
        window = t[start:end]
        if 'completed' in window and '2022' in window:
            return True
    return False

# First, find funding records whose name suggests park-related
for r in funding:
    pname = r.get('Project_Name','')
    if not pname:
        continue
    if any(k in pname.lower() for k in park_keywords):
        # look for mention in docs indicating completed in 2022
        for d in docs:
            if doc_mentions_completed_2022(d.get('text',''), pname):
                fid = r.get('Funding_ID')
                if fid not in seen_ids:
                    matches.append({'Funding_ID': fid, 'Project_Name': pname, 'Amount': r.get('Amount'), 'filename': d.get('filename')})
                    seen_ids.add(fid)
                break

# Also, find projects mentioned in docs as completed in 2022 that include park keywords, then match funding by substring
proj_phrases = set()
for d in docs:
    t = d.get('text','')
    low = t.lower()
    if 'completed' in low and '2022' in low:
        # grab lines
        lines = t.splitlines()
        for i, line in enumerate(lines):
            if 'completed' in line.lower() and '2022' in line.lower():
                # look back up to 6 lines for candidate name
                j = i-1
                while j >= 0 and j >= i-6:
                    ln = lines[j].strip()
                    if ln:
                        if any(k in ln.lower() for k in park_keywords):
                            proj_phrases.add(ln)
                            break
                    j -= 1

for phrase in proj_phrases:
    plow = phrase.lower()
    for r in funding:
        pname = r.get('Project_Name','')
        if plow in pname.lower() or pname.lower() in plow:
            fid = r.get('Funding_ID')
            if fid not in seen_ids:
                matches.append({'Funding_ID': fid, 'Project_Name': pname, 'Amount': r.get('Amount'), 'matched_phrase': phrase})
                seen_ids.add(fid)

# Sum amounts
total = sum(m['Amount'] for m in matches)

out = {'total_funding': total, 'matching_projects': matches}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0fUjBApHRNYQRbT9gTd4fnWS': 'file_storage/call_0fUjBApHRNYQRbT9gTd4fnWS.json', 'var_call_agSZO2Qc3Ku1gCpY4STNohpM': 'file_storage/call_agSZO2Qc3Ku1gCpY4STNohpM.json'}

exec(code, env_args)
