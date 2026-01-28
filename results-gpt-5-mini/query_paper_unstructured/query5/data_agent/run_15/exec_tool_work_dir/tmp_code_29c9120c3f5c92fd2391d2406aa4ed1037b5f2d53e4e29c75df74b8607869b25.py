code = """import pandas as pd
import json
import re

# Load the query results from storage-provided file paths
# var_call_whUnnBK7V9wrv6dMJuAdPQQM and var_call_Tf8URzJH7O9L9sSBRBQgkBDj are available

df_citations = pd.read_json(var_call_whUnnBK7V9wrv6dMJuAdPQQM)
# convert citation_count to int
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'], errors='coerce').fillna(0).astype(int)

df_docs = pd.read_json(var_call_Tf8URzJH7O9L9sSBRBQgkBDj)
# extract title from filename
df_docs['title'] = df_docs['filename'].str.replace('.txt','', regex=False)

# function to detect CHI in the header of the paper text
pattern = re.compile(r'\bCHI\b', re.IGNORECASE)

def is_chi(text):
    if not isinstance(text, str):
        return False
    head = text[:1000]  # look at the beginning of the document where venue is typically listed
    return bool(pattern.search(head))

df_docs['is_chi'] = df_docs['text'].apply(is_chi)

# Merge citations (which are for 2020) with docs on title
merged = pd.merge(df_citations, df_docs[['title','is_chi']], on='title', how='left')
# keep only those identified as CHI
chi_cited = merged[merged['is_chi'] == True].copy()

# Prepare output
chi_cited['citation_count'] = chi_cited['citation_count'].astype(int)
papers = chi_cited[['title','citation_count']].to_dict(orient='records')
total = int(chi_cited['citation_count'].sum())
num = len(papers)

result = {'num_papers': num, 'total_citations_2020': total, 'papers': papers}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_whUnnBK7V9wrv6dMJuAdPQQM': 'file_storage/call_whUnnBK7V9wrv6dMJuAdPQQM.json', 'var_call_Tf8URzJH7O9L9sSBRBQgkBDj': 'file_storage/call_Tf8URzJH7O9L9sSBRBQgkBDj.json'}

exec(code, env_args)
