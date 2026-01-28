code = """import json, re

# Load data from storage-provided file paths
with open(var_call_Rzijr1ISlDUOM9pATv8LIjjx, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_Ux2JQYUAZi3uGCxmtmShczUi, 'r') as f:
    funding_records = json.load(f)

# Helper normalize function
def normalize(name):
    if name is None:
        return ''
    s = name.lower()
    # remove parenthetical content
    s = re.sub(r"\([^)]*\)", "", s)
    # remove non-alphanumeric except spaces
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Disaster keywords
disaster_kw = ['disaster', 'fema', 'caloes', 'caljpia', 'fire', 'woolsey', 'disaster recovery', 'fema/']

candidates = set()

for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i,line in enumerate(lines):
        L = line.strip()
        if not L:
            continue
        # Heuristic: line likely a project name if contains Project or Repair(s) or Improvements or Road/Bridge and not too long
        if (('project' in L.lower() or 'repair' in L.lower() or 'improvements' in L.lower() or 'repairs' in L.lower())
            and len(L) < 200):
            # exclude lines that are clearly headings like 'Updates:' or 'Project Schedule:'
            low = L.lower()
            if any(ex in low for ex in ['updates:', 'project schedule', 'project description', 'project updates', 'agenda item']):
                continue
            # Grab context
            start = max(0, i-6)
            end = min(len(lines), i+7)
            context = '\n'.join(lines[start:end]).lower()
            # Check for year 2022 in context
            if '2022' in context:
                # Check for disaster keywords in context
                if any(kw in context for kw in disaster_kw):
                    # Clean candidate name
                    name = re.sub(r"^[^a-zA-Z0-9]*", "", L)
                    name = name.strip(':- \t')
                    candidates.add(name)

# As a fallback, also look for project names that include '(FEMA' etc anywhere in funding list and check civic docs contain 2022
# But we'll proceed with candidates found

# Normalize funding records
for r in funding_records:
    # ensure Amount is int
    try:
        r['Amount'] = int(r.get('Amount',0))
    except:
        # remove commas
        r['Amount'] = int(re.sub(r'[^0-9]', '', str(r.get('Amount','0'))))

# Build mapping of normalized funding names to records
fund_by_norm = {}
for r in funding_records:
    norm = normalize(r.get('Project_Name',''))
    fund_by_norm.setdefault(norm, []).append(r)

# Match candidates to funding
matched = []
matched_funding_total = 0
matched_details = []

for c in sorted(candidates):
    n = normalize(c)
    found = False
    # exact match
    if n in fund_by_norm:
        for rec in fund_by_norm[n]:
            matched_funding_total += rec['Amount']
            matched_details.append({'extracted_project': c, 'fund_project_name': rec['Project_Name'], 'amount': rec['Amount']})
            found = True
    else:
        # try substring matches
        for fnorm, recs in fund_by_norm.items():
            if n and (n in fnorm or fnorm in n):
                for rec in recs:
                    matched_funding_total += rec['Amount']
                    matched_details.append({'extracted_project': c, 'fund_project_name': rec['Project_Name'], 'amount': rec['Amount']})
                    found = True
        # also try matching by words
    # if not found, continue

# As an additional step, there may be disaster projects in funding with '(FEMA' etc and civic docs mention 2022 generally
# So look for funding records whose project name contains fema/caloes/caljpia and check if civic docs text contains that project name and 2022
for r in funding_records:
    pname = r.get('Project_Name','')
    lowp = pname.lower()
    if any(x in lowp for x in ['fema','caloes','caljpia']):
        # check if project name (without parenthetical) appears in any civic doc text with 2022
        pnorm = normalize(pname)
        appears_in_2022 = False
        for doc in civic_docs:
            if '2022' in doc.get('text',''):
                if pnorm and pnorm in normalize(doc.get('text','')):
                    appears_in_2022 = True
                    break
        if appears_in_2022:
            # avoid double counting if already matched by earlier logic
            already = any(d['fund_project_name']==pname and d['amount']==r['Amount'] for d in matched_details)
            if not already:
                matched_funding_total += r['Amount']
                matched_details.append({'extracted_project': None, 'fund_project_name': r['Project_Name'], 'amount': r['Amount']})

# Prepare output
output = {
    'total_funding': matched_funding_total,
    'matched_count': len(matched_details),
    'matched_details': matched_details,
    'extracted_project_candidates': sorted(list(candidates))
}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_Rzijr1ISlDUOM9pATv8LIjjx': 'file_storage/call_Rzijr1ISlDUOM9pATv8LIjjx.json', 'var_call_Ux2JQYUAZi3uGCxmtmShczUi': 'file_storage/call_Ux2JQYUAZi3uGCxmtmShczUi.json'}

exec(code, env_args)
