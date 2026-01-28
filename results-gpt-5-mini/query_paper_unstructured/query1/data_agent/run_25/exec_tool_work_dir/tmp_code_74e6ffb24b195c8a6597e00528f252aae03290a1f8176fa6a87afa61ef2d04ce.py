code = """import json
import pandas as pd

# Load the MongoDB query results (may be a file path or a list)
data_file = var_call_vVQLBPnDuT7bkj1my5o1Cs80
if isinstance(data_file, str):
    with open(data_file, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = data_file

# Load the SQLite query results
cit_file = var_call_i5mEZBDsfel1baPVrCppPtPC
if isinstance(cit_file, str):
    with open(cit_file, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = cit_file

# Create DataFrames
df_docs = pd.DataFrame(docs)
df_cits = pd.DataFrame(cits)

# Normalize and extract title from filename
if 'filename' in df_docs.columns:
    df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_docs['title'] = ''

# Lowercase text for matching
df_docs['text_l'] = df_docs.get('text', pd.Series([''] * len(df_docs))).fillna('').str.lower()

# Identify food-related papers using substring matching on text and filename
# Use a set of keywords to improve recall
import re
keywords_pattern = r"\b(food|meal|meals|eat|eating|nutrition|calori|diet|restaurant|foodjournal|food journal|food-tracking|food tracking)\b"

# Check in text and filename
df_docs['is_food'] = df_docs['text_l'].str.contains(keywords_pattern, regex=True, na=False) | df_docs['title'].str.lower().str.contains('food', na=False)

# Get set of titles for food domain
food_titles = set(df_docs.loc[df_docs['is_food'], 'title'].dropna().unique().tolist())

# Prepare citations dataframe: ensure citation_count numeric
if 'citation_count' in df_cits.columns:
    df_cits['citation_count'] = pd.to_numeric(df_cits['citation_count'], errors='coerce').fillna(0)
else:
    df_cits['citation_count'] = 0

# Sum citation_count for titles matching food_titles
total = int(df_cits[df_cits['title'].isin(food_titles)]['citation_count'].sum())

# Output result in required print format
import json
print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_call_BE9cVWVvvzJJoZmPVNfxmlXm': ['paper_docs'], 'var_call_vVQLBPnDuT7bkj1my5o1Cs80': 'file_storage/call_vVQLBPnDuT7bkj1my5o1Cs80.json', 'var_call_i5mEZBDsfel1baPVrCppPtPC': 'file_storage/call_i5mEZBDsfel1baPVrCppPtPC.json'}

exec(code, env_args)
