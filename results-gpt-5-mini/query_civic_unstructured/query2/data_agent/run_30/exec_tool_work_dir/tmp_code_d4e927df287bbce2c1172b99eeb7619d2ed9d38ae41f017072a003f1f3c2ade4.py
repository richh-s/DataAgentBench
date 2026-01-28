code = """import json
import re

# Load the tool results from storage variables
with open(var_call_n9AZpz1dFRUuqubYzQvaSoqT, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_5Ta0B5Rj8lZjdUtJWzhXyTkF, 'r') as f:
    funding = json.load(f)

# compile patterns
completed_2022_pattern = re.compile(r'completed|complete', re.IGNORECASE)
year_pattern = re.compile(r'2022')
keywords = ['park','playground','walkway','shade','bench','plaza','play','parkway']

found_projects = set()

for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i,line in enumerate(lines):
        if year_pattern.search(line) and completed_2022_pattern.search(line):
            # scan back up to 12 lines to find a project title containing keyword
            for j in range(max(0,i-12), i):
                cand = lines[j].strip()
                # ignore short non-informative lines
                if len(cand) < 3:
                    continue
                # ignore lines that are likely headings
                if re.search(r'^(Updates:|Project Schedule:|Project Description:|Agenda Item|Page \d+ of|Approved by:|Prepared by:|Subject:)', cand, re.IGNORECASE):
                    continue
                # check for keywords
                if any(k in cand.lower() for k in keywords):
                    # clean candidate: remove leading bullet markers and cid stuff
                    cand_clean = re.sub(r"^\(cid:[0-9]+\)\s*", '', cand)
                    cand_clean = cand_clean.strip(' -:')
                    if len(cand_clean) > 0:
                        found_projects.add(cand_clean)
                        break

# Also search for lines that explicitly say 'Construction was completed' adjacent to project titles
# (already handled above)

# Prepare funding match
funding_matches = []
matched_funding_ids = set()

# helper to normalize

def norm(s):
    return re.sub(r'[^a-z0-9]+',' ', s.lower()).strip()

for proj in sorted(found_projects):
    nproj = norm(proj)
    for rec in funding:
        fname = rec.get('Project_Name','')
        nf = norm(fname)
        match = False
        if nproj and nproj in nf:
            match = True
        elif nf and nf in nproj:
            match = True
        else:
            # token overlap
            p_tokens = set([t for t in nproj.split() if len(t)>3])
            f_tokens = set([t for t in nf.split() if len(t)>3])
            if p_tokens & f_tokens:
                match = True
        if match:
            try:
                amount = int(rec.get('Amount') or 0)
            except:
                try:
                    amount = int(float(rec.get('Amount')))
                except:
                    amount = 0
            funding_matches.append({'project_extracted': proj, 'funding_id': rec.get('Funding_ID'), 'funding_name': fname, 'amount': amount})
            matched_funding_ids.add(rec.get('Funding_ID'))

# Sum amounts, avoid duplicate funding ids
total = sum(item['amount'] for item in funding_matches)

# To avoid double counting same funding id multiple times (if matched to multiple projects), deduplicate by funding id
unique_funding = {}
for item in funding_matches:
    fid = item['funding_id']
    if fid not in unique_funding:
        unique_funding[fid] = item

unique_total = sum(v['amount'] for v in unique_funding.values())

result = {
    'extracted_projects_completed_2022': sorted(list(found_projects)),
    'matched_funding_records': list(unique_funding.values()),
    'total_amount_sum_unique_funding_ids': unique_total
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qqvsBQmMn9KBlsyFeW4qV9D0': ['civic_docs'], 'var_call_n9AZpz1dFRUuqubYzQvaSoqT': 'file_storage/call_n9AZpz1dFRUuqubYzQvaSoqT.json', 'var_call_vOINh3VzqNQkq7TY5jjtXxJr': ['Funding'], 'var_call_5Ta0B5Rj8lZjdUtJWzhXyTkF': 'file_storage/call_5Ta0B5Rj8lZjdUtJWzhXyTkF.json'}

exec(code, env_args)
