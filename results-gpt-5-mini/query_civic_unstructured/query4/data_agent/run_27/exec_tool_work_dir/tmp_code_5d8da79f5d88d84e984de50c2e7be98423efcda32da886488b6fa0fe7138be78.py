code = """import json
import re

# Load the large query results from storage file paths
with open(var_call_PkTliFj7k0N4rX3E1QJLtIYp, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_TqHwFfltDLxtEcYvlRowYRZ9, 'r') as f:
    funding_rows = json.load(f)

# Normalize funding table into list of dicts with amounts as ints
funding = []
for r in funding_rows:
    try:
        amt = int(r.get('Amount') if isinstance(r.get('Amount'), (int, float)) else int(str(r.get('Amount')).replace(',', '')))
    except Exception:
        try:
            amt = int(float(r.get('Amount')))
        except Exception:
            amt = 0
    funding.append({'Project_Name': r.get('Project_Name', '').strip(), 'Amount': amt, 'Funding_ID': r.get('Funding_ID'), 'Funding_Source': r.get('Funding_Source')})

# Helper normalize
def norm(s):
    return re.sub(r"[^0-9a-z]", "", s.lower())

# Find projects with Begin Construction containing 'spring' and '2022'
found_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if 'begin' in line.lower() and 'construction' in line.lower():
            # check if spring and 2022 appear in same line
            if re.search(r'spring', line, re.I) and re.search(r'2022', line):
                # find project name by searching backward for a plausible title
                pname = None
                for k in range(1, 12):
                    idx = i - k
                    if idx < 0:
                        break
                    cand = lines[idx].strip()
                    if not cand:
                        continue
                    # skip lines that look like labels
                    if re.search(r'update|updates|project schedule|project description|agenda item|meeting date|prepared by|approved by|page \d+', cand, re.I):
                        continue
                    if cand.startswith('(') or cand.lower().startswith('cid:'):
                        continue
                    # avoid lines containing ':' which are likely labels
                    if ':' in cand:
                        continue
                    # small lines like 'Item' skip
                    if len(cand) < 3:
                        continue
                    pname = cand
                    break
                if pname is None:
                    # fallback: use previous non-empty line
                    for idx in range(i-1, -1, -1):
                        cand = lines[idx].strip()
                        if cand:
                            pname = cand
                            break
                if pname:
                    pname = re.sub(r"\s+", " ", pname).strip()
                    found_projects.append(pname)
        else:
            # sometimes pattern 'Begin Construction: Spring/Summer 2022' or 'Begin Construction: Spring/Summer 2022' -> still contains 'spring' and '2022' check
            if re.search(r'begin\s+construction', line, re.I) and re.search(r'spring', line, re.I) and re.search(r'2022', line):
                # same extraction
                pname = None
                for k in range(1, 12):
                    idx = i - k
                    if idx < 0:
                        break
                    cand = lines[idx].strip()
                    if not cand:
                        continue
                    if re.search(r'update|updates|project schedule|project description|agenda item|meeting date|prepared by|approved by|page \d+', cand, re.I):
                        continue
                    if cand.startswith('(') or cand.lower().startswith('cid:'):
                        continue
                    if ':' in cand:
                        continue
                    if len(cand) < 3:
                        continue
                    pname = cand
                    break
                if pname is None:
                    for idx in range(i-1, -1, -1):
                        cand = lines[idx].strip()
                        if cand:
                            pname = cand
                            break
                if pname:
                    pname = re.sub(r"\s+", " ", pname).strip()
                    found_projects.append(pname)

# Deduplicate preserving order
seen = set()
projects = []
for p in found_projects:
    key = p.lower()
    if key not in seen:
        seen.add(key)
        projects.append(p)

# Now match projects to funding table using multiple matching strategies
matched = []
unmatched = []
for p in projects:
    pnorm = norm(p)
    matches = []
    for f in funding:
        fname = f['Project_Name']
        if not fname:
            continue
        fnorm = norm(fname)
        if pnorm == fnorm:
            matches.append(f)
        else:
            # substring match either direction
            if pnorm in fnorm or fnorm in pnorm:
                matches.append(f)
            else:
                # fuzzy: check words overlap
                pwords = set(re.findall(r"[a-z0-9]+", p.lower()))
                fwords = set(re.findall(r"[a-z0-9]+", fname.lower()))
                if len(pwords & fwords) >= 3:
                    matches.append(f)
    if matches:
        total_amt = sum(m['Amount'] for m in matches)
        matched.append({'Project_Name': p, 'Matched_Funding_Entries': matches, 'Total_Matched_Amount': total_amt})
    else:
        unmatched.append(p)

# Aggregate totals
num_projects = len(projects)
# For total funding, sum unique matched funding entries to avoid double-counting same funding record if multiple projects matched to same funding row
matched_funding_ids = set()
total_funding = 0
for m in matched:
    for entry in m['Matched_Funding_Entries']:
        fid = entry.get('Funding_ID')
        if fid not in matched_funding_ids:
            matched_funding_ids.add(fid)
            total_funding += entry['Amount']

# Prepare simple output
out = {
    'num_projects_found_in_docs_with_begin_construction_spring_2022': num_projects,
    'total_funding_for_these_projects': total_funding,
    'projects': []
}
for m in matched:
    out['projects'].append({'Project_Name': m['Project_Name'], 'Total_Matched_Amount': m['Total_Matched_Amount'], 'Matched_Funding_Entries': [{'Funding_ID': e.get('Funding_ID'), 'Project_Name': e.get('Project_Name'), 'Amount': e.get('Amount'), 'Funding_Source': e.get('Funding_Source')} for e in m['Matched_Funding_Entries']]})

# include unmatched if any
if unmatched:
    out['unmatched_projects'] = unmatched

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_bm6chtbjTJGfnPAjCXTXMzQy': ['civic_docs'], 'var_call_PCbz92iOxfdFItuC1LWUz8hE': ['Funding'], 'var_call_NA6irinFJ9hG00qRQhMMEkff': 'file_storage/call_NA6irinFJ9hG00qRQhMMEkff.json', 'var_call_PkTliFj7k0N4rX3E1QJLtIYp': 'file_storage/call_PkTliFj7k0N4rX3E1QJLtIYp.json', 'var_call_TqHwFfltDLxtEcYvlRowYRZ9': 'file_storage/call_TqHwFfltDLxtEcYvlRowYRZ9.json'}

exec(code, env_args)
