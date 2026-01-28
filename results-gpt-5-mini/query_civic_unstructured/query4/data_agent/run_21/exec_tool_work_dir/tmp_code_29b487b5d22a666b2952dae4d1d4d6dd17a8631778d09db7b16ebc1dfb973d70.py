code = """import json
import pandas as pd
import re

# Load previous tool results from storage variables
# var_call_UwWh34q9U1qqpucR050BWqoV and var_call_0EoTJFoP1Jo92FvXtBjJpFfQ

with open(var_call_UwWh34q9U1qqpucR050BWqoV, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_0EoTJFoP1Jo92FvXtBjJpFfQ, 'r') as f:
    funding_records = json.load(f)

# Create DataFrame for funding
fund_df = pd.DataFrame(funding_records)
# Ensure Amount is integer
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Prepare spring 2022 keywords
spring_keywords = [
    'spring 2022', '2022-spring', 'spring, 2022', 'spring 22',
    'march 2022', 'mar 2022', '2022 march', '03-2022', '03/2022', '2022-03', '2022.03',
    'april 2022', 'apr 2022', '2022 april', '04-2022', '04/2022', '2022-04', '2022.04',
    'may 2022', 'may, 2022', '05-2022', '05/2022', '2022-05', '2022.05'
]

# Lowercase keywords for comparison
spring_keywords = [k.lower() for k in spring_keywords]

# Build a single large text per document
docs = []
for d in civic_docs:
    text = d.get('text','')
    filename = d.get('filename','')
    docs.append({'filename': filename, 'text': text, 'text_lower': text.lower()})

# For each project in funding, check if it appears in any civic doc near a spring 2022 keyword
matched_projects = set()

for proj in fund_df['Project_Name'].unique():
    proj_lower = proj.lower()
    for doc in docs:
        txt = doc['text_lower']
        idx = txt.find(proj_lower)
        if idx != -1:
            # get context window
            start = max(0, idx-300)
            end = min(len(txt), idx + len(proj_lower) + 300)
            window = txt[start:end]
            # check for any spring keyword in window
            if any(k in window for k in spring_keywords):
                matched_projects.add(proj)
                break
            # also check entire document as fallback
            if any(k in txt for k in spring_keywords):
                # ensure the keywords appear after or near; still count
                matched_projects.add(proj)
                break

# Now compute count and total funding for matched projects
matched_list = sorted(list(matched_projects))
count = len(matched_list)

if count > 0:
    total_funding = int(fund_df[fund_df['Project_Name'].isin(matched_list)]['Amount'].sum())
else:
    total_funding = 0

result = {'count': count, 'total_funding': total_funding, 'projects': matched_list}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_UwWh34q9U1qqpucR050BWqoV': 'file_storage/call_UwWh34q9U1qqpucR050BWqoV.json', 'var_call_0EoTJFoP1Jo92FvXtBjJpFfQ': 'file_storage/call_0EoTJFoP1Jo92FvXtBjJpFfQ.json'}

exec(code, env_args)
