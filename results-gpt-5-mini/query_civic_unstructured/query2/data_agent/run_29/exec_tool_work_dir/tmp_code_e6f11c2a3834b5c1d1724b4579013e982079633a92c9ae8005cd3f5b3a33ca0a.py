code = """import json
import pandas as pd

# Load the large results from storage file paths provided by previous query_db calls
with open(var_call_k503RNWsWEIoJhv6e9ZIANHv, 'r') as f:
    funding_records = json.load(f)
with open(var_call_K6d2FtvJxFYaKDbpWj0ccywA, 'r') as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_records)
# Normalize Amount to int
funding_df['Amount'] = funding_df['Amount'].astype(int)

matched = []

for _, row in funding_df.iterrows():
    proj = row['Project_Name']
    proj_low = proj.lower()
    amount = int(row['Amount'])
    # Search through all civic documents for evidence project was completed in 2022
    found = False
    for doc in civic_docs:
        text = doc.get('text','')
        text_low = text.lower()
        if proj_low in text_low and '2022' in text_low:
            # require mention of completion
            if 'completed' in text_low or 'completion' in text_low or 'notice of completion' in text_low:
                found = True
                break
    if found:
        matched.append({
            'Project_Name': proj,
            'Amount': amount
        })

total = sum(m['Amount'] for m in matched)

result = {
    'total_funding_for_park_related_projects_completed_in_2022': total,
    'matched_projects': matched
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_K6d2FtvJxFYaKDbpWj0ccywA': 'file_storage/call_K6d2FtvJxFYaKDbpWj0ccywA.json', 'var_call_k503RNWsWEIoJhv6e9ZIANHv': 'file_storage/call_k503RNWsWEIoJhv6e9ZIANHv.json'}

exec(code, env_args)
