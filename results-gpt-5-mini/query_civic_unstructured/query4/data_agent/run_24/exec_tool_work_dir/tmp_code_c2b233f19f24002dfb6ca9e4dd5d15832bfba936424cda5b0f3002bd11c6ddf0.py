code = """import json, re

# Load the previous tool results from storage variables (file paths)
with open(var_call_TEOYmhfmkcoWUuH52pFkfr3V, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_qVyGX30AOYCMsaHGBMenIZQN, 'r') as f:
    funding_rows = json.load(f)

texts = [d.get('text','') for d in civic_docs]

season_regex = re.compile(r'(?:.{0,120})(Spring|March|April|May)(?:.{0,40})2022|2022(?:.{0,40})(Spring|March|April|May)', re.IGNORECASE)

candidate_names = []

exclude_prefixes = ('(cid:','Updates','Project Schedule','Project Description','Project Updates','RECOMMENDED ACTION','DISCUSSION','To:','Prepared by','Approved by','Date prepared','Meeting date','Subject','Page','Agenda Item')

for text in texts:
    for m in season_regex.finditer(text):
        idx = m.start()
        # look back up to 400 chars to find a header line
        start_search = max(0, idx-400)
        context = text[start_search:idx]
        # split into lines and take last reasonable header-like line
        lines = [ln.strip() for ln in context.splitlines() if ln.strip()]
        header = None
        # iterate from last to first
        for ln in reversed(lines):
            ln_clean = ln.strip()
            if len(ln_clean) < 6 or len(ln_clean) > 120:
                continue
            if any(ln_clean.startswith(p) for p in exclude_prefixes):
                continue
            # exclude lines that are likely sentences (contain period and many words)
            if ln_clean.count(' ') > 12:
                continue
            # exclude lines that are mostly uppercase words like section headers but could be ok
            if ln_clean.lower().startswith('page'):
                continue
            # exclude generic words
            if ln_clean.lower() in ('discussion','recommended action'):
                continue
            header = ln_clean
            break
        if header:
            candidate_names.append(header)

# deduplicate preserving order
seen = set()
candidates = []
for n in candidate_names:
    key = ' '.join(re.sub(r'\s+', ' ', n).strip().lower().split())
    if key not in seen:
        seen.add(key)
        candidates.append(n)

# Normalize funding rows
funding_map = []
for r in funding_rows:
    name = r.get('Project_Name')
    amt = r.get('Total_Amount')
    try:
        amt_val = int(amt)
    except:
        try:
            amt_val = int(float(amt))
        except:
            amt_val = 0
    funding_map.append({'name': name, 'amount': amt_val})

def normalize(n):
    if not n:
        return ''
    # remove parenthetical suffixes and punctuation, lowercase
    n2 = re.sub(r"\(.*?\)", "", n)
    n2 = re.sub(r"[^0-9a-z ]+", ' ', n2.lower())
    n2 = re.sub(r"\s+", ' ', n2).strip()
    return n2

funding_by_norm = {}
for fr in funding_map:
    norm = normalize(fr['name'])
    funding_by_norm.setdefault(norm, 0)
    funding_by_norm[norm] += fr['amount']

# For each candidate, attempt to find funding
project_results = []
total_funding = 0
matched_funding_norms = set()

for c in candidates:
    cn = normalize(c)
    matched_amount = 0
    # exact match
    if cn in funding_by_norm:
        matched_amount = funding_by_norm[cn]
        matched_funding_norms.add(cn)
    else:
        # substring matching
        for fnorm, famt in funding_by_norm.items():
            if cn and (cn in fnorm or fnorm in cn):
                matched_amount += famt
                matched_funding_norms.add(fnorm)
    project_results.append({'name': c, 'funding': matched_amount})
    total_funding += matched_amount

# Count of projects started in Spring 2022 is number of unique candidates
projects_count = len(candidates)

output = {'projects_count': projects_count, 'total_funding': total_funding, 'projects': project_results}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_KOG9gcEOiv0tTBZAN7qGGGZ6': ['civic_docs'], 'var_call_2g7IvBlsrcuTYdGEbhodVKH9': ['Funding'], 'var_call_TEOYmhfmkcoWUuH52pFkfr3V': 'file_storage/call_TEOYmhfmkcoWUuH52pFkfr3V.json', 'var_call_qVyGX30AOYCMsaHGBMenIZQN': 'file_storage/call_qVyGX30AOYCMsaHGBMenIZQN.json'}

exec(code, env_args)
