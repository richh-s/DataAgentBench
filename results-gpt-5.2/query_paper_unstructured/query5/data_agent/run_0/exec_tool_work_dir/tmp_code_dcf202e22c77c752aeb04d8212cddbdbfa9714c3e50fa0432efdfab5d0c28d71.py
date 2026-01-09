code = """import json, pandas as pd, re

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

cit2020 = load_json_maybe(var_call_wviFNFF1O9TJpXtDTZNpGVSi)
docs = load_json_maybe(var_call_Ri5qMdBcMHlKEXtcBqOAHWCz)

cit_df = pd.DataFrame(cit2020)
# normalize types
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# Build title->text mapping from docs
# title key is filename without .txt
text_by_title = {}
for d in docs:
    fn = d.get('filename')
    if not fn:
        continue
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if title not in text_by_title:
        text_by_title[title] = d.get('text','') or ''

# Determine if paper is CHI by searching for CHI in header/citation lines
chi_titles = []
pattern = re.compile(r"\bCHI\b", re.IGNORECASE)
for title in cit_df['title'].unique():
    txt = text_by_title.get(title)
    if not txt:
        continue
    head = txt[:4000]
    if pattern.search(head):
        # exclude cases where only references include CHI? hard; keep simple
        chi_titles.append(title)

chi_set = set(chi_titles)
res_df = cit_df[cit_df['title'].isin(chi_set)].copy()

# Aggregate total citations in 2020 per CHI paper (in case multiple rows)
out = (res_df.groupby('title', as_index=False)['citation_count'].sum()
       .sort_values(['citation_count','title'], ascending=[False, True]))

result = {
    'total_chi_papers_cited_in_2020': int(out.shape[0]),
    'total_citations_2020_for_chi_papers': int(out['citation_count'].sum()),
    'per_paper_citation_counts_2020': out.to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_wviFNFF1O9TJpXtDTZNpGVSi': 'file_storage/call_wviFNFF1O9TJpXtDTZNpGVSi.json', 'var_call_Ri5qMdBcMHlKEXtcBqOAHWCz': 'file_storage/call_Ri5qMdBcMHlKEXtcBqOAHWCz.json'}

exec(code, env_args)
