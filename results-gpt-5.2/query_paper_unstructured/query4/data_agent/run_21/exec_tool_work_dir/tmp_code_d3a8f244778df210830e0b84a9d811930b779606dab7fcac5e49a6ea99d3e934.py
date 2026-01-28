code = """import json, re, pandas as pd

def load_maybe_path(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

paper_docs = load_maybe_path(var_call_SkUoxCtH1EJd6SMZ87TwXJEe)
citations = load_maybe_path(var_call_QTMBHmsYqppr9yZFz2gLs7un)

# Build paper metadata (title, year, domain) from docs
rows=[]
for d in paper_docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','',fn)
    text = d.get('text','') or ''
    # year: prefer copyright year; else first 4-digit year near top
    year = None
    m = re.search(r'Copyright\s*(?:\u00a9|\(C\))?\s*(\d{4})', text, flags=re.IGNORECASE)
    if m:
        year = int(m.group(1))
    else:
        m2 = re.search(r'\b(20\d{2}|19\d{2})\b', text[:2000])
        if m2:
            year = int(m2.group(1))
    # domain: look for keywords list appearance
    domain = ''
    # Search Author Keywords section line
    mk = re.search(r'Author Keywords\s*(.*?)\n\n', text, flags=re.IGNORECASE|re.DOTALL)
    kw = mk.group(1) if mk else ''
    if 'physical activity' in (kw.lower()):
        domain='physical activity'
    else:
        # fallback: contains in text
        if re.search(r'\bphysical activity\b', text, flags=re.IGNORECASE):
            domain='physical activity'
    if domain=='physical activity' and year==2016:
        rows.append({'title': title, 'year': year, 'domain': domain})

meta_df = pd.DataFrame(rows).drop_duplicates(subset=['title'])

cit_df = pd.DataFrame(citations)
if not cit_df.empty:
    cit_df['citation_count']=pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# total citations across all citation years
if meta_df.empty:
    out=[]
else:
    merged = meta_df.merge(cit_df, on='title', how='left')
    tot = merged.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citation_count'})
    out = tot.sort_values('total_citation_count', ascending=False).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_SkUoxCtH1EJd6SMZ87TwXJEe': 'file_storage/call_SkUoxCtH1EJd6SMZ87TwXJEe.json', 'var_call_QTMBHmsYqppr9yZFz2gLs7un': 'file_storage/call_QTMBHmsYqppr9yZFz2gLs7un.json'}

exec(code, env_args)
