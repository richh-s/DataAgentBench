code = """import json
import pandas as pd

# Load file paths from previous tool results
path_docs = var_call_vJEnRVZLWiPPXqCDublUOayL
path_cites = var_call_XW6s89GG8j4LXX2DC6DAAHBg

# Read JSON files
with open(path_docs, 'r') as f:
    docs = json.load(f)
with open(path_cites, 'r') as f:
    cites = json.load(f)

# DataFrames
df_docs = pd.DataFrame(docs)
df_cites = pd.DataFrame(cites)

# Extract title from filename
if 'filename' in df_docs.columns:
    df_docs['title'] = df_docs['filename'].str.replace('\\.txt$', '', regex=True)
else:
    df_docs['title'] = ''

# Ensure citation counts are integers
if 'total_citations' in df_cites.columns:
    df_cites['total_citations'] = df_cites['total_citations'].astype(int)
else:
    df_cites['total_citations'] = 0

# Patterns for food domain
patterns = ['food', 'diet', 'eat', 'eating', 'nutrition', 'calorie', 'meal', 'meals', 'food journal', 'journaled food', 'restaurant', 'dish', 'cuisine', 'snack']

# Lowercase text
if 'text' in df_docs.columns:
    df_docs['text_lc'] = df_docs['text'].fillna('').str.lower()
else:
    df_docs['text_lc'] = ''

# Function to check for any pattern
def contains_food(text):
    for p in patterns:
        if p in text:
            return True
    return False

# Flag food domain
df_docs['domain_food'] = df_docs['text_lc'].apply(contains_food)

# Select food domain docs
df_food = df_docs[df_docs['domain_food']]

# Merge with citation totals
merged = pd.merge(df_food[['title']], df_cites, on='title', how='inner')

# Sum citations
total_citations = int(merged['total_citations'].sum()) if not merged.empty else 0

result = json.dumps({"domain": "food", "total_citations": total_citations})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_CHGBb7wafAe7T30o4R6pbP4Q': ['paper_docs'], 'var_call_vJEnRVZLWiPPXqCDublUOayL': 'file_storage/call_vJEnRVZLWiPPXqCDublUOayL.json', 'var_call_RZ0gmVCoq0KvWJYcrBcV9ICO': ['Citations', 'sqlite_sequence'], 'var_call_XW6s89GG8j4LXX2DC6DAAHBg': 'file_storage/call_XW6s89GG8j4LXX2DC6DAAHBg.json'}

exec(code, env_args)
