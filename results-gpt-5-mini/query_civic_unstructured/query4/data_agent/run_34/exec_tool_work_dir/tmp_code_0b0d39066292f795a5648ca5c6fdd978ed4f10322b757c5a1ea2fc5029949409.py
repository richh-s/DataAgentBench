code = """import json
import re
import pandas as pd

# Load data from storage-provided file paths
docs_path = var_call_T7sf1DXAkweBowsJnBnlIKEa
funding_path = var_call_sk4Py445O2dS9gieZNkgmkxu

with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Compile regexes for Spring 2022 and months March/April/May 2022
spring_regex = re.compile(r"\bSpring\s*2022\b", re.IGNORECASE)
month_regex = re.compile(r"\b(March|April|May)\s*2022\b", re.IGNORECASE)
alt_regex = re.compile(r"2022[-_/ ]?(March|April|May)", re.IGNORECASE)

candidate_projects = []

def is_valid_title(line):
    if not line:
        return False
    line = line.strip()
    if len(line) < 5 or len(line) > 200:
        return False
    low = line.lower()
    # Exclude common non-title prefixes
    bad_prefixes = ['page', 'agenda', 'item', 'to:', 'subject:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'recommend', 'discussion', 'updates', '(cid']
    for bp in bad_prefixes:
        if low.startswith(bp):
            return False
    if ':' in line and not line.lower().strip().endswith('project'):
        # lines like 'Project Schedule:' are not titles
        return False
    # Must contain letters
    if not re.search(r'[A-Za-z]', line):
        return False
    return True

for doc in docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if spring_regex.search(line) or month_regex.search(line) or alt_regex.search(line):
            # search backwards up to 10 lines for a plausible title
            title = None
            for j in range(max(0, i-12), i+1)[::-1]:
                candidate = lines[j].strip()
                if is_valid_title(candidate):
                    # Avoid lines that are just 'Project Schedule' or 'Project Updates'
                    low = candidate.lower()
                    if 'project schedule' in low or candidate.lower().startswith('project schedule'):
                        continue
                    if candidate.lower().startswith('updates') or candidate.lower().startswith('project updates'):
                        continue
                    # Also skip lines that are single words like 'Discussion'
                    if len(candidate.split()) <= 2 and not candidate.lower().endswith('project'):
                        continue
                    title = candidate
                    break
            if title:
                candidate_projects.append(title)

# Deduplicate while preserving order
seen = set()
projects = []
for p in candidate_projects:
    norm = p.strip()
    if norm not in seen:
        seen.add(norm)
        projects.append(norm)

# Load funding into DataFrame
fund_df = pd.DataFrame(funding)
# Normalize funding amounts to int
if not fund_df.empty:
    fund_df['Amount'] = fund_df['Amount'].astype(int)
    fund_df['Project_Name_str'] = fund_df['Project_Name'].astype(str)
else:
    fund_df['Amount'] = pd.Series(dtype=int)
    fund_df['Project_Name_str'] = pd.Series(dtype=str)

# For each project, try to find matching funding records
results = []
for proj in projects:
    matched_records = fund_df[fund_df['Project_Name_str'].str.lower() == proj.lower()]
    if matched_records.empty:
        # try substring match
        matched_records = fund_df[fund_df['Project_Name_str'].str.lower().str.contains(re.escape(proj.lower()))]
    if matched_records.empty:
        # try reverse containment
        matched_records = fund_df[fund_df['Project_Name_str'].str.lower().apply(lambda x: proj.lower() in x)]
    # Sum amounts
    total = int(matched_records['Amount'].sum()) if not matched_records.empty else 0
    record_names = matched_records['Project_Name_str'].tolist()
    results.append({'project': proj, 'matched_funding_amount': total, 'matched_records': record_names})

# Compute overall count and total funding
count_projects = len(projects)
total_funding = sum(r['matched_funding_amount'] for r in results)

output = {'count_projects': count_projects, 'total_funding': total_funding, 'projects': results}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_HW9ZkBmGMYzpwgAdnQj3jbbt': ['civic_docs'], 'var_call_tAowD8W9bhtcSi6T7DehBuLG': ['Funding'], 'var_call_T7sf1DXAkweBowsJnBnlIKEa': 'file_storage/call_T7sf1DXAkweBowsJnBnlIKEa.json', 'var_call_sk4Py445O2dS9gieZNkgmkxu': 'file_storage/call_sk4Py445O2dS9gieZNkgmkxu.json'}

exec(code, env_args)
