code = """import json
from pathlib import Path

# Load the stored query results from previous tool calls
# The storage file paths are provided in variables (these names come from the tool call ids)
var_call_xHTQYwVDgsOGMdNJNzehcdiQ_path = var_call_xHTQYwVDgsOGMdNJNzehcdiQ
var_call_ucr9bvHA93EHNq2cqRusfhzm_path = var_call_ucr9bvHA93EHNq2cqRusfhzm

with open(var_call_xHTQYwVDgsOGMdNJNzehcdiQ_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_ucr9bvHA93EHNq2cqRusfhzm_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding amounts to int
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        # remove commas, currency symbols
        s = str(r.get('Amount','0'))
        s = ''.join(c for c in s if c.isdigit())
        r['Amount'] = int(s) if s else 0

# Prepare civic_docs texts
docs_texts = [d.get('text','').lower() for d in civic_docs]

# Keywords to detect disaster-related projects
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'fema/caloes', 'fema/']

included_records = []

for fr in funding:
    pname = fr.get('Project_Name','')
    pname_l = pname.lower()
    amount = fr.get('Amount',0)
    found_in_doc = False
    started_2022 = False
    disaster_context = False

    # Search each civic doc for project name
    for doc_text in docs_texts:
        if pname_l in doc_text:
            found_in_doc = True
            # find index of occurrence
            idx = doc_text.find(pname_l)
            start = max(0, idx-500)
            end = min(len(doc_text), idx+500)
            window = doc_text[start:end]
            # Check for '2022' in window or doc
            if '2022' in window or '2022' in doc_text:
                started_2022 = True
            # Check for disaster keywords in window or doc
            for kw in disaster_keywords:
                if kw in window or kw in doc_text:
                    disaster_context = True
                    break
            # if both found, we can include
            if started_2022 and disaster_context:
                included_records.append({'Project_Name': pname, 'Amount': amount})
                break
    # If project name not found in docs, but name itself contains disaster keyword and any civic doc contains '2022',
    # we can attempt to include if there is evidence of 2022 in docs generally.
    if not found_in_doc:
        name_has_disaster_kw = any(kw in pname_l for kw in disaster_keywords)
        any_doc_has_2022 = any('2022' in dt for dt in docs_texts)
        any_doc_has_disaster = any(any(kw in dt for kw in disaster_keywords) for dt in docs_texts)
        if name_has_disaster_kw and any_doc_has_2022 and any_doc_has_disaster:
            included_records.append({'Project_Name': pname, 'Amount': amount})

# Remove duplicates (by Project_Name and Amount)
unique = {}
for rec in included_records:
    key = (rec['Project_Name'], rec['Amount'])
    unique[key] = rec
included_list = list(unique.values())

total = sum(r['Amount'] for r in included_list)

# Prepare result dict
result = {'total_funding_for_disaster_projects_started_2022': total, 'projects_included': included_list}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xHTQYwVDgsOGMdNJNzehcdiQ': 'file_storage/call_xHTQYwVDgsOGMdNJNzehcdiQ.json', 'var_call_ucr9bvHA93EHNq2cqRusfhzm': 'file_storage/call_ucr9bvHA93EHNq2cqRusfhzm.json'}

exec(code, env_args)
