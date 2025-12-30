code = """import json, pandas as pd

# Load full funding data
path_funding = var_call_o8kHuEuEWHyWSKN5viGVF820
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Load civic docs with emergency/FEMA mentions
path_docs = var_call_TuIfdLmGtMLHatQfg1trRwZc
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Very simple heuristic: any project whose name contains 'FEMA' or 'Warning' or 'Emergency'
# will be considered related to emergency/FEMA. In a more advanced setup, we'd parse docs,
# but here we align by Project_Name substrings.

funding_df = pd.DataFrame(funding)

mask = funding_df['Project_Name'].str.contains('FEMA', case=False, na=False) \
       | funding_df['Project_Name'].str.contains('emergency', case=False, na=False) \
       | funding_df['Project_Name'].str.contains('Warning', case=False, na=False)

related = funding_df[mask].copy()

# From docs, try to get statuses for these project names by simple substring search
results = []
for _, row in related.iterrows():
    pname = row['Project_Name']
    status = None
    topic = None
    # simple heuristic: look for 'design', 'completed', 'not started' near project name in any doc
    for doc in docs:
        text = doc['text']
        if pname.split(' (')[0] in text:
            lower = text.lower()
            idx = lower.find(pname.split(' (')[0].lower())
            window = lower[max(0, idx-300): idx+300]
            if 'completed' in window:
                status = 'completed'
            elif 'not started' in window:
                status = 'not started'
            elif 'design' in window:
                status = 'design'
            # topics: emergency, fema, warning
            topics = []
            for kw in ['emergency','fema','warning']:
                if kw in window:
                    topics.append(kw)
            if topics:
                topic = ', '.join(sorted(set(topics)))
            if status or topic:
                break
    results.append({
        'Project_Name': pname,
        'Funding_Source': row['Funding_Source'],
        'Amount': int(row['Amount']),
        'Status': status if status else 'unknown'
    })

out = json.dumps(results)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_o8kHuEuEWHyWSKN5viGVF820': 'file_storage/call_o8kHuEuEWHyWSKN5viGVF820.json', 'var_call_TuIfdLmGtMLHatQfg1trRwZc': 'file_storage/call_TuIfdLmGtMLHatQfg1trRwZc.json'}

exec(code, env_args)
