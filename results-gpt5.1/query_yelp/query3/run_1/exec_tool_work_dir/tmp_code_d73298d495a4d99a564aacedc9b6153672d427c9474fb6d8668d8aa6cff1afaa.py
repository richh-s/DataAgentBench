code = """import json, pandas as pd
from pathlib import Path

# Load full results
review_path = Path(var_call_TfidTwfVZ3uQm8BvHrja5GoA)
tip_path = Path(var_call_4OuQj4VmeNlMUFt6yPlsJaOC)

review = json.loads(review_path.read_text())
tip = json.loads(tip_path.read_text())

rev_df = pd.DataFrame(review)
tip_df = pd.DataFrame(tip)

# Filter rows whose date string contains '2018'
rev_2018 = rev_df[rev_df['year'].str.contains('2018', na=False)]
tip_2018 = tip_df[tip_df['year'].str.contains('2018', na=False)]

# Businesses with any reviews or tips in 2018
biz_2018_refs = pd.unique(pd.concat([rev_2018['business_ref'], tip_2018['business_ref']], ignore_index=True))

# Convert to corresponding business_id keys
biz_2018_ids = pd.Series(biz_2018_refs).str.replace('businessref_', 'businessid_', regex=False).tolist()

result = json.dumps(biz_2018_ids)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_yp00JtDfbHhlgIJ7wZNlrnXl': 'file_storage/call_yp00JtDfbHhlgIJ7wZNlrnXl.json', 'var_call_TfidTwfVZ3uQm8BvHrja5GoA': 'file_storage/call_TfidTwfVZ3uQm8BvHrja5GoA.json', 'var_call_4OuQj4VmeNlMUFt6yPlsJaOC': 'file_storage/call_4OuQj4VmeNlMUFt6yPlsJaOC.json'}

exec(code, env_args)
