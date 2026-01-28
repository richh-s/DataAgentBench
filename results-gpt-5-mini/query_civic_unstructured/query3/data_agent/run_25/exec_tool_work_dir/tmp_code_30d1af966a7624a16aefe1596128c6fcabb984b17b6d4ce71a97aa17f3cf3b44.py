code = """import json
import re
from pathlib import Path

# Load tool results from storage variables
with open(var_call_5oztQ1h43QJsRueRDMVuuaAK, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_saeTDqEPUE7OFPW1yq9NfDlk, 'r') as f:
    funding_rows = json.load(f)

# Helper normalize
def normalize_name(s):
    if s is None:
        return ""
    s = s.lower()
    # remove parenthetical content
    s = re.sub(r"\([^)]*\)", "", s)
    # remove punctuation
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Search civic docs for lines mentioning FEMA or emergency or siren
matches = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r"\bfema\b|\bemergency\b|siren|warning", line, re.I):
            # find project name: scan upwards for a plausible title line
            proj_name = None
            for k in range(1,9):
                if i-k < 0:
                    break
                cand = lines[i-k].strip()
                if not cand:
                    continue
                lc = cand.lower()
                # skip obvious non-title lines
                if any(tok in lc for tok in ['updates', 'project schedule', 'project description', 'agenda', 'discussion', 'recommended action', 'date prepared', 'meeting date', 'page']):
                    continue
                # skip lines that look like field labels ending with ':'
                if cand.endswith(':'):
                    continue
                # Accept candidate as project name
                proj_name = cand
                break
            if not proj_name:
                # fallback previous non-empty line
                j = i-1
                while j>=0 and not lines[j].strip():
                    j -= 1
                proj_name = lines[j].strip() if j>=0 else None
            # find status: scan downwards for key phrases
            status = None
            status_lines = []
            for k in range(0,12):
                if i+k >= len(lines):
                    break
                l = lines[i+k].strip()
                if not l:
                    continue
                status_lines.append(l)
                if re.search(r"complete d|completed|construction was completed|complete construction|construction was completed", l, re.I):
                    status = 'completed'
                    break
                if re.search(r"currently under construction|begin construction|begin construction:", l, re.I):
                    status = 'under construction'
                    break
                if re.search(r"design|preliminary design|complete design|final design|finalizing the design|in the preliminary design", l, re.I):
                    status = 'design'
                    break
                if re.search(r"not started|identified but not begun|not begun", l, re.I):
                    status = 'not started'
                    break
                if re.search(r"awaiting.*fema|awaiting final fema|awaiting final fema/caloes|awaiting final fema approval", l, re.I):
                    status = 'awaiting FEMA approval'
                    break
            # if not set, try to infer from nearby lines concatenated
            if not status:
                combined = ' '.join(status_lines)
                if re.search(r"construction", combined, re.I):
                    status = 'under construction'
                elif re.search(r"design", combined, re.I):
                    status = 'design'
                else:
                    status = None
            matches.append({'doc_file': doc.get('filename'), 'project_mention_line': line.strip(), 'project_name_candidate': proj_name, 'status': status})

# Deduplicate by normalized project_name_candidate
unique_projects = {}
for m in matches:
    key = normalize_name(m['project_name_candidate'] or '')
    if not key:
        continue
    if key not in unique_projects:
        unique_projects[key] = {'project_name_candidate': m['project_name_candidate'], 'status': m['status'], 'doc_files': [m['doc_file']], 'mentions': [m['project_mention_line']]}
    else:
        unique_projects[key]['doc_files'].append(m['doc_file'])
        unique_projects[key]['mentions'].append(m['project_mention_line'])
        # prefer non-null status
        if not unique_projects[key]['status'] and m['status']:
            unique_projects[key]['status'] = m['status']

# Load funding rows into list and normalize
funding_list = funding_rows
for fr in funding_list:
    # ensure Amount numeric
    try:
        fr['Amount'] = int(fr.get('Amount') if fr.get('Amount') not in (None, '') else 0)
    except:
        try:
            fr['Amount'] = int(float(fr.get('Amount')))
        except:
            fr['Amount'] = 0
    fr['_norm'] = normalize_name(fr.get('Project_Name',''))

# For each unique civic project, try to match funding entries
results = []
for key, info in unique_projects.items():
    cand_norm = key
    cand_name = info['project_name_candidate']
    status = info['status']
    matched = False
    for fr in funding_list:
        fn = fr['_norm']
        if not fn:
            continue
        # match if normalized strings overlap substantially or one contains the other
        if cand_norm and (cand_norm in fn or fn in cand_norm):
            results.append({'Project_Name': fr.get('Project_Name'), 'Funding_Source': fr.get('Funding_Source'), 'Amount': fr.get('Amount'), 'Status': status})
            matched = True
    # If no exact match found, also check funding rows that explicitly mention FEMA or 'outdoor warning' etc and might relate
    if not matched:
        for fr in funding_list:
            if re.search(r"\bfema\b|outdoor warning|siren|emergency", fr.get('Project_Name',''), re.I):
                # only add if not already present
                already = any(r['Project_Name']==fr.get('Project_Name') and r['Status']==status for r in results)
                if not already:
                    results.append({'Project_Name': fr.get('Project_Name'), 'Funding_Source': fr.get('Funding_Source'), 'Amount': fr.get('Amount'), 'Status': status})

# Also include funding entries that explicitly mention FEMA even if not found in civic docs; try to find status by searching civic docs texts for their project names
for fr in funding_list:
    if re.search(r"\bfema\b", fr.get('Project_Name',''), re.I):
        # check if already in results
        if any(r['Project_Name']==fr.get('Project_Name') for r in results):
            continue
        # try to find status by searching civic docs text for the funding project name (normalized)
        fnorm = fr['_norm']
        found_status = None
        for doc in civic_docs:
            if re.search(re.escape(fnorm), normalize_name(doc.get('text',''))):
                # crude: get nearby phrase
                found_status = 'mentioned in civic documents'
                break
        results.append({'Project_Name': fr.get('Project_Name'), 'Funding_Source': fr.get('Funding_Source'), 'Amount': fr.get('Amount'), 'Status': found_status})

# Deduplicate final results by project name and funding source and amount
final = []
seen = set()
for r in results:
    key = (r.get('Project_Name'), r.get('Funding_Source'), r.get('Amount'), r.get('Status'))
    if key in seen:
        continue
    seen.add(key)
    final.append(r)

import json
print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_5oztQ1h43QJsRueRDMVuuaAK': 'file_storage/call_5oztQ1h43QJsRueRDMVuuaAK.json', 'var_call_saeTDqEPUE7OFPW1yq9NfDlk': 'file_storage/call_saeTDqEPUE7OFPW1yq9NfDlk.json'}

exec(code, env_args)
