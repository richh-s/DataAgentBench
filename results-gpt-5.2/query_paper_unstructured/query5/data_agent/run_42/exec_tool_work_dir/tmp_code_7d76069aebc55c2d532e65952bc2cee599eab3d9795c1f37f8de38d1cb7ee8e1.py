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

# venue extraction: look for CHI in header-like text
pat = re.compile(r"\bCHI\b", re.IGNORECASE)

def is_chi(text):
    if not isinstance(text, str):
        return False
    head = text[:5000]
    return bool(pat.search(head))

df_p['is_chi'] = df_p['text'].apply(is_chi)

# join and aggregate
chi_titles = set(df_p.loc[df_p['is_chi'], 'title'])
df_chi_cit = df_cit[df_cit['title'].isin(chi_titles)]

total = int(df_chi_cit['citation_count'].sum())

out = json.dumps({
    "total_citations_2020_for_CHI_papers": total,
    "num_chi_papers_with_citations_in_2020": int(df_chi_cit['title'].nunique()),
    "num_citation_records_matched": int(len(df_chi_cit))
})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_hBMNtLT3jpsx8aDxz65hoYIP': 'file_storage/call_hBMNtLT3jpsx8aDxz65hoYIP.json', 'var_call_B7Nd9ZV7ZXGO00IJwzlralmQ': 'file_storage/call_B7Nd9ZV7ZXGO00IJwzlralmQ.json'}

exec(code, env_args)
