code = """import json, re, pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str) and maybe_path_or_list.endswith('.json'):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

paper_docs = load_records(var_call_hfb4VGkl2mhqkZODBZsoBbmd)
citations = load_records(var_call_CiBrTfUMshjlNWKzKjzshVKG)

def extract_year(text):
    if not text:
        return None
    t = text[:5000]
    m = re.search(r'Copyright\s*(?:\(c\))?\s*(\d{4})', t, re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(19\d{2}|20\d{2})\b", t)
    if m:
        return int(m.group(1))
    return None

def has_empirical(text):
    return bool(text) and ('empirical' in text.lower())

papers = []
for d in paper_docs:
    fn = d.get('filename','')
    title = fn[:-4] if isinstance(fn,str) and fn.lower().endswith('.txt') else fn
    year = extract_year(d.get('text',''))
    papers.append({'title': str(title) if title is not None else None, 'year': year, 'empirical': has_empirical(d.get('text',''))})

papers_df = pd.DataFrame(papers)
papers_df = papers_df.dropna(subset=['title'])
filtered_titles = set(papers_df[(papers_df['empirical']==True) & (papers_df['year'].fillna(0).astype(int) > 2016)]['title'].astype(str).tolist())

cit_df = pd.DataFrame(citations)
if 'title' in cit_df.columns:
    cit_df['title'] = cit_df['title'].astype(str)
for c in ['citation_count','citation_year']:
    if c in cit_df.columns:
        cit_df[c] = pd.to_numeric(cit_df[c], errors='coerce')

cit_sum = (cit_df[cit_df['title'].isin(filtered_titles)]
           .groupby('title', as_index=False)['citation_count'].sum(min_count=1)
           .rename(columns={'citation_count':'total_citation_count'}))

out_df = pd.DataFrame({'title': sorted(filtered_titles)})
out_df['title'] = out_df['title'].astype(str)
out_df = out_df.merge(cit_sum, on='title', how='left')
out_df['total_citation_count'] = pd.to_numeric(out_df['total_citation_count'], errors='coerce').fillna(0).astype(int)

out_df = out_df.sort_values(['total_citation_count','title'], ascending=[False, True])
result = out_df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hfb4VGkl2mhqkZODBZsoBbmd': 'file_storage/call_hfb4VGkl2mhqkZODBZsoBbmd.json', 'var_call_CiBrTfUMshjlNWKzKjzshVKG': 'file_storage/call_CiBrTfUMshjlNWKzKjzshVKG.json'}

exec(code, env_args)
