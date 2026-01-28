code = """import json, re
import pandas as pd

# Load citations 2020
cit_path = var_call_8ufMzYknab8QDmC0Z2TqTnT0
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
# normalize types
if not df_cit.empty:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)
    df_cit['title_norm'] = df_cit['title'].astype(str).str.strip().str.lower()

# Load paper docs
docs_path = var_call_FVCPNN19AGNcWgpEAVWtrgnN
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)
if df_docs.empty:
    out = {"total_citations": 0, "paper_count": 0}
else:
    df_docs['title'] = df_docs['filename'].astype(str).str.replace(r'\.txt$', '', regex=True)
    df_docs['title_norm'] = df_docs['title'].str.strip().str.lower()

    # Determine venue CHI via text contains patterns
    def is_chi(t):
        if not isinstance(t, str):
            return False
        tt = t.lower()
        # exclude sub-venues when only mention CHI? keep simple: require "chi" token and not "ozchi"
        if 'ozchi' in tt:
            return False
        # common patterns
        pats = [r"\bchi\b", r"chi '\d{2}", r"chi\s+\d{4}", r"acm\s+chi"]
        return any(re.search(p, tt) for p in pats)

    df_docs['is_chi'] = df_docs['text'].apply(is_chi)
    df_chi = df_docs[df_docs['is_chi']][['title','title_norm']].drop_duplicates('title_norm')

    df_join = df_cit.merge(df_chi, on='title_norm', how='inner')
    total = int(df_join['citation_count'].sum())
    paper_count = int(df_join['title_norm'].nunique())

    # Also provide per-paper counts
    per = (df_join.groupby('title', as_index=False)['citation_count'].sum()
           .sort_values(['citation_count','title'], ascending=[False, True]))
    out = {
        "total_citations": total,
        "paper_count": paper_count,
        "per_paper": per.to_dict(orient='records')
    }

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_8ufMzYknab8QDmC0Z2TqTnT0': 'file_storage/call_8ufMzYknab8QDmC0Z2TqTnT0.json', 'var_call_FVCPNN19AGNcWgpEAVWtrgnN': 'file_storage/call_FVCPNN19AGNcWgpEAVWtrgnN.json'}

exec(code, env_args)
