code = """import json, re
import pandas as pd

# Load citations 2018
cit_path = var_call_N9IiqL3UgGToyF2neI9gUaHv
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
# ensure numeric
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load paper docs
docs_path = var_call_dzstTzEJR5AvBTszYbb2xcAl
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$','', regex=True)

# Determine ACM source using text markers
pat = re.compile(r'\bACM\b|Association for Computing Machinery|acm\.org', re.IGNORECASE)
df_docs['is_acm'] = df_docs['text'].apply(lambda t: bool(pat.search(t or '')))

df_acm_titles = df_docs.loc[df_docs['is_acm'], ['title']].drop_duplicates()

# Join with citations 2018
merged = df_cit.merge(df_acm_titles, on='title', how='inner')

avg_cites = float(merged['citation_count'].mean()) if len(merged) else None
result = {
    'average_citation_count_2018_acm_papers': avg_cites,
    'num_acm_papers_with_2018_citations': int(len(merged)),
    'num_total_papers_with_2018_citations': int(len(df_cit))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_N9IiqL3UgGToyF2neI9gUaHv': 'file_storage/call_N9IiqL3UgGToyF2neI9gUaHv.json', 'var_call_dzstTzEJR5AvBTszYbb2xcAl': 'file_storage/call_dzstTzEJR5AvBTszYbb2xcAl.json'}

exec(code, env_args)
