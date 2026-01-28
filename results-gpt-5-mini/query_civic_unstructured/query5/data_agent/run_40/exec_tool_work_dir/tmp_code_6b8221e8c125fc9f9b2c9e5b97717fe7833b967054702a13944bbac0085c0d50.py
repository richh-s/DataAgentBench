code = """import json
import re
import pandas as pd

# Load data from previous tool calls (file paths are stored in these variables)
with open(var_call_KP05Q7S0PO433HfJ0t0pGS0A, 'r') as f:
    funding_records = json.load(f)
with open(var_call_MzOq5uyisfIvVdZH1y0R5oBS, 'r') as f:
    civic_docs = json.load(f)

# Create DataFrame for funding
funding_df = pd.DataFrame(funding_records)
# Ensure Amount is int
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Prepare civic texts
docs_texts = [doc.get('text','') for doc in civic_docs]

# Disaster keywords
disaster_keywords = ['fema','caloes','calo es','caljpia','disaster','fire','woolsey','emergency','federal assistance','cal o es']

matched_rows = []

for idx, row in funding_df.iterrows():
    name = row['Project_Name']
    amount = int(row['Amount'])
    name_lower = name.lower()
    base_name = re.sub(r"\s*\(.*\)", "", name).strip().lower()
    found = False
    year2022 = False
    disaster = False

    for text in docs_texts:
        t_lower = text.lower()
        # try full name
        m = re.search(re.escape(name_lower), t_lower)
        if not m:
            m = re.search(re.escape(base_name), t_lower)
        if not m:
            continue
        found = True
        # window around match
        start = max(0, m.start() - 400)
        end = min(len(t_lower), m.end() + 400)
        window = t_lower[start:end]
        # check year 2022 in window or in whole doc
        if '2022' in window or '2022' in t_lower:
            year2022 = True
        # check disaster keywords in window or project name
        for kw in disaster_keywords:
            if kw in window or kw in name_lower or kw in base_name:
                disaster = True
                break
        # also check if document header mentions 'disaster recovery'
        if not disaster and 'disaster recovery' in t_lower:
            disaster = True
        if found and year2022 and disaster:
            matched_rows.append({'Project_Name': name, 'Amount': amount})
            break

# Sum amounts
total = sum(r['Amount'] for r in matched_rows)

# For debugging we could also list matched projects, but only need total

import json
print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_call_KP05Q7S0PO433HfJ0t0pGS0A': 'file_storage/call_KP05Q7S0PO433HfJ0t0pGS0A.json', 'var_call_wb699j7GKVODuIZGnebrIgjF': ['civic_docs'], 'var_call_MzOq5uyisfIvVdZH1y0R5oBS': 'file_storage/call_MzOq5uyisfIvVdZH1y0R5oBS.json'}

exec(code, env_args)
