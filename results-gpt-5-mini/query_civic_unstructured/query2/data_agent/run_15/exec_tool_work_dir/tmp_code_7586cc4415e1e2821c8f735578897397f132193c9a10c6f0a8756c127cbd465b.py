code = """import json, re
# Load data from storage files
with open(var_call_0fUjBApHRNYQRbT9gTd4fnWS, 'r') as f:
    funding = json.load(f)
with open(var_call_agSZO2Qc3Ku1gCpY4STNohpM, 'r') as f:
    docs = json.load(f)

# Normalize funding amounts to int
for rec in funding:
    amt = rec.get('Amount')
    try:
        rec['Amount'] = int(amt)
    except Exception:
        s = re.sub(r"[^0-9]", "", str(amt or ''))
        rec['Amount'] = int(s) if s else 0

park_keywords = ['park', 'playground', 'walkway', 'benches', 'benches and', 'bench', 'trail', 'plaza', 'shade structure']

matches = []
matched_fids = set()

# Function to check proximity: whether all keywords appear within a window of characters
def prox_check(text, keywords, window=1000):
    low = text.lower()
    return all(k in low for k in keywords)

# First pass: for each funding record that looks park-related by name, search docs for name + completed + 2022
for rec in funding:
    pname = rec.get('Project_Name','')
    if not pname:
        continue
    pname_low = pname.lower()
    # check if funding project name itself suggests park
    name_is_park = any(k in pname_low for k in park_keywords)
    if not name_is_park:
        continue
    # search docs for mention
    for doc in docs:
        text = doc.get('text','')
        text_low = text.lower()
        if pname_low in text_low:
            # find index
            idx = text_low.find(pname_low)
            window_start = max(0, idx-500)
            window_end = min(len(text), idx+1500)
            window = text[window_start:window_end].lower()
            if ('completed' in window or 'construction was completed' in window) and '2022' in window:
                fid = rec.get('Funding_ID')
                if fid not in matched_fids:
                    matches.append({'Funding_ID': fid, 'Project_Name': rec.get('Project_Name'), 'Amount': rec.get('Amount'), 'filename': doc.get('filename')})
                    matched_fids.add(fid)
                break

# Second pass: search docs for any lines indicating a park project was completed in 2022, then match funding names containing that project phrase
candidate_project_phrases = set()
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    # iterate lines to find those that contain 'completed' and '2022' on same or nearby lines
    for i, line in enumerate(lines):
        line_low = line.lower()
        if 'completed' in line_low and '2022' in line_low:
            # look back up to 5 previous non-empty lines for a project title or name
            j = i-1
            collected = []
            while j >= 0 and len(collected) < 6:
                l = lines[j].strip()
                if l:
                    collected.append(l)
                j -= 1
            # take the nearest prior non-empty line as candidate
            if collected:
                cand = collected[0]
                cand_low = cand.lower()
                if any(k in cand_low for k in park_keywords):
                    candidate_project_phrases.add(cand)
            # also scan nearby lines within window for park keywords and possible project names
            window_lines = '\n'.join(lines[max(0,i-6):i+3])
            for ln in re.split(r'\n', window_lines):
                if len(ln.strip())>0 and any(k in ln.lower() for k in park_keywords):
                    # heuristics: take the longest short line as phrase
                    phrase = ln.strip()
                    if len(phrase) < 200:
                        candidate_project_phrases.add(phrase)

# Match candidate phrases to funding records by substring
for cand in candidate_project_phrases:
    cand_low = cand.lower()
    for rec in funding:
        pname_low = rec.get('Project_Name','').lower()
        if cand_low in pname_low or pname_low in cand_low:
            fid = rec.get('Funding_ID')
            if fid not in matched_fids:
                matches.append({'Funding_ID': fid, 'Project_Name': rec.get('Project_Name'), 'Amount': rec.get('Amount'), 'matched_doc_phrase': cand})
                matched_fids.add(fid)

# Compute total
total = sum(m['Amount'] for m in matches)

out = {'total_funding': total, 'matching_projects': matches}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0fUjBApHRNYQRbT9gTd4fnWS': 'file_storage/call_0fUjBApHRNYQRbT9gTd4fnWS.json', 'var_call_agSZO2Qc3Ku1gCpY4STNohpM': 'file_storage/call_agSZO2Qc3Ku1gCpY4STNohpM.json'}

exec(code, env_args)
