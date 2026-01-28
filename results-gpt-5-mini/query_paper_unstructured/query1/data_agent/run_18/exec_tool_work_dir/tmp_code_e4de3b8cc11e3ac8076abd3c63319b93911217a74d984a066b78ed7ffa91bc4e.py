code = """import json
import pandas as pd

# Load the large MongoDB query result (file path stored in var_call_vJEnRVZLWiPPXqCDublUOayL)
with open(var_call_vJEnRVZLWiPPXqCDublUOayL, 'r') as f:
    docs = json.load(f)

# Load the aggregated citations result (file path stored in var_call_XW6s89GG8j4LXX2DC6DAAHBg)
with open(var_call_XW6s89GG8j4LXX2DC6DAAHBg, 'r') as f:
    cites = json.load(f)

# Create DataFrames
df_docs = pd.DataFrame(docs)
df_cites = pd.DataFrame(cites)

# Normalize and extract title from filename
if 'filename' in df_docs.columns:
    df_docs['title'] = df_docs['filename'].str.replace(r"\.txt$", '', regex=True)
else:
    df_docs['title'] = ''

# Ensure citation counts are integers
if 'total_citations' in df_cites.columns:
    df_cites['total_citations'] = df_cites['total_citations'].astype(int)
else:
    df_cites['total_citations'] = 0

# Define patterns indicative of the 'food' domain
patterns = ['food', 'diet', 'eat', 'eating', 'nutrition', 'calorie', 'meal', 'meals', 'food journal', 'journaled food', 'restaurant', 'dish', 'cuisine', 'snack']

# Lowercase text and check for any pattern
if 'text' in df_docs.columns:
    df_docs['text_lc'] = df_docs['text'].fillna('').str.lower()
else:
    df_docs['text_lc'] = ''

def contains_food(text):
    return any(p in text for p in patterns)

df_docs['domain_food'] = df_docs['text_lc'].apply(contains_food)

# Merge documents flagged as food domain with citation totals
df_food = df_docs[df_docs['domain_food']]
merged = pd.merge(df_food[['title']], df_cites, on='title', how='inner')

total_citations = int(merged['total_citations'].sum()) if not merged.empty else 0

import json as _json
result = _json.dumps({"domain": "food", "total_citations": total_citations})

# PRINT FORMAT
print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
print(f"print('{result}')")
print("----END PRINT FORMAT----")"""

env_args = {'var_call_CHGBb7wafAe7T30o4R6pbP4Q': ['paper_docs'], 'var_call_vJEnRVZLWiPPXqCDublUOayL': 'file_storage/call_vJEnRVZLWiPPXqCDublUOayL.json', 'var_call_RZ0gmVCoq0KvWJYcrBcV9ICO': ['Citations', 'sqlite_sequence'], 'var_call_XW6s89GG8j4LXX2DC6DAAHBg': 'file_storage/call_XW6s89GG8j4LXX2DC6DAAHBg.json'}

exec(code, env_args)
