code = """import json
import pandas as pd
import re

# Load query results from storage files
with open(var_call_qcnVMctHShpOR2enygpenmQX, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_NxzDY71sirjBiE58HbpvSeVl, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Create DataFrames
df_cit = pd.DataFrame(citations)
# ensure citation_count is int
df_cit['citation_count'] = df_cit['citation_count'].astype(int)

# docs: extract title from filename
df_docs = pd.DataFrame(docs)
# Some entries might lack filename; drop those
df_docs = df_docs.dropna(subset=['filename'])
# title matches filename without .txt
df_docs['title'] = df_docs['filename'].str.replace(r"\.txt$", "", regex=True)

# Determine if doc is from CHI by searching for 'CHI' in text (case-insensitive)
def is_chi(text):
    if not isinstance(text, str):
        return False
    # Search for CHI as a word or patterns like "CHI '15" or "CHI 2015"
    if re.search(r"\bCHI\b", text, flags=re.IGNORECASE):
        return True
    if re.search(r"CHI\s*'\d{2}", text):
        return True
    if re.search(r"CHI\s*\d{4}", text):
        return True
    return False

df_docs['is_chi'] = df_docs['text'].apply(is_chi)

# Merge citations with docs on title
merged = pd.merge(df_cit, df_docs[['title', 'is_chi']], on='title', how='left')
# Keep only those with is_chi == True
chi_citations = merged[merged['is_chi'] == True].copy()

# Prepare output: list of papers and their citation counts
papers_list = []
for _, row in chi_citations.iterrows():
    papers_list.append({'title': row['title'], 'citation_count': int(row['citation_count'])})

total_citations = int(chi_citations['citation_count'].sum()) if not chi_citations.empty else 0

output = {'papers': papers_list, 'total_citations': total_citations}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_qcnVMctHShpOR2enygpenmQX': 'file_storage/call_qcnVMctHShpOR2enygpenmQX.json', 'var_call_NfZhd2KOcVnYPEYgnQNdDROs': ['paper_docs'], 'var_call_NxzDY71sirjBiE58HbpvSeVl': 'file_storage/call_NxzDY71sirjBiE58HbpvSeVl.json'}

exec(code, env_args)
