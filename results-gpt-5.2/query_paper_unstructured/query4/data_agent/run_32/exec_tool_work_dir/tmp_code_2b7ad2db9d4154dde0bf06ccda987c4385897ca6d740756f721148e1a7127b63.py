code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

paper_docs = load_records(var_call_ATj1On1VLUKNZPVuntP4HGjH)
citations = load_records(var_call_VwIPiu5hID8S04slRvYGUT72)

# Build (title -> domain/year) by parsing text for year and domain.
# Year: first 4-digit year between 2000-2026 that appears near top; fallback: any.

def extract_year(text):
    head = text[:3000]
    yrs = re.findall(r'\b(20\d{2})\b', head)
    if not yrs:
        yrs = re.findall(r'\b(19\d{2}|20\d{2})\b', head)
    if not yrs:
        return None
    # prefer 2016 if present else first occurrence
    for y in yrs:
        if y == '2016':
            return 2016
    return int(yrs[0])

def is_physical_activity_domain(text):
    head = text[:6000].lower()
    return ('physical activity' in head) or ('physical-activity' in head)

rows = []
for d in paper_docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text') or ''
    year = extract_year(text)
    if year == 2016 and is_physical_activity_domain(text):
        rows.append({'title': title})

papers2016_pa = pd.DataFrame(rows).drop_duplicates()

cit_df = pd.DataFrame(citations)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# total citations across all citation years
if papers2016_pa.empty:
    out = []
else:
    merged = cit_df.merge(papers2016_pa, on='title', how='inner')
    out_df = merged.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citation_count'})
    out_df = out_df.sort_values(['total_citation_count','title'], ascending=[False, True])
    out = out_df.to_dict('records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_ATj1On1VLUKNZPVuntP4HGjH': 'file_storage/call_ATj1On1VLUKNZPVuntP4HGjH.json', 'var_call_VwIPiu5hID8S04slRvYGUT72': 'file_storage/call_VwIPiu5hID8S04slRvYGUT72.json'}

exec(code, env_args)
