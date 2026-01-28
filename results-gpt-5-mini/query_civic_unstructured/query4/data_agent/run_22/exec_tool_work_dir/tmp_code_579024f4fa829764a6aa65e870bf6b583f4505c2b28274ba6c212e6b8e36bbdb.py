code = """import json, re

# Load data from storage file paths provided by previous tool calls
with open(var_call_oM9fF0ceT8cpCIpTFp0douXc, 'r') as f:
    docs = json.load(f)
with open(var_call_8fzGQWMf0n1awFW2g5xDFjUd, 'r') as f:
    funding = json.load(f)

candidates = []
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r'spring\s*2022', line, re.I):
            # look back up to 10 lines for a candidate project title
            title = None
            for j in range(i-1, max(i-11, -1), -1):
                l = lines[j].strip()
                if not l:
                    continue
                if ':' in l:
                    continue
                # skip short or very long lines
                if len(l) < 5 or len(l) > 200:
                    continue
                # skip all-caps short headings
                if l.upper() == l and len(l.split()) < 10:
                    continue
                title = l
                break
            if title:
                candidates.append(title)

# Normalize unique preserving order
seen = set()
uniq_projects = []
for c in candidates:
    c2 = ' '.join(c.split())
    if c2 not in seen:
        seen.add(c2)
        uniq_projects.append(c2)

# Prepare funding matching
fund_rows = funding
matched_ids = set()
matched_records = []

def tokenize(s):
    return [t.lower() for t in re.findall(r"[A-Za-z0-9]+", s)]

for proj in uniq_projects:
    p_low = proj.lower()
    p_tokens = set(tokenize(proj))
    for row in fund_rows:
        fname = row.get('Project_Name','')
        f_low = fname.lower()
        if not fname:
            continue
        match = False
        if p_low in f_low or f_low in p_low:
            match = True
        else:
            f_tokens = set(tokenize(fname))
            if p_tokens and f_tokens:
                inter = p_tokens & f_tokens
                if len(inter) >= 2 or len(inter) >= 0.5 * min(len(p_tokens), len(f_tokens)):
                    match = True
        if match:
            fid = row.get('Funding_ID')
            if fid not in matched_ids:
                matched_ids.add(fid)
                # parse amount
                amt_raw = row.get('Amount')
                try:
                    amt = int(float(amt_raw))
                except:
                    amt = 0
                matched_records.append({'Funding_ID': fid, 'Project_Name': row.get('Project_Name'), 'Amount': amt})

# Sum amounts
total_funding = sum(r['Amount'] for r in matched_records)

result = {
    'project_count_identified': len(uniq_projects),
    'total_funding_matched': total_funding,
    'identified_projects': uniq_projects,
    'matched_funding_records': matched_records
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_90KW5gb5l0aKm4fGIQLSCn1V': ['civic_docs'], 'var_call_GNu0SDGXscZavzXu7agaWGPl': ['Funding'], 'var_call_oM9fF0ceT8cpCIpTFp0douXc': 'file_storage/call_oM9fF0ceT8cpCIpTFp0douXc.json', 'var_call_8fzGQWMf0n1awFW2g5xDFjUd': 'file_storage/call_8fzGQWMf0n1awFW2g5xDFjUd.json'}

exec(code, env_args)
