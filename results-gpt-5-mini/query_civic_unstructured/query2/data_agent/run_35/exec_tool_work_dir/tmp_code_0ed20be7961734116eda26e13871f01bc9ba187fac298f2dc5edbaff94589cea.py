code = """import json
import pandas as pd

# Load tool results from storage file paths
with open(var_call_3UC3YtgdzesXLula5V5ZNc60, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)
with open(var_call_04JAjPhfCf3YfqX7uvRX4hOy, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Park-related funding rows by project name
park_rows = funding_df[funding_df['Project_Name'].str.lower().str.contains('park') | funding_df['Project_Name'].str.lower().str.contains('playground')]

# Lowercase civic texts
texts = [doc.get('text','').lower() for doc in civic_docs]

matched = []
for _, row in park_rows.iterrows():
    pname = row['Project_Name']
    pname_l = pname.lower()
    found = False
    for text in texts:
        idx = text.find(pname_l)
        if idx != -1:
            start = max(0, idx-200)
            end = min(len(text), idx+200)
            window = text[start:end]
            if 'completed' in window and '2022' in window:
                matched.append({'Project_Name': pname, 'Amount': int(row['Amount'])})
                found = True
                break
    # If not found by exact name, try a looser check: look for key suffixes like 'bluffs park', 'malibu park', 'legacy park', 'playground' near 'completed' and '2022'
    if not found:
        keywords = []
        if 'bluffs' in pname_l:
            keywords.append('bluffs park')
        if 'legacy' in pname_l:
            keywords.append('legacy park')
        if 'malibu park' in pname_l:
            keywords.append('malibu park')
        if 'playground' in pname_l:
            keywords.append('playground')
        for text in texts:
            for kw in keywords:
                idx2 = text.find(kw)
                if idx2 != -1:
                    start = max(0, idx2-200)
                    end = min(len(text), idx2+200)
                    window = text[start:end]
                    if 'completed' in window and '2022' in window:
                        matched.append({'Project_Name': pname, 'Amount': int(row['Amount'])})
                        found = True
                        break
            if found:
                break

# Remove duplicates
unique = {}
for m in matched:
    unique[m['Project_Name']] = unique.get(m['Project_Name'], 0) + m['Amount']

total = sum(unique.values())

output = {'matched_projects': [{'Project_Name': k, 'Amount': v} for k,v in unique.items()], 'total_funding': int(total)}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_04JAjPhfCf3YfqX7uvRX4hOy': 'file_storage/call_04JAjPhfCf3YfqX7uvRX4hOy.json', 'var_call_3UC3YtgdzesXLula5V5ZNc60': 'file_storage/call_3UC3YtgdzesXLula5V5ZNc60.json'}

exec(code, env_args)
