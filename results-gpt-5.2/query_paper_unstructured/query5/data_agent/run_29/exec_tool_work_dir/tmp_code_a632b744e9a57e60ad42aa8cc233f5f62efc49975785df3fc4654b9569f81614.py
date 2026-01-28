code = """import json, re
import pandas as pd

cit_path = var_call_8ufMzYknab8QDmC0Z2TqTnT0
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
# handle possible column names
if 'title' not in df_cit.columns and 'Title' in df_cit.columns:
    df_cit = df_cit.rename(columns={'Title':'title'})
if 'citation_count' not in df_cit.columns and 'CitationCount' in df_cit.columns:
    df_cit = df_cit.rename(columns={'CitationCount':'citation_count'})

if df_cit.empty or 'title' not in df_cit.columns:
    df_cit = pd.DataFrame(columns=['title','citation_count'])

df_cit['title'] = df_cit['title'].astype(str)
df_cit['citation_count'] = pd.to_numeric(df_cit.get('citation_count',0), errors='coerce').fillna(0).astype(int)
df_cit['title_norm'] = df_cit['title'].str.strip().str.lower()

# docs

docs_path = var_call_FVCPNN19AGNcWgpEAVWtrgnN
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)
if df_docs.empty:
    out = {"total_citations": 0, "paper_count": 0, "per_paper": []}
else:
    if 'filename' not in df_docs.columns:
        df_docs['filename'] = ''
    if 'text' not in df_docs.columns:
        df_docs['text'] = ''
    df_docs['title'] = df_docs['filename'].astype(str).str.replace(r'\.txt$', '', regex=True)
    df_docs['title_norm'] = df_docs['title'].str.strip().str.lower()

    def is_chi(t):
        if not isinstance(t, str):
            return False
        tt = t.lower()
        if 'ozchi' in tt:
            return False
        pats = [r"\bchi\b", r"chi '\d{2}", r"chi\s+\d{4}", r"acm\s+chi"]
        return any(re.search(p, tt) for p in pats)

    df_docs['is_chi'] = df_docs['text'].apply(is_chi)
    df_chi = df_docs[df_docs['is_chi']][['title','title_norm']].drop_duplicates('title_norm')

    df_join = df_cit.merge(df_chi, on='title_norm', how='inner')
    total = int(df_join['citation_count'].sum())
    paper_count = int(df_join['title_norm'].nunique())

    per = (df_join.groupby('title_y', as_index=False)['citation_count'].sum()
           .rename(columns={'title_y':'title'})
           .sort_values(['citation_count','title'], ascending=[False, True]))

    out = {"total_citations": total, "paper_count": paper_count, "per_paper": per.to_dict(orient='records')}

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_8ufMzYknab8QDmC0Z2TqTnT0': 'file_storage/call_8ufMzYknab8QDmC0Z2TqTnT0.json', 'var_call_FVCPNN19AGNcWgpEAVWtrgnN': 'file_storage/call_FVCPNN19AGNcWgpEAVWtrgnN.json'}

exec(code, env_args)
