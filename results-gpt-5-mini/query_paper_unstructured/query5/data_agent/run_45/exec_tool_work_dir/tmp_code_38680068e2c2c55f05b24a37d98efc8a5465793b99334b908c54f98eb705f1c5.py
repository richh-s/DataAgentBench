code = """import json
import pandas as pd
import re

# Load citations data
data_citations = None
if isinstance(var_call_4EFqrNYfrs8yFpChOBcDWvsl, str):
    with open(var_call_4EFqrNYfrs8yFpChOBcDWvsl, 'r', encoding='utf-8') as f:
        data_citations = json.load(f)
else:
    data_citations = var_call_4EFqrNYfrs8yFpChOBcDWvsl

# Load paper docs data
data_papers = None
if isinstance(var_call_2yhsNBZQnu2ffxQCZqh7e4hH, str):
    with open(var_call_2yhsNBZQnu2ffxQCZqh7e4hH, 'r', encoding='utf-8') as f:
        data_papers = json.load(f)
else:
    data_papers = var_call_2yhsNBZQnu2ffxQCZqh7e4hH

# Create DataFrames
df_cit = pd.DataFrame(data_citations)
# Ensure proper types
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# Papers: extract title from filename
df_p = pd.DataFrame(data_papers)
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r"\.txt$", '', regex=True)
else:
    df_p['title'] = ''
# Detect CHI venue: look for 'CHI' as a word in the text (common header like "CHI '15")
if 'text' in df_p.columns:
    df_p['is_chi'] = df_p['text'].fillna('').str.contains(r"\bCHI\b", regex=True)
else:
    df_p['is_chi'] = False

# Filter to CHI papers
df_chi = df_p[df_p['is_chi']][['title']].drop_duplicates()

# Join with citations for 2020 (var_call_4EF... already filtered by citation_year in the SQL query)
merged = pd.merge(df_cit, df_chi, on='title', how='inner')

total_citations = int(merged['citation_count'].sum())
num_papers = int(len(merged))

result = {
    'total_citations': total_citations,
    'num_papers': num_papers
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4EFqrNYfrs8yFpChOBcDWvsl': 'file_storage/call_4EFqrNYfrs8yFpChOBcDWvsl.json', 'var_call_JJ4mKnI7jt2F0rjjoG3g96oU': ['paper_docs'], 'var_call_2yhsNBZQnu2ffxQCZqh7e4hH': 'file_storage/call_2yhsNBZQnu2ffxQCZqh7e4hH.json'}

exec(code, env_args)
