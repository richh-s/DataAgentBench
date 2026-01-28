code = """import json
import pandas as pd

# Load tool results from storage file paths provided
with open(var_call_3UC3YtgdzesXLula5V5ZNc60, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

with open(var_call_04JAjPhfCf3YfqX7uvRX4hOy, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# DataFrame for funding
funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Lowercase civic texts
texts = [doc.get('text','').lower() for doc in civic_docs]

# Select funding rows that are park-related by project name
def is_park_related(name):
    nl = name.lower()
    return ('park' in nl) or ('playground' in nl)

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
            start = max(0, idx-300)
            end = min(len(text), idx+300)
            window = text[start:end]
            if ('completed' in window) and ('2022' in window):
                found = True
                context_snippet = window.replace('\n', ' ')[:500]
                break
    if found:
        matched.append({'Project_Name': pname, 'Amount': int(row['Amount']), 'context': context_snippet})

# Additionally, find generic park mentions that include 'completed' and '2022'
import re
park_fragments = set()
for text in texts:
    if 'park' in text and 'completed' in text and '2022' in text:
        # extract fragments around 'park' occurrences
        for m in re.finditer(r"(.{0,120}park.{0,120}completed.{0,120}2022.{0,120})", text):
            frag = m.group(1)
            park_fragments.add(frag.strip())

# Try to match fragments to funding project names not already matched
for frag in park_fragments:
    frag_l = frag
    for _, r in funding_df.iterrows():
        pname = r['Project_Name']
        pname_l = pname.lower()
        if is_park_related(pname) and pname_l not in [m['Project_Name'].lower() for m in matched]:
            # check if major words of pname appear in fragment
            words = [w for w in re.split(r'\W+', pname_l) if len(w) > 3]
            if words and all(w in frag_l for w in words):
                matched.append({'Project_Name': pname, 'Amount': int(r['Amount']), 'context': frag})

# Compute total
total = sum(m['Amount'] for m in matched)

output = {'matched_projects': matched, 'total_funding': int(total)}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_04JAjPhfCf3YfqX7uvRX4hOy': 'file_storage/call_04JAjPhfCf3YfqX7uvRX4hOy.json', 'var_call_3UC3YtgdzesXLula5V5ZNc60': 'file_storage/call_3UC3YtgdzesXLula5V5ZNc60.json'}

exec(code, env_args)
