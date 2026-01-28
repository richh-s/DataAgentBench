code = """import json
import re
import pandas as pd

business_file = var_call_glKA8W8O9XQpL6skMLeTPrBG
review_file = var_call_Yq9r2lFTFDEhJb5LK7Hi8IAf

with open(business_file, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(review_file, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Try different regex patterns to extract state
patterns = [r"in\s+([A-Za-z .'-]+),\s*([A-Z]{2})\b", r"\b([A-Za-z .'-]+),\s*([A-Z]{2})\b", r"in\s+[0-9]+\s+[A-Za-z .'-]+,\s*([A-Z]{2})\b"]

extracted = []
for desc in df_b['description'].astype(str):
    found = None
    for p in patterns:
        m = re.search(p, desc)
        if m:
            # If pattern has city and state or only state group varies
            if m.lastindex >= 2:
                state = m.group(2)
            else:
                state = m.group(1)
            found = state
            break
    extracted.append(found)

df_b['state_try'] = extracted

# Count non-null
state_counts = df_b['state_try'].notna().sum()
unique_states = sorted(df_b['state_try'].dropna().unique().tolist())

# Prepare a sample of descriptions without extracted state
no_state_samples = df_b[df_b['state_try'].isna()].head(10)['description'].tolist()

out = {
    'nonnull_count': int(state_counts),
    'unique_states': unique_states,
    'no_state_samples': no_state_samples
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_glKA8W8O9XQpL6skMLeTPrBG': 'file_storage/call_glKA8W8O9XQpL6skMLeTPrBG.json', 'var_call_Yq9r2lFTFDEhJb5LK7Hi8IAf': 'file_storage/call_Yq9r2lFTFDEhJb5LK7Hi8IAf.json', 'var_call_HxpbTYuyfCLvCURVDJsrjBQ2': {'state': None, 'total_reviews': 0, 'avg_rating': None}}

exec(code, env_args)
