code = """import json, re, pandas as pd
# Load results from previous tool calls (file paths are provided in the variables)
path_mongo = var_call_Q6Is5ZqdpmLF9IhXls8SGIUT
path_sql = var_call_NoULbuVXj56umJ20Cmv1uAzM

with open(path_mongo, 'r', encoding='utf-8') as f:
    mongo = json.load(f)
with open(path_sql, 'r', encoding='utf-8') as f:
    cit = json.load(f)

# Create DataFrames
df_m = pd.DataFrame(mongo)
df_c = pd.DataFrame(cit)

# Derive title from filename
if 'filename' in df_m.columns:
    df_m['title'] = df_m['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_m['title'] = ''

# Lowercase text and filename for searching
df_m['text_lower'] = df_m.get('text', pd.Series(['']*len(df_m))).fillna('').astype(str).str.lower()
if 'filename' in df_m.columns:
    df_m['filename_lower'] = df_m['filename'].fillna('').astype(str).str.lower()
else:
    df_m['filename_lower'] = ''

# Identify papers in the 'food' domain by searching for the word 'food' in text or filename
df_m['is_food'] = df_m['text_lower'].str.contains(r"\bfood\b") | df_m['filename_lower'].str.contains(r"\bfood\b")

# Prepare citations DataFrame: ensure numeric
if 'total_citations' in df_c.columns:
    df_c['total_citations'] = pd.to_numeric(df_c['total_citations'], errors='coerce').fillna(0).astype(int)
else:
    df_c['total_citations'] = 0

# Merge on title
df_join = pd.merge(df_m[['title', 'is_food']], df_c, on='title', how='inner')

# Sum citations for papers marked as food
food_citations = int(df_join.loc[df_join['is_food'] == True, 'total_citations'].sum())

# Also capture which titles were counted (for transparency in results structure)
food_titles = df_join.loc[df_join['is_food'] == True, 'title'].tolist()

output = {"domain": "food", "total_citations": food_citations, "titles_counted": food_titles}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_vivdb7DD4eO02aVnh0LeE7v0': ['paper_docs'], 'var_call_Q6Is5ZqdpmLF9IhXls8SGIUT': 'file_storage/call_Q6Is5ZqdpmLF9IhXls8SGIUT.json', 'var_call_NoULbuVXj56umJ20Cmv1uAzM': 'file_storage/call_NoULbuVXj56umJ20Cmv1uAzM.json'}

exec(code, env_args)
