code = """import json
import pandas as pd

# Load the previous tool results from storage file paths
with open(var_call_3UC3YtgdzesXLula5V5ZNc60, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

with open(var_call_04JAjPhfCf3YfqX7uvRX4hOy, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Create DataFrame for funding
funding_df = pd.DataFrame(funding_records)
# Ensure Amount is int
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Prepare civic document texts
texts = [doc.get('text','').lower() for doc in civic_docs]

# Identify park-related funding project names
def is_park_related(name):
    name_l = name.lower()
    keywords = ['park', 'playground']
    return any(k in name_l for k in keywords)

park_funding = funding_df[funding_df['Project_Name'].apply(is_park_related)].copy()

matched = []

for _, row in park_funding.iterrows():
    pname = row['Project_Name']
    pname_l = pname.lower()
    found = False
    context_snippet = None
    for text in texts:
        idx = text.find(pname_l)
        if idx != -1:
            # look for 'completed' and '2022' in a window around the mention
            start = max(0, idx-300)
            end = min(len(text), idx+300)
            window = text[start:end]
            if ('completed' in window) and ('2022' in window):
                found = True
                # capture a bit more context for verification
                context_snippet = window.replace('\n',' ')[:500]
                break
    if found:
        matched.append({'Project_Name': pname, 'Amount': int(row['Amount']), 'context': context_snippet})

# Additionally, check for park projects mentioned in civic docs that might not match funding names exactly
# (e.g., project name in funding could be slightly different). We'll also scan civic docs for lines mentioning 'park' and 'completed' and '2022', then try to fuzzy-match to funding names by substring overlap.
import re
park_mentions = set()
for text in texts:
    # find sentences or fragments that include 'park' and 'completed' and '2022'
    if 'park' in text and 'completed' in text and '2022' in text:
        # extract fragments around these occurrences
        for m in re.finditer(r"([^.\n]{0,120}park[^.\n]{0,120}completed[^.\n]{0,120}2022[^.\n]{0,120})", text):
            frag = m.group(1)
            park_mentions.add(frag.strip())

# Try to map these fragments to funding project names by checking if funding name words appear in fragment
additional_matches = []
for frag in park_mentions:
    for pname in park_funding['Project_Name'].unique():
        pname_l = pname.lower()
        # use simple check: all words with length>3 in pname appear in frag
        words = [w for w in re.split(r"\W+", pname_l) if len(w)>3]
        if words and all(w in frag for w in words):
            # find all funding rows with this pname and add if not already added
            rows = funding_df[funding_df['Project_Name']==pname]
            for _, r in rows.iterrows():
                if not any(m['Project_Name']==pname and m['Amount']==int(r['Amount']) for m in matched):
                    matched.append({'Project_Name': pname, 'Amount': int(r['Amount']), 'context': frag})

# Compute total funding
total = sum(m['Amount'] for m in matched)

# Prepare output
output = {'matched_projects': matched, 'total_funding': int(total)}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_04JAjPhfCf3YfqX7uvRX4hOy': 'file_storage/call_04JAjPhfCf3YfqX7uvRX4hOy.json', 'var_call_3UC3YtgdzesXLula5V5ZNc60': 'file_storage/call_3UC3YtgdzesXLula5V5ZNc60.json'}

exec(code, env_args)
