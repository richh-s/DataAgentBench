code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_jxuVAh57LFc6hmEX4rv1doBa, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_s5ZLygkXH1OihgI8e3pDkUib, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Prepare funding dataframe-like structure: list of dicts with Project_Name and Amount as int
funding = []
for r in funding_rows:
    name = r.get('Project_Name')
    amt_raw = r.get('Amount')
    try:
        amt = int(amt_raw)
    except:
        try:
            amt = int(float(amt_raw))
        except:
            amt = 0
    funding.append({'Project_Name': name, 'Amount': amt, 'Funding_ID': r.get('Funding_ID')})

# Helper: normalize strings
def norm(s):
    return re.sub(r"\s+", " ", s.strip().lower()) if s else ''

# Extract candidate project names that have spring 2022 in nearby schedule lines
spring_projects = []
pattern = re.compile(r'spring\s*,?\s*2022', re.IGNORECASE)
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if pattern.search(line):
            # look upwards for a likely project title within previous 12 lines
            title = None
            for j in range(i-1, max(i-13, -1), -1):
                candidate = lines[j].strip()
                if not candidate:
                    continue
                low = candidate.lower()
                # skip common labels or lines that are clearly not titles
                if any(tok in low for tok in ['updates', 'project schedule', 'page', 'agenda', 'item', 'meeting date', 'prepared by', 'approved by', 'date prepared', 'subject', 'recommended action', 'discussion']):
                    continue
                if candidate.endswith(':'):
                    continue
                # skip lines that are short (less informative)
                if len(candidate) < 5:
                    continue
                # If line has many lowercase words or looks like a sentence, still accept
                title = candidate
                break
            if title:
                spring_projects.append(title)

# Deduplicate normalized
unique_projects = []
seen = set()
for p in spring_projects:
    n = norm(p)
    if n and n not in seen:
        seen.add(n)
        unique_projects.append(p)

# Now match with funding records using case-insensitive containment
matched = []
for pname in unique_projects:
    pn_norm = norm(pname)
    project_fund_records = []
    total_for_project = 0
    for fr in funding:
        fn = norm(fr['Project_Name'] or '')
        if not fn:
            continue
        # match if either contains the other (word-level)
        if pn_norm in fn or fn in pn_norm:
            project_fund_records.append({'Funding_ID': fr['Funding_ID'], 'Project_Name': fr['Project_Name'], 'Amount': fr['Amount']})
            total_for_project += fr['Amount']
        else:
            # also try token intersection
            pn_tokens = set(re.findall(r"\w+", pn_norm))
            fn_tokens = set(re.findall(r"\w+", fn))
            if pn_tokens and fn_tokens and len(pn_tokens.intersection(fn_tokens)) >= 3:
                project_fund_records.append({'Funding_ID': fr['Funding_ID'], 'Project_Name': fr['Project_Name'], 'Amount': fr['Amount']})
                total_for_project += fr['Amount']
    matched.append({'Extracted_Name': pname, 'Matched_Funding_Records': project_fund_records, 'Project_Funding_Total': total_for_project})

# Overall totals: count of unique extracted projects and sum of their matched funding (avoid double-counting funding records if mapped to multiple projects)
count_projects = len(unique_projects)
all_matched_ids = set()
total_funding = 0
for m in matched:
    for rec in m['Matched_Funding_Records']:
        fid = rec['Funding_ID']
        if fid not in all_matched_ids:
            all_matched_ids.add(fid)
            total_funding += rec['Amount']

# Build result
result = {
    'count_projects_started_spring_2022': count_projects,
    'total_funding_for_these_projects': total_funding,
    'projects': matched
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JdZeXDS8WXzYcSjvWKmpFA4N': ['civic_docs'], 'var_call_jxuVAh57LFc6hmEX4rv1doBa': 'file_storage/call_jxuVAh57LFc6hmEX4rv1doBa.json', 'var_call_AYRtLiY45ynLQxTkvRLwM4v8': ['Funding'], 'var_call_s5ZLygkXH1OihgI8e3pDkUib': 'file_storage/call_s5ZLygkXH1OihgI8e3pDkUib.json'}

exec(code, env_args)
