code = """import json
import re

# Load the civic docs query result from the storage file
with open(var_call_xJjYI40NMaXKKv53fJ94wWGY, 'r') as f:
    civic_docs = json.load(f)

# Load the funding table query result
with open(var_call_XOjgY5eEJox3E6EzKiSyKhMG, 'r') as f:
    funding_records = json.load(f)

# Prepare search tokens for Spring 2022
spring_tokens = [
    r"Spring\s*,?\s*2022",
    r"March\s+2022",
    r"Mar\.?\s+2022",
    r"April\s+2022",
    r"Apr\.?\s+2022",
    r"May\s+2022",
    r"03[\/-]2022",
    r"04[\/-]2022",
    r"05[\/-]2022",
    r"03[\/-]22",
    r"04[\/-]22",
    r"05[\/-]22",
]
spring_re = re.compile(r"(?:" + r"|".join(spring_tokens) + r")", flags=re.IGNORECASE)

matched_projects = set()
matched_rows = []
total_amount = 0

# Iterate over funding records and search for project name mentions in civic docs
for rec in funding_records:
    proj = rec.get('Project_Name', '')
    amt_raw = rec.get('Amount', 0)
    # normalize amount to int
    try:
        amt = int(float(str(amt_raw).replace(',', '')))
    except:
        amt = 0

    found_in_spring = False
    if not proj:
        continue
    proj_escaped = re.escape(proj)
    # search across all civic docs
    for doc in civic_docs:
        text = doc.get('text', '')
        # look for the project name in the text (case-insensitive)
        m = re.search(proj_escaped, text, flags=re.IGNORECASE)
        if m:
            # get context around match
            start = max(0, m.start() - 250)
            end = min(len(text), m.end() + 250)
            context = text[start:end]
            # check if any spring token is in the context
            if spring_re.search(context):
                found_in_spring = True
                break
    if found_in_spring:
        matched_projects.add(proj)
        matched_rows.append({'Project_Name': proj, 'Amount': amt})
        total_amount += amt

result = {
    'count_unique_projects': len(matched_projects),
    'total_funding': total_amount,
    'projects': sorted(list(matched_projects))
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cTBTY6S9iKKD4BWwxdXVS6eY': ['civic_docs'], 'var_call_Fv8fJWtheNTSd4rwDlmwwbUe': ['Funding'], 'var_call_xJjYI40NMaXKKv53fJ94wWGY': 'file_storage/call_xJjYI40NMaXKKv53fJ94wWGY.json', 'var_call_XOjgY5eEJox3E6EzKiSyKhMG': 'file_storage/call_XOjgY5eEJox3E6EzKiSyKhMG.json'}

exec(code, env_args)
