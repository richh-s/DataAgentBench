code = """import json
from pathlib import Path

# Load tool result variables (file paths)
path_civic = Path(var_call_O41YPgIMwwpDQ0mDeNFIYiWp)
path_funding = Path(var_call_nwCBWIyTNPQah9PPbJJOWmRT)

civic = json.loads(path_civic.read_text())
funding = json.loads(path_funding.read_text())

# Normalize funding amounts to int
for f in funding:
    try:
        f['Amount'] = int(f['Amount'])
    except:
        try:
            f['Amount'] = int(float(f['Amount']))
        except:
            f['Amount'] = None

# Create combined text
combined_text = "\n\n".join(d.get('text','') for d in civic)
combined_text_lower = combined_text.lower()

matches = []

# Helper: extract status snippet near occurrence
def extract_status(doc_text, project_name):
    txt = doc_text
    name_lower = project_name.lower()
    idx = txt.lower().find(name_lower)
    if idx == -1:
        # try base name without parenthetical
        base = project_name.split('(')[0].strip().lower()
        idx = txt.lower().find(base)
        if idx == -1:
            return "(status not found in docs)"
    # take window after occurrence
    window = txt[idx: idx+1500]
    # look for 'Updates:'
    up_idx = window.lower().find('updates:')
    if up_idx != -1:
        # capture until double newline or 'Project Schedule' or 'Project Schedule:'
        seg = window[up_idx+8:]
        # cut at 'Project Schedule' if present
        psch = seg.lower().find('project schedule')
        if psch != -1:
            seg = seg[:psch]
        # Cut at double newline
        dbl = seg.find('\n\n')
        if dbl != -1:
            seg = seg[:dbl]
        return seg.strip().replace('\n',' ').replace('\r',' ').strip()
    # fallback: look for headings like '(Design)', '(Construction)', 'Not Started', 'Completed'
    for kw in ['under construction', 'construction was completed', 'complete construction', 'complete design', 'complete design:', 'project is currently under construction', 'project is in the preliminary design phase', 'project is in the preliminary design', 'project is in the preliminary design phase']:
        if kw in window.lower():
            # return nearby phrase
            start = window.lower().find(kw)
            return window[start:start+200].strip().replace('\n',' ')
    # else try to find section header above occurrence (look back 200 chars for section like 'Capital Improvement Projects (Design)')
    back = txt[max(0, idx-500): idx]
    headers = ['capital improvement projects (design)','capital improvement projects (construction)','capital improvement projects (not started)','disaster recovery projects','capital improvement projects']
    for h in headers:
        if h in back.lower():
            return h
    return '(status not found)'

# For each funding record, decide if related to FEMA or emergency
for f in funding:
    pname = f['Project_Name']
    pname_lower = pname.lower()
    related = False
    reason = []
    # If project name contains 'fema' it's related
    if 'fema' in pname_lower:
        related = True
        reason.append('FEMA in project name')
    # If project name appears in any civic doc that also mentions FEMA or emergency
    base = pname.split('(')[0].strip()
    if base and base.lower() in combined_text_lower:
        # find docs where it appears
        for doc in civic:
            t = doc.get('text','')
            if base.lower() in t.lower():
                if 'fema' in t.lower() or 'emergency' in t.lower() or 'outdoor warning' in t.lower() or 'warning' in t.lower():
                    related = True
                    reason.append('Mentioned near FEMA/emergency in civic docs')
    # Additionally, if combined text contains words 'emergency' and project name contains 'warning' or 'sirens' etc
    if ('emergency' in combined_text_lower) and any(k in pname_lower for k in ['warning','sirens','outdoor']):
        related = True
        reason.append('Emergency-related keyword match')

    if related:
        # find status by searching docs
        status = '(status not found)'
        # search docs that mention the project base
        found = False
        for doc in civic:
            t = doc.get('text','')
            if base.lower() in t.lower():
                status = extract_status(t, pname)
                found = True
                break
        if not found:
            # try to extract status from combined text
            status = extract_status(combined_text, pname)
        matches.append({
            'Project_Name': pname,
            'Funding_Source': f.get('Funding_Source'),
            'Amount': f.get('Amount'),
            'Status': status,
            'Match_Reasons': reason
        })

# Also ensure we include funding records where project name doesn't include FEMA but civic docs include projects with 'FEMA' nearby not matched to funding table names
# Find project-like headings in civic docs near 'FEMA' or 'emergency'
# Simple heuristic: lines before 'Updates:' up to 80 chars
extra = []
for doc in civic:
    t = doc.get('text','')
    low = t.lower()
    if 'fema' in low or 'emergency' in low:
        parts = t.split('\n')
        for i,line in enumerate(parts):
            if 'updates:' in line.lower():
                # get previous non-empty line as title candidate
                j = i-1
                while j>=0 and parts[j].strip()=='' and j>i-5:
                    j-=1
                if j>=0:
                    candidate = parts[j].strip()
                    # exclude very short candidates
                    if len(candidate) > 5 and len(candidate) < 200:
                        # check if already in matches
                        if not any(m['Project_Name'].lower().split('(')[0].strip() == candidate.lower().split('(')[0].strip() for m in matches):
                            extra.append({'Project_Name': candidate, 'Funding_Source': None, 'Amount': None, 'Status': extract_status(t, candidate), 'Match_Reasons': ['Found in civic docs near FEMA/emergency']})

# combine unique by project name
all_results = {}
for m in matches+extra:
    key = m['Project_Name']
    if key not in all_results:
        all_results[key] = m

results_list = list(all_results.values())

# Sort results by Project_Name
results_list = sorted(results_list, key=lambda x: x['Project_Name'].lower())

# Prepare final JSON-serializable output (ensure amounts are ints or null)
for r in results_list:
    if r['Amount'] is None:
        r['Amount'] = None
    else:
        try:
            r['Amount'] = int(r['Amount'])
        except:
            r['Amount'] = None

import json
print("__RESULT__:")
print(json.dumps(results_list))"""

env_args = {'var_call_O41YPgIMwwpDQ0mDeNFIYiWp': 'file_storage/call_O41YPgIMwwpDQ0mDeNFIYiWp.json', 'var_call_nwCBWIyTNPQah9PPbJJOWmRT': 'file_storage/call_nwCBWIyTNPQah9PPbJJOWmRT.json'}

exec(code, env_args)
