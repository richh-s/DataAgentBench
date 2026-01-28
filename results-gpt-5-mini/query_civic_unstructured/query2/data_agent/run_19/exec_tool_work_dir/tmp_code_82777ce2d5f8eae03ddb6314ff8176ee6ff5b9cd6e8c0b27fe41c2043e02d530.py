code = """import json, re

# Load tool results from storage (file paths)
with open(var_call_lTwyHRaUdN2O9L62qi1wbTrs, 'r') as f:
    funding_records = json.load(f)
with open(var_call_EOPIjH1hij8LDLdbl6SuMdH9, 'r') as f:
    civic_docs = json.load(f)

# Helper functions
def normalize(text):
    if text is None:
        return ""
    # remove parenthetical suffixes and punctuation, lowercase
    text = re.sub(r"\(.*?\)", "", text)
    text = re.sub(r"[^0-9a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()

park_keywords = ['park','playground','walkway','bench','benches','shade','paver','playground','playground','walk']

# Find project titles in civic docs that have a "completed" mention with 2022
completed_titles = set()
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i,line in enumerate(lines):
        low = line.lower()
        if 'completed' in low and '2022' in low:
            # search backwards up to 12 lines for a likely title
            for j in range(max(0,i-12), i):
                cand = lines[j].strip()
                if not cand:
                    continue
                lc = cand.lower()
                # skip lines that are clearly not titles
                if any(k in lc for k in ['updates','project schedule','project description','agenda item', 'page', 'cid:']):
                    continue
                # avoid lines that are like '(cid:190) Updates:'
                if re.match(r"^[\(\[]?cid", lc):
                    continue
                # likely title
                completed_titles.add(cand)
                break

# Normalize completed titles
norm_completed = set(normalize(t) for t in completed_titles)

# Filter funding records for park-related projects
park_fundings = []
for r in funding_records:
    pname = r.get('Project_Name','')
    lp = pname.lower()
    if any(k in lp for k in park_keywords):
        # include
        try:
            amt = int(r.get('Amount') or 0)
        except:
            try:
                amt = int(float(r.get('Amount')))
            except:
                amt = 0
        park_fundings.append({'Funding_ID': r.get('Funding_ID'), 'Project_Name': pname, 'Amount': amt})

# Match park funding records to completed titles
matched = []
for pf in park_fundings:
    pname = pf['Project_Name']
    n_pname = normalize(pname)
    matched_flag = False
    # direct substring match
    for ct in norm_completed:
        if n_pname and (n_pname in ct or ct in n_pname):
            matched_flag = True
            break
        # token overlap match
        p_tokens = set(n_pname.split())
        c_tokens = set(ct.split())
        # require at least 2 token overlap or include word 'park' and one token overlap
        if p_tokens & c_tokens:
            overlap = p_tokens & c_tokens
            if ('park' in p_tokens or 'playground' in p_tokens or 'walkway' in p_tokens) and len(overlap) >= 1:
                matched_flag = True
                break
            if len(overlap) >= 2:
                matched_flag = True
                break
    if matched_flag:
        matched.append(pf)

# Sum amounts
total = sum(m['Amount'] for m in matched)

# Prepare output
output = {'total_funding': total, 'matched_projects': matched, 'extracted_completed_titles': list(completed_titles)}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_C6VE98VHwlHBH15ZQlfQ8dGm': ['civic_docs'], 'var_call_aRPao80bjabitIv1wMHDnFMh': ['Funding'], 'var_call_lTwyHRaUdN2O9L62qi1wbTrs': 'file_storage/call_lTwyHRaUdN2O9L62qi1wbTrs.json', 'var_call_EOPIjH1hij8LDLdbl6SuMdH9': 'file_storage/call_EOPIjH1hij8LDLdbl6SuMdH9.json'}

exec(code, env_args)
