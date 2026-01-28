code = """import json, re, pandas as pd

paper_docs_src = var_call_Yss6Wnn1UF3XRRgAYOB70NTl
if isinstance(paper_docs_src, str):
    with open(paper_docs_src, 'r', encoding='utf-8') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_src

cit_src = var_call_N8qbMFjAFrQmjkDZbq0h3htT
if isinstance(cit_src, str):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cit_rows = json.load(f)
else:
    cit_rows = cit_src

cit_df = pd.DataFrame(cit_rows)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)
    cit_agg = cit_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
else:
    cit_agg = pd.DataFrame(columns=['title','total_citations'])

year_pat = re.compile(r'\b(20\d{2}|19\d{2})\b')


def extract_year(text: str):
    if not text:
        return None
    m = re.search(r"\b(?:CHI|CSCW|UbiComp|UBICOMP|DIS|IUI|WWW|TEI|OzCHI|AH|PervasiveHealth)\s*'\s*(\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy < 50 else 1900 + yy
    m = re.search(r'Copyright\s+(20\d{2}|19\d{2})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    head = text[:2000]
    years = [int(y) for y in year_pat.findall(head)]
    years = [y for y in years if 1980 <= y <= 2026]
    if years:
        return min(years)
    return None


def is_empirical(text: str) -> bool:
    if not text:
        return False
    if not re.search(r'\bempirical\b', text, flags=re.IGNORECASE):
        return False
    if re.search(r'\bcontribution\b[^\n]{0,80}\bempirical\b', text, flags=re.IGNORECASE):
        return True
    if re.search(r'\bempirical\s+(study|evaluation|investigation|analysis)\b', text, flags=re.IGNORECASE):
        return True
    if re.search(r'\bwe\s+(conduct|present|report)\s+(an|a)\s+empirical\b', text, flags=re.IGNORECASE):
        return True
    if re.search(r'\bempirical\b', text[:3000], flags=re.IGNORECASE):
        return True
    return False

rows = []
for doc in paper_docs:
    fn = doc.get('filename', '')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = doc.get('text', '')
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    if not is_empirical(text):
        continue
    rows.append({'title': title, 'year': year})

papers_df = pd.DataFrame(rows)
if not papers_df.empty:
    papers_df = papers_df.drop_duplicates(subset=['title'])

out_df = papers_df.merge(cit_agg, how='left', on='title') if not papers_df.empty else papers_df
if not out_df.empty:
    out_df['total_citations'] = out_df.get('total_citations', 0)
    out_df['total_citations'] = out_df['total_citations'].fillna(0).astype(int)
    out_df = out_df.sort_values(['total_citations', 'title'], ascending=[False, True])
    result = out_df[['title', 'total_citations']].to_dict(orient='records')
else:
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Yss6Wnn1UF3XRRgAYOB70NTl': 'file_storage/call_Yss6Wnn1UF3XRRgAYOB70NTl.json', 'var_call_N8qbMFjAFrQmjkDZbq0h3htT': 'file_storage/call_N8qbMFjAFrQmjkDZbq0h3htT.json'}

exec(code, env_args)
