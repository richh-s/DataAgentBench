code = """import json
import pandas as pd

# Load previous tool results from storage file paths
with open(var_call_FKaO08dCZpqBJ2LEg9OQmRxN, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_aj5SZDAQkKmoeos4mGeb2lF9, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Create DataFrames
df_cit = pd.DataFrame(citations)
# Ensure citation_count numeric
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

df_docs = pd.DataFrame(docs)
# Extract title from filename by removing trailing .txt
df_docs['title'] = df_docs['filename'].str.replace(r"\.txt$", "", regex=True)
# Detect ACM source: look for 'acm' in text, and ensure not IEEE or PubMed
df_docs['is_acm'] = df_docs['text'].str.contains(r'\bacm\b', case=False, na=False)
# Also prefer detection via 'copyright' lines mentioning ACM
df_docs['copyright_acm'] = df_docs['text'].str.contains(r'copyright[^\n]{0,60}acm', case=False, na=False)
# Final flag
df_docs['source_acm'] = df_docs['is_acm'] | df_docs['copyright_acm']

# Merge citations with docs on title
merged = pd.merge(df_cit, df_docs[['title','source_acm']], on='title', how='left')
# Filter where source_acm is True
acm_merged = merged[merged['source_acm'] == True]

# Compute average citation count
if len(acm_merged) == 0:
    result = {"average_citation_count": None, "counted_papers": 0}
else:
    avg = acm_merged['citation_count'].dropna().mean()
    # Round to 4 decimal places
    avg = float(round(avg, 4))
    result = {"average_citation_count": avg, "counted_papers": int(len(acm_merged))}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WpgIHC8Y29iZj0n0VkFiYS1J': ['paper_docs'], 'var_call_zfApXxSAJ9X3xevFqVFTJyZ7': ['Citations', 'sqlite_sequence'], 'var_call_FKaO08dCZpqBJ2LEg9OQmRxN': 'file_storage/call_FKaO08dCZpqBJ2LEg9OQmRxN.json', 'var_call_aj5SZDAQkKmoeos4mGeb2lF9': 'file_storage/call_aj5SZDAQkKmoeos4mGeb2lF9.json'}

exec(code, env_args)
