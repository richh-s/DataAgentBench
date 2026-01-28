code = """import json
import pandas as pd

# Load the MongoDB paper_docs query result (stored in a .json file path)
with open(var_call_4zP0P2cfI6DrneygeIiLl1ty, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load the aggregated citations result (stored in a .json file path)
with open(var_call_mHTuwr86OSxECQPUOUW4ZTxx, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Create DataFrame for documents
df_docs = pd.DataFrame(docs)
# Extract title from filename by removing trailing .txt if present
df_docs['title'] = df_docs['filename'].str.replace(r"\.txt$", '', regex=True)
# Lowercase text for matching
df_docs['text_lower'] = df_docs['text'].str.lower().fillna('')
# Determine food domain: if 'food' appears in text or title
df_docs['is_food_domain'] = df_docs['text_lower'].str.contains('food') | df_docs['title'].str.lower().str.contains('food')

# Titles identified as food domain
food_titles = set(df_docs.loc[df_docs['is_food_domain'], 'title'].tolist())

# Create DataFrame for citations
df_c = pd.DataFrame(citations)
# Ensure total_citations is integer
df_c['total_citations'] = df_c['total_citations'].astype(int)

# Filter citations for titles in food domain
df_food_citations = df_c[df_c['title'].isin(food_titles)]

# Compute total citation count
total_citations_food = int(df_food_citations['total_citations'].sum())

import json
print("__RESULT__:")
print(json.dumps({"total_citations_food": total_citations_food}))"""

env_args = {'var_call_ndvWwJjXqKPDulQiUL7SiHfR': ['paper_docs'], 'var_call_zP7A8fyjFaHWWtT0lDdBp0F4': ['Citations', 'sqlite_sequence'], 'var_call_4zP0P2cfI6DrneygeIiLl1ty': 'file_storage/call_4zP0P2cfI6DrneygeIiLl1ty.json', 'var_call_mHTuwr86OSxECQPUOUW4ZTxx': 'file_storage/call_mHTuwr86OSxECQPUOUW4ZTxx.json'}

exec(code, env_args)
