code = """import json, re, pandas as pd

# load citations 2020
cit_path = var_call_hBMNtLT3jpsx8aDxz65hoYIP
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# load paper docs
papers_path = var_call_B7Nd9ZV7ZXGO00IJwzlralmQ
with open(papers_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)
df_p = pd.DataFrame(papers)
df_p['title'] = df_p['filename'].str.replace(r'\.txt$','', regex=True)

# detect CHI by 'CHI <year>' or 'CHI\s*\d{4}' etc in first 8000 chars
pat = re.compile(r"\bCHI\s*(?:Conference)?\s*(?:on)?\s*(?:Human\s+Factors\s+in\s+Computing\s+Systems)?\s*(?:Proceedings)?\s*\(?CHI\s*\d{4}\)?|\bCHI\s*\d{4}\b", re.IGNORECASE)

def is_chi(text):
    if not isinstance(text, str):
        return False
    head = text[:8000]
    return bool(pat.search(head))

df_p['is_chi'] = df_p['text'].apply(is_chi)

chi_titles = set(df_p.loc[df_p['is_chi'], 'title'])
df_chi_cit = df_cit[df_cit['title'].isin(chi_titles)]

out = {
    "total_citations_2020_for_CHI_papers": int(df_chi_cit['citation_count'].sum()),
    "num_chi_papers_with_citations_in_2020": int(df_chi_cit['title'].nunique()),
    "num_chi_papers_in_docs": int(df_p['is_chi'].sum())
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_hBMNtLT3jpsx8aDxz65hoYIP': 'file_storage/call_hBMNtLT3jpsx8aDxz65hoYIP.json', 'var_call_B7Nd9ZV7ZXGO00IJwzlralmQ': 'file_storage/call_B7Nd9ZV7ZXGO00IJwzlralmQ.json', 'var_call_dDvhD8Tl8825uM3qly4gYxpH': {'total_citations_2020_for_CHI_papers': 0, 'num_chi_papers_with_citations_in_2020': 0, 'num_citation_records_matched': 0}, 'var_call_UewTKYCOPDUwqVlGsi9JL9zk': 'file_storage/call_UewTKYCOPDUwqVlGsi9JL9zk.json'}

exec(code, env_args)
