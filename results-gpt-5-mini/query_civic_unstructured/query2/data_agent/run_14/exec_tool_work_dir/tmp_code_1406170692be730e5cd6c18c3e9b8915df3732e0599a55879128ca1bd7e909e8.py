code = """import json
import re

# Load the civic docs and funding results from storage file paths
with open(var_call_tgQWC1ymKcQnlyZes7oyE8jr, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_lSfRKQOizb499AMEQrqdr1OT, 'r') as f:
    funding = json.load(f)

# Helper keywords to identify park-related projects
park_keywords = ['park', 'playground', 'walkway', 'bluff', 'bluffs', 'legacy park', 'malibu park']

found_projects = set()

for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        low = line.lower()
        # detect lines that indicate completion in 2022
        if ('completed' in low and '2022' in low) or ('complete construction' in low and '2022' in low) or ('complete construction:' in low and '2022' in low):
            # scan backwards for a plausible project title within previous 8 lines
            title = None
            for back in range(1,9):
                if idx-back < 0:
                    break
                cand = lines[idx-back].strip()
                if not cand:
                    continue
                cand_low = cand.lower()
                # skip lines that are clearly not titles
                if cand_low.startswith('(') or cand_low.startswith('cid:') or 'updates' in cand_low or 'project schedule' in cand_low or 'agenda' in cand_low or 'page' in cand_low:
                    continue
                # also skip lines that look like headings like 'capital improvement projects (construction)'
                if len(cand.split())>10:
                    # too long likely not title
                    continue
                title = cand
                break
            if title:
                # check if title is park-related by keywords
                tl = title.lower()
                if any(k in tl for k in park_keywords):
                    # normalize whitespace
                    found_projects.add(title.strip())

# Also look for explicit 'Construction was completed' with following context where project titles may be on same line or preceding lines with colon
# (handled above mostly)

# Now match found projects to funding table entries
matched = []
total = 0

# Build mapping of funding project names to records
fund_map = {}
for rec in funding:
    pname = rec.get('Project_Name','').strip()
    fund_map.setdefault(pname, []).append(rec)

# For each found project, try exact match, then substring match
for proj in sorted(found_projects):
    matched_recs = []
    # exact match
    if proj in fund_map:
        matched_recs = fund_map[proj]
    else:
        # try case-insensitive match exact
        for pname, recs in fund_map.items():
            if pname.lower() == proj.lower():
                matched_recs = recs
                break
    if not matched_recs:
        # substring matching: funding name contains proj or proj contains funding name
        for pname, recs in fund_map.items():
            if proj.lower() in pname.lower() or pname.lower() in proj.lower():
                matched_recs.extend(recs)
    # dedupe matched_recs by Funding_ID
    unique = {}
    for r in matched_recs:
        unique[r['Funding_ID']] = r
    matched_recs = list(unique.values())
    amount_sum = 0
    recs_out = []
    for r in matched_recs:
        try:
            amt = int(r.get('Amount') or 0)
        except:
            try:
                amt = int(float(r.get('Amount') or 0))
            except:
                amt = 0
        amount_sum += amt
        recs_out.append({'Funding_ID': r.get('Funding_ID'), 'Project_Name': r.get('Project_Name'), 'Amount': amt, 'Funding_Source': r.get('Funding_Source')})
    if matched_recs:
        total += amount_sum
        matched.append({'Detected_Project_Title': proj, 'Matched_Funding_Records': recs_out, 'Project_Funding_Total': amount_sum})

result = {'matched_projects': matched, 'total_funding_for_park_projects_completed_in_2022': total}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_tgQWC1ymKcQnlyZes7oyE8jr': 'file_storage/call_tgQWC1ymKcQnlyZes7oyE8jr.json', 'var_call_lSfRKQOizb499AMEQrqdr1OT': 'file_storage/call_lSfRKQOizb499AMEQrqdr1OT.json'}

exec(code, env_args)
