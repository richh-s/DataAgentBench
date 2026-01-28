code = """import json, re, os

# Load data from storage-provided file paths
with open(var_call_3hqM1np6KkTn39C8KATGtjxs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_2Ym9gg8atfpTFNFLlyWXF5ZU, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Preprocess funding amounts and names
for rec in funding:
    try:
        rec['Amount'] = int(rec['Amount'])
    except:
        # fallback if empty or malformed
        rec['Amount'] = 0
    rec['Project_Name_clean'] = re.sub(r"[^a-z0-9 ]", "", rec['Project_Name'].lower())

# Find project headings that have an associated "Spring 2022" schedule
pattern = re.compile(r"\bSpring\s*,?\s*2022\b", flags=re.IGNORECASE)
found_projects = []

for doc in docs:
    text = doc.get('text', '')
    for m in pattern.finditer(text):
        start = m.start()
        # look back up to 600 chars to find a project title
        context = text[max(0, start-800):start]
        lines = context.splitlines()
        # reverse iterate to find a candidate title line
        candidate = None
        for line in reversed(lines):
            s = line.strip()
            if not s:
                continue
            # skip lines that are clearly not titles
            if s.lower().startswith('(cid') or s.lower().startswith('page'):
                continue
            if ':' in s:
                # many lines like "Project Schedule:" or "Updates:" or "Project Description:" shouldn't be titles
                continue
            # skip lines that look like dates
            if re.search(r"\b\d{1,2}[-/]?\d{1,2}[-/]?\d{2,4}\b", s):
                continue
            # likely title if length reasonable
            if 3 < len(s) < 150:
                candidate = s
                break
        if candidate:
            # clean excessive whitespace
            candidate = re.sub(r"\s+", " ", candidate).strip()
            found_projects.append(candidate)

# Deduplicate while preserving order
seen = set()
projects = []
for p in found_projects:
    key = p.lower()
    if key not in seen:
        seen.add(key)
        projects.append(p)

# Matching funding records to extracted projects
matched_records = []
unmatched_projects = []

for p in projects:
    pclean = re.sub(r"[^a-z0-9 ]", "", p.lower())
    p_words = [w for w in pclean.split() if len(w)>2]
    matched = []
    for rec in funding:
        fname = rec['Project_Name_clean']
        # exact containment or all significant words present
        if pclean and (pclean in fname or fname in pclean):
            matched.append(rec)
            continue
        if p_words:
            if all(w in fname for w in p_words):
                matched.append(rec)
                continue
    if matched:
        # add unique matched recs
        for mrec in matched:
            if mrec not in matched_records:
                matched_records.append(mrec)
    else:
        unmatched_projects.append(p)

# Count projects (extracted) and sum funding for matched records
count_projects = len(projects)
total_funding = sum(rec['Amount'] for rec in matched_records)

# Prepare output
output = {
    'extracted_projects': projects,
    'count_projects': count_projects,
    'matched_funding_records': [{
        'Funding_ID': rec['Funding_ID'],
        'Project_Name': rec['Project_Name'],
        'Amount': rec['Amount']
    } for rec in matched_records],
    'total_funding': total_funding,
    'unmatched_projects': unmatched_projects
}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_mrKUQUZqQpDRGmJMWm4fFH94': ['civic_docs'], 'var_call_3hqM1np6KkTn39C8KATGtjxs': 'file_storage/call_3hqM1np6KkTn39C8KATGtjxs.json', 'var_call_n9w8fx8eWTs8Wte7JafN2ugu': ['Funding'], 'var_call_2Ym9gg8atfpTFNFLlyWXF5ZU': 'file_storage/call_2Ym9gg8atfpTFNFLlyWXF5ZU.json'}

exec(code, env_args)
