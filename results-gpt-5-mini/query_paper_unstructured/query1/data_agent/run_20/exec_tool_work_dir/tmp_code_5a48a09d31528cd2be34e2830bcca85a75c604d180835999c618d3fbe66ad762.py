code = """import json
import pandas as pd
# Load the JSON results from previous tool calls (file paths are provided in the variables)
with open(var_call_fxpX04oADNc1fZkJhMdEJ2iZ, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(var_call_GuU3TfiC8kY2GW0id1cUpjEn, 'r', encoding='utf-8') as f:
    citations = json.load(f)
# Build dataframes
df_p = pd.DataFrame(papers)
if 'filename' not in df_p.columns:
    df_p['filename'] = ''
df_p['title'] = df_p['filename'].str.replace('\.txt$', '', regex=True)
if 'text' not in df_p.columns:
    df_p['text'] = ''
df_p['text'] = df_p['text'].fillna('').astype(str)
# Mark food domain by substring matching for 'food' in text or title (case-insensitive)
df_p['is_food'] = df_p['text'].str.lower().str.contains('food') | df_p['title'].str.lower().str.contains('food')
# Citations dataframe
df_c = pd.DataFrame(citations)
if 'citation_count' not in df_c.columns:
    df_c['citation_count'] = 0
if 'title' not in df_c.columns:
    df_c['title'] = ''
# Convert citation_count to numeric
df_c['citation_count'] = pd.to_numeric(df_c['citation_count'], errors='coerce').fillna(0).astype(int)
# Merge on title and sum citation_count for papers marked as food
df_merged = df_c.merge(df_p[['title', 'is_food']], on='title', how='left')
df_merged['is_food'] = df_merged['is_food'].fillna(False)
total_citations = int(df_merged.loc[df_merged['is_food'], 'citation_count'].sum())
# Print result in required format
print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_call_fxpX04oADNc1fZkJhMdEJ2iZ': 'file_storage/call_fxpX04oADNc1fZkJhMdEJ2iZ.json', 'var_call_GuU3TfiC8kY2GW0id1cUpjEn': 'file_storage/call_GuU3TfiC8kY2GW0id1cUpjEn.json'}

exec(code, env_args)
