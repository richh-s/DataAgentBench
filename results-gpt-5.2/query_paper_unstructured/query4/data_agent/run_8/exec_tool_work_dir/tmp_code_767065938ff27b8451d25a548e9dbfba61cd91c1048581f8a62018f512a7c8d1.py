code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

paper_docs = load_records(var_call_VFUqW3NcfYU91ZUHkCjZsNhU)
cit_rows = load_records(var_call_TQJvW4s8V8TvJmUc6cDJ8GXt)

# Heuristics for extraction

def extract_year(text):
    head = text[:2500]
    m = re.search(r"\b(20\d{2})\b", head)
    if m:
        return int(m.group(1))
    m2 = re.search(r"\b(?:CHI|CSCW|UbiComp|UBICOMP|DIS|IUI|WWW|TEI|AH|OzCHI)\s*['’](\d{2})\b", head, re.IGNORECASE)
    if m2:
        return 2000 + int(m2.group(1))
    return None

def has_physical_activity_domain(text):
    if re.search(r"(?i)domain\s*:\s*[^\n]*physical activity", text):
        return True
    if re.search(r"(?i)author keywords[\s\S]{0,800}?physical activity", text):
        return True
    if len(re.findall(r"(?i)physical activity", text)) >= 2:
        return True
    return False

papers = []
for d in paper_docs:
    fn = d.get('filename', '') or ''
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text', '') or ''
    if not has_physical_activity_domain(text):
        continue
    year = extract_year(text)
    if year != 2016:
        continue
    papers.append({'title': title})

papers_df = pd.DataFrame(papers).drop_duplicates()

cit_df = pd.DataFrame(cit_rows)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

if papers_df.empty or cit_df.empty:
    out = []
else:
    merged = papers_df.merge(cit_df, on='title', how='left')
    agg = merged.groupby('title', as_index=False)['citation_count'].sum()
    agg = agg.rename(columns={'citation_count': 'total_citations'})
    out = agg.sort_values(['total_citations', 'title'], ascending=[False, True]).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_TQJvW4s8V8TvJmUc6cDJ8GXt': 'file_storage/call_TQJvW4s8V8TvJmUc6cDJ8GXt.json', 'var_call_VFUqW3NcfYU91ZUHkCjZsNhU': 'file_storage/call_VFUqW3NcfYU91ZUHkCjZsNhU.json'}

exec(code, env_args)
