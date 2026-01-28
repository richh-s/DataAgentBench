code = """import json
import re
from pathlib import Path

# Files provided in storage
civic_docs_path = Path(var_call_wqikkWRqfgawfU0hW7Q1BYJO)
funding_path = Path(var_call_QLafuON7ilSuw3U6TxZ544tK)

civic_docs = json.loads(civic_docs_path.read_text())
funding_rows = json.loads(funding_path.read_text())

# Build funding lookup (normalized)
funding_lookup = {}
for r in funding_rows:
    name = r.get('Project_Name')
    amt = r.get('Total_Amount')
    try:
        amt_val = int(amt)
    except Exception:
        # try convert from string with commas
        amt_val = int(str(amt).replace(',','')) if amt not in (None, '') else 0
    funding_lookup[name.strip().lower()] = amt_val

# Regex to find Spring 2022 mentions
spring2022_re = re.compile(r"spring\s*,?\s*2022", re.IGNORECASE)

found_projects = []

for doc in civic_docs:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if spring2022_re.search(ln):
            # search backwards for probable project title
            title = None
            for j in range(i-1, max(-1, i-30), -1):
                cand = lines[j]
                if not cand:
                    continue
                low = cand.lower()
                # skip lines that are obviously not titles
                if low.startswith('(cid') or low.startswith('page') or low.startswith('agenda') or low.startswith('item'):
                    continue
                if ':' in cand and len(cand) < 40:
                    # likely a schedule line like 'Complete Design: Spring 2023' skip
                    continue
                # require at least a few letters and start with uppercase or contain the word 'Project' or 'Park' etc
                if len(cand) > 5 and (cand[0].isupper() or 'project' in low or 'park' in low or 'road' in low or 'repair' in low or 'improvements' in low or 'improvement' in low):
                    title = cand
                    break
            if not title:
                # fallback previous non-empty
                for j in range(i-1, max(-1, i-10), -1):
                    cand = lines[j]
                    if cand:
                        title = cand
                        break
            if title:
                # Clean title removing leading bullets or numbers
                title_clean = re.sub(r"^[\W\d]+","", title).strip()
                if title_clean and title_clean.lower() not in [t.lower() for t in found_projects]:
                    found_projects.append(title_clean)

# Deduplicate while preserving order
unique_projects = []
seen = set()
for p in found_projects:
    key = p.strip().lower()
    if key not in seen:
        seen.add(key)
        unique_projects.append(p)

# Match with funding
matched = []
unmatched = []
total_funding = 0
for p in unique_projects:
    key = p.strip().lower()
    if key in funding_lookup:
        amt = funding_lookup[key]
        matched.append({'Project_Name': p, 'Amount': amt})
        total_funding += amt
    else:
        # try fuzzy: find funding entries that startwith or contain the project name
        found_amt = 0
        found_name = None
        for fname, famt in funding_lookup.items():
            if key in fname or fname in key:
                found_amt = famt
                found_name = fname
                break
        if found_name:
            matched.append({'Project_Name': p, 'Matched_Funding_Name': found_name, 'Amount': found_amt})
            total_funding += found_amt
        else:
            unmatched.append(p)

result = {
    'count_projects_found_with_spring_2022': len(unique_projects),
    'total_funding_for_these_projects': total_funding,
    'projects': unique_projects,
    'matched_funding_records': matched,
    'unmatched_projects': unmatched
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BTa81LopYovhmVIaPjFUZbCP': ['civic_docs'], 'var_call_hjGwwxQ5aVIVVOkFVOmxH1YI': ['Funding'], 'var_call_wqikkWRqfgawfU0hW7Q1BYJO': 'file_storage/call_wqikkWRqfgawfU0hW7Q1BYJO.json', 'var_call_QLafuON7ilSuw3U6TxZ544tK': 'file_storage/call_QLafuON7ilSuw3U6TxZ544tK.json'}

exec(code, env_args)
