code = """import json, re

# Load data from storage-provided file paths
with open(var_call_c1qEeIcfYV2j9XXcklUAC7jg, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_FH2VjWuOAAWVTxL5LBeROsyI, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Helper to normalize strings
def norm(s):
    return re.sub(r"\s+", " ", s.strip()).strip() if s else s

projects = {}
keyword_re = re.compile(r"\b(FEMA|emergency)\b", re.I)

for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if keyword_re.search(line):
            # find candidate title in previous non-empty lines
            title = None
            for j in range(i-1, max(i-20, -1), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                # skip lines that seem like headers or page footers
                if cand.lower().startswith('page') or cand.lower().startswith('agenda'):
                    continue
                if len(cand) > 200:
                    continue
                # skip lines that are just labels like 'Updates:'
                if re.match(r'^(updates:|project schedule:|recommended action:|discussion:)', cand.lower()):
                    continue
                # accept this as title
                title = norm(cand)
                break
            if not title:
                # fallback: take a few words from the line with keyword
                title = norm(line)
            # store minimal info
            if title not in projects:
                projects[title] = {'Project_Name': title, 'Matches': [], 'Status': None}
            projects[title]['Matches'].append({'doc_filename': doc.get('filename'), 'line_with_keyword': norm(line)})
            # attempt to extract status from following lines
            status = None
            for k in range(i, min(i+25, len(lines))):
                l = lines[k].strip()
                low = l.lower()
                if 'under construction' in low or 'begin construction' in low or 'construction was' in low:
                    status = 'under construction'
                    break
                if 'complete construction' in low or 'construction was completed' in low or 'notice of completion' in low:
                    status = 'completed'
                    break
                if 'design' in low or 'preliminary design' in low or 'final design' in low or 'complete design' in low:
                    status = 'design'
                    break
                if 'not started' in low or 'not yet' in low:
                    status = 'not started'
                    break
                # other heuristics
                if 'project is currently under construction' in low:
                    status = 'under construction'
                    break
            # if already have a status keep the more definitive one (completed > under construction > design > not started)
            priority = {'completed':4, 'under construction':3, 'design':2, 'not started':1, None:0}
            if status:
                cur = projects[title].get('Status')
                if priority.get(status,0) > priority.get(cur,0):
                    projects[title]['Status'] = status

# Prepare funding matching: try case-insensitive containment matches
fund_matches = {p: [] for p in projects}
for f in funding:
    fname = f.get('Project_Name','')
    for p in projects:
        # both normalized and lowered
        pl = p.lower()
        fl = fname.lower()
        if pl in fl or fl in pl or 'fema' in fl or 'emergency' in fl:
            fund_matches[p].append({'Funding_Source': f.get('Funding_Source'), 'Amount': int(f.get('Amount')) if f.get('Amount') and str(f.get('Amount')).isdigit() else f.get('Amount'), 'Funding_Project_Name': fname})

# Build results: include only projects that are related to FEMA or emergency (we already filtered)
results = []
for p, meta in projects.items():
    entry = {
        'Project_Name': meta['Project_Name'],
        'Status': meta['Status'] if meta['Status'] else None,
        'Funding': fund_matches.get(p) if fund_matches.get(p) else []
    }
    # If no funding matches but the matched lines mention FEMA or emergency, try to also add funding records that explicitly contain 'fema' or 'emergency'
    if not entry['Funding']:
        for f in funding:
            if 'fema' in f.get('Project_Name','').lower() or 'fema' in (f.get('Funding_Source') or '').lower() or 'emergency' in f.get('Project_Name','').lower() or 'emergency' in (f.get('Funding_Source') or '').lower():
                # include as possible related funding
                entry['Funding'].append({'Funding_Source': f.get('Funding_Source'), 'Amount': int(f.get('Amount')) if f.get('Amount') and str(f.get('Amount')).isdigit() else f.get('Amount'), 'Funding_Project_Name': f.get('Project_Name')})
    results.append(entry)

# Flatten results: one record per funding entry (or one with null funding if none)
flat = []
for r in results:
    if r['Funding']:
        for f in r['Funding']:
            flat.append({'Project_Name': r['Project_Name'], 'Funding_Source': f['Funding_Source'], 'Amount': f['Amount'], 'Status': r['Status']})
    else:
        flat.append({'Project_Name': r['Project_Name'], 'Funding_Source': None, 'Amount': None, 'Status': r['Status']})

# Deduplicate by tuple
seen = set()
final = []
for item in flat:
    key = (item['Project_Name'], str(item['Funding_Source']), str(item['Amount']), str(item['Status']))
    if key in seen:
        continue
    seen.add(key)
    final.append(item)

import json
print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_c1qEeIcfYV2j9XXcklUAC7jg': 'file_storage/call_c1qEeIcfYV2j9XXcklUAC7jg.json', 'var_call_FH2VjWuOAAWVTxL5LBeROsyI': 'file_storage/call_FH2VjWuOAAWVTxL5LBeROsyI.json'}

exec(code, env_args)
