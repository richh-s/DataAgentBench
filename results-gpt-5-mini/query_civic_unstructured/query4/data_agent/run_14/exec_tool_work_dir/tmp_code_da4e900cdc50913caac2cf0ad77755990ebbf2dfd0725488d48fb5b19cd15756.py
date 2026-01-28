code = """import json
import re

# Load data from storage variables provided by previous tool calls
# var_call_z5NGOn9MI8UDM6KCNFtBuvgC and var_call_0C7EHHinH7FML83N9qX164I3

with open(var_call_z5NGOn9MI8UDM6KCNFtBuvgC, 'r') as f:
    civic_docs = json.load(f)

with open(var_call_0C7EHHinH7FML83N9qX164I3, 'r') as f:
    funding_rows = json.load(f)

# Normalize funding rows to list of dicts with Project_Name and Amount as int
funding = []
for r in funding_rows:
    name = r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_int = int(amt)
    except:
        try:
            amt_int = int(float(amt))
        except:
            amt_int = 0
    funding.append({'Project_Name': name, 'Amount': amt_int})

# Regex to find Begin lines indicating start in Spring 2022
begin_regex = re.compile(r'Begin[^\n]{0,80}(Spring|March|April|May)[^\n]{0,80}2022', re.IGNORECASE)

found_projects = []

for doc in civic_docs:
    text = doc.get('text','')
    for m in begin_regex.finditer(text):
        start_idx = m.start()
        # look backwards up to 600 chars to find a project title line
        back = text[max(0, start_idx-800):start_idx]
        # split into lines and find last line containing 'Project' (case-insensitive)
        lines = back.splitlines()
        candidate = None
        for line in reversed(lines):
            s = line.strip()
            if not s:
                continue
            # prefer lines that contain the word 'Project' or 'Park' or 'Facility' or 'Improvements' or 'Road' or 'Bridge' or 'Playground' or 'Walkway' or 'Structure'
            if re.search(r'Project|Park|Facility|Improvements|Road|Bridge|Playground|Walkway|Structure|Median|Culvert|Retaining Wall|Skate Park|Shade Structure', s, re.IGNORECASE):
                candidate = s
                break
            # else if line is title-cased and reasonable length, take it
            if 2 <= len(s.split()) <= 8 and len(s) < 120 and s[0].isupper():
                candidate = s
                break
        if candidate is None:
            # fallback: take the last non-empty line
            for line in reversed(lines):
                s = line.strip()
                if s:
                    candidate = s
                    break
        if candidate:
            # clean candidate
            cand = re.sub(r'\s+', ' ', candidate).strip()
            # remove leading numbering or bullets
            cand = re.sub(r'^[\d\W]+', '', cand).strip()
            found_projects.append({'project_title': cand, 'match_text': m.group(0), 'doc_filename': doc.get('filename')})

# Deduplicate project titles (case-insensitive)
unique_projects = {}
for p in found_projects:
    key = p['project_title'].lower()
    if key not in unique_projects:
        unique_projects[key] = p

project_titles = [v['project_title'] for v in unique_projects.values()]

# Now match project_titles to funding entries
# Define helper to normalize strings for fuzzy matching
import unicodedata

def norm(s):
    if s is None:
        return ''
    s2 = unicodedata.normalize('NFKD', s)
    s2 = re.sub(r"[^0-9a-zA-Z]+", ' ', s2)
    return s2.strip().lower()

norm_funding = [(norm(r['Project_Name']), r['Project_Name'], r['Amount']) for r in funding]

matched = []
unmatched_projects = []

for pt in project_titles:
    npt = norm(pt)
    found = False
    # Try exact or substring matches
    for nf, orig_name, amt in norm_funding:
        if npt == nf or npt in nf or nf in npt:
            matched.append({'project_title': pt, 'funding_name': orig_name, 'amount': amt})
            found = True
            break
    if not found:
        # try partial token overlap
        pt_tokens = set(npt.split())
        best = None
        best_overlap = 0
        for nf, orig_name, amt in norm_funding:
            nf_tokens = set(nf.split())
            overlap = len(pt_tokens & nf_tokens)
            if overlap > best_overlap and overlap >= 2:
                best_overlap = overlap
                best = (orig_name, amt)
        if best:
            matched.append({'project_title': pt, 'funding_name': best[0], 'amount': best[1]})
            found = True
    if not found:
        unmatched_projects.append(pt)

# Compute unique project count and total funding for matched ones
unique_matched_titles = {m['project_title']: m for m in matched}
count_started = len(unique_projects)  # count of projects detected starting in Spring 2022
# But funding total should sum funding for matched projects only
total_funding = sum(m['amount'] for m in unique_matched_titles.values())

# Prepare result dictionary
result = {
    'projects_started_count': count_started,
    'total_funding_for_matched_projects': total_funding,
    'matched_projects': matched,
    'unmatched_project_titles': unmatched_projects
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Mtan0j93JBLHMVNO1YxvtkOQ': ['civic_docs'], 'var_call_kwSpEb6yGaN6VMlAdvT975TG': ['Funding'], 'var_call_z5NGOn9MI8UDM6KCNFtBuvgC': 'file_storage/call_z5NGOn9MI8UDM6KCNFtBuvgC.json', 'var_call_0C7EHHinH7FML83N9qX164I3': 'file_storage/call_0C7EHHinH7FML83N9qX164I3.json'}

exec(code, env_args)
