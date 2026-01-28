code = """import json
import pandas as pd
import re

# Load the query results from storage files
with open(var_call_5IfHIIM0h6rzU2zyc0byMSfC, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_sIniYzyIIrP5IgCIywGocR5U, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Create DataFrames
df_c = pd.DataFrame(citations)
df_p = pd.DataFrame(papers)

# Normalize titles: filename without .txt
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_p['title'] = ''

# Ensure citation counts are integers
if 'total_citations' in df_c.columns:
    df_c['total_citations'] = df_c['total_citations'].astype(int)
else:
    df_c['total_citations'] = 0

# Merge on title
df = pd.merge(df_p[['title','text']], df_c, on='title', how='inner')

# Identify papers in the 'food' domain by searching for the word 'food' in title or text (case-insensitive)
mask_text = df['text'].str.contains(r'\bfood\b', case=False, na=False)
mask_title = df['title'].str.contains('food', case=False, na=False)
mask = mask_text | mask_title

df_food = df[mask].copy()

# Compute total citations
total_citations = int(df_food['total_citations'].sum())
num_papers = int(len(df_food))

# Prepare result JSON
result_obj = {
    'total_citations': total_citations,
    'num_papers': num_papers
}

import json
print("__RESULT__:")
print(json.dumps(result_obj))"""

env_args = {'var_call_6FBgCCK9yWQgJp2K6muXwuWF': ['paper_docs'], 'var_call_5IfHIIM0h6rzU2zyc0byMSfC': 'file_storage/call_5IfHIIM0h6rzU2zyc0byMSfC.json', 'var_call_sIniYzyIIrP5IgCIywGocR5U': 'file_storage/call_sIniYzyIIrP5IgCIywGocR5U.json'}

exec(code, env_args)
