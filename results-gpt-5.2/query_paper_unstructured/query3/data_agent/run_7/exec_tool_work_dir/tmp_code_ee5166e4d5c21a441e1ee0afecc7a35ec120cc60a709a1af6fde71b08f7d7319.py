code = """import json, re, pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str) and maybe_path_or_list.endswith('.json'):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

paper_docs = load_records(var_call_hfb4VGkl2mhqkZODBZsoBbmd)
citations = load_records(var_call_CiBrTfUMshjlNWKzKjzshVKG)

# Build publication year & contribution from paper text
# Heuristic: year from copyright / venue year patterns; contribution: contains 'empirical'

def extract_year(text):
    if not text:
        return None
    t = text[:4000]
    m = re.search(r'Copyright\s*(?:\(c\))?\s*(\d{4})', t, re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(19\d{2}|20\d{2})\b", t)
    if m:
        return int(m.group(1))
    return None

def has_empirical(text):
    if not text:
        return False
    return 'empirical' in text.lower()

papers = []
for d in paper_docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','')
    year = extract_year(text)
    empirical = has_empirical(text)
    papers.append({'title': title, 'year': year, 'empirical': empirical})

papers_df = pd.DataFrame(papers)
filtered_titles = set(papers_df[(papers_df['empirical']==True) & (papers_df['year'].fillna(0).astype(int) > 2016)]['title'].tolist())

cit_df = pd.DataFrame(citations)
# ensure numeric
for c in ['citation_count','citation_year']:
    if c in cit_df.columns:
        cit_df[c] = pd.to_numeric(cit_df[c], errors='coerce')

cit_sum = (cit_df[cit_df['title'].isin(filtered_titles)]
           .groupby('title', as_index=False)['citation_count'].sum()
           .rename(columns={'citation_count':'total_citation_count'}))

# If some titles have no citations, include with 0
out_df = pd.DataFrame({'title': sorted(filtered_titles)})
out_df = out_df.merge(cit_sum, on='title', how='left')
out_df['total_citation_count'] = out_df['total_citation_count'].fillna(0).astype(int)

out_df = out_df.sort_values(['total_citation_count','title'], ascending=[False, True])
result = out_df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hfb4VGkl2mhqkZODBZsoBbmd': 'file_storage/call_hfb4VGkl2mhqkZODBZsoBbmd.json', 'var_call_CiBrTfUMshjlNWKzKjzshVKG': 'file_storage/call_CiBrTfUMshjlNWKzKjzshVKG.json'}

exec(code, env_args)
