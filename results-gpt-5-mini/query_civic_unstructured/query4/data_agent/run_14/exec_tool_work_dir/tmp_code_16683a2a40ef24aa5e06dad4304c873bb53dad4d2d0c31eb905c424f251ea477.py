code = """import json
import re
import unicodedata

# Load data
with open(var_call_z5NGOn9MI8UDM6KCNFtBuvgC, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_0C7EHHinH7FML83N9qX164I3, 'r') as f:
    funding_rows = json.load(f)

# Normalize funding
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

# function to normalize strings for matching
def norm(s):
    if s is None:
        return ''
    s2 = unicodedata.normalize('NFKD', s)
    s2 = re.sub(r"[^0-9a-zA-Z]+", ' ', s2)
    return s2.strip().lower()

# find project titles that start in Spring 2022
season_terms = ['spring','march','april','may']
projects_found = []
for doc in civic_docs:
    text = doc.get('text','')
    lowtext = text.lower()
    for term in season_terms:
        for m in re.finditer(re.escape(term), lowtext):
            idx = m.start()
            # check if '2022' within +/-120 chars
            start_window = max(0, idx-120)
            end_window = min(len(lowtext), idx+120)
            window = lowtext[start_window:end_window]
            if '2022' in window:
                # find preceding lines up to idx
                prefix = text[max(0, start_window-400):idx]
                lines = prefix.splitlines()
                candidate = None
                for line in reversed(lines):
                    s = line.strip()
                    if not s:
                        continue
                    if re.search(r'project|park|facility|improvements|road|bridge|playground|walkway|structure|median|culvert|retaining wall|skate park|shade structure', s, re.IGNORECASE):
                        candidate = s
                        break
                    if 2 <= len(s.split()) <= 8 and len(s) < 120 and s[0].isupper():
                        candidate = s
                        break
                if candidate is None:
                    # fallback to last non-empty line
                    for line in reversed(lines):
                        s = line.strip()
                        if s:
                            candidate = s
                            break
                if candidate:
                    cand = re.sub(r'\s+', ' ', candidate).strip()
                    cand = re.sub(r'^[\d\W]+', '', cand).strip()
                    projects_found.append(cand)

# deduplicate
unique_projects = []
seen = set()
for p in projects_found:
    key = p.lower()
    if key not in seen:
        seen.add(key)
        unique_projects.append(p)

# prepare normalized funding list
norm_funding = [(norm(r['Project_Name']), r['Project_Name'], r['Amount']) for r in funding]

matched = []
unmatched = []
for pt in unique_projects:
    npt = norm(pt)
    found = False
    for nf, orig, amt in norm_funding:
        if npt == nf or npt in nf or nf in npt:
            matched.append({'project_title': pt, 'funding_name': orig, 'amount': amt})
            found = True
            break
    if not found:
        # token overlap
        pt_tokens = set(npt.split())
        best = None
        best_overlap = 0
        for nf, orig, amt in norm_funding:
            nf_tokens = set(nf.split())
            overlap = len(pt_tokens & nf_tokens)
            if overlap > best_overlap and overlap >= 2:
                best_overlap = overlap
                best = (orig, amt)
        if best:
            matched.append({'project_title': pt, 'funding_name': best[0], 'amount': best[1]})
            found = True
    if not found:
        unmatched.append(pt)

# count projects started in Spring 2022
projects_started_count = len(unique_projects)
# sum funding for matched unique project titles (avoid duplicates by project_title)
amount_sum = 0
seen_titles = set()
for m in matched:
    t = m['project_title']
    if t not in seen_titles:
        amount_sum += m['amount']
        seen_titles.add(t)

result = {
    'projects_started_count': projects_started_count,
    'total_funding_for_matched_projects': amount_sum,
    'matched_projects': matched,
    'unmatched_project_titles': unmatched
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Mtan0j93JBLHMVNO1YxvtkOQ': ['civic_docs'], 'var_call_kwSpEb6yGaN6VMlAdvT975TG': ['Funding'], 'var_call_z5NGOn9MI8UDM6KCNFtBuvgC': 'file_storage/call_z5NGOn9MI8UDM6KCNFtBuvgC.json', 'var_call_0C7EHHinH7FML83N9qX164I3': 'file_storage/call_0C7EHHinH7FML83N9qX164I3.json'}

exec(code, env_args)
