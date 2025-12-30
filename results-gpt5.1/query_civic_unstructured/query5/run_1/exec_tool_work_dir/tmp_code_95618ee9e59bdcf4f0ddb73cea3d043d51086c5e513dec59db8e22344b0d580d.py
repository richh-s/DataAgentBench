code = """import json, re, pandas as pd

with open(var_call_mhiHbzpEIElwM0PFZbXrbqMQ, 'r') as f:
    civic_docs = json.load(f)
texts = ' '.join(doc['text'] for doc in civic_docs)

with open(var_call_vjGUf8GChnY2WpqhvXFxVyEW, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

mask_disaster = fund_df['Project_Name'].str.contains('FEMA', case=False) | \
                fund_df['Project_Name'].str.contains('CalOES', case=False) | \
                fund_df['Project_Name'].str.contains('CalJPIA', case=False) | \
                fund_df['Project_Name'].str.contains('Disaster', case=False) | \
                fund_df['Project_Name'].str.contains('Recovery', case=False)

text_lower = texts.lower()

def started_2022(name):
    n_low = name.lower()
    idx = text_lower.find(n_low)
    if idx == -1:
        return False
    window = text_lower[max(0, idx-100): idx+len(n_low)+100]
    return '2022' in window

fund_df['is_disaster'] = mask_disaster
fund_df['started_2022'] = fund_df.apply(lambda r: started_2022(r['Project_Name']) if r['is_disaster'] else False, axis=1)

subset = fund_df[fund_df['is_disaster'] & fund_df['started_2022']]

total = int(subset['Amount'].sum())

result = {"total_disaster_funding_started_2022": total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mhiHbzpEIElwM0PFZbXrbqMQ': 'file_storage/call_mhiHbzpEIElwM0PFZbXrbqMQ.json', 'var_call_vjGUf8GChnY2WpqhvXFxVyEW': 'file_storage/call_vjGUf8GChnY2WpqhvXFxVyEW.json'}

exec(code, env_args)
