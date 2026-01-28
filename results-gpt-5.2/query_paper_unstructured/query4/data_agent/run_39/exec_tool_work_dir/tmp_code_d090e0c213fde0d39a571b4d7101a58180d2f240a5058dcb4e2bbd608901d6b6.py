code = """import json, re, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

paper_docs = load_maybe_path(var_call_MDgJz3LUtjVI7LEKxT1pAa0W)
ci = load_maybe_path(var_call_Ats84aEU42MEzKH9r5ILjr2K)

# Extract metadata heuristically from text

def extract_year(text):
    # Prefer 2016 if clearly present near header as a standalone year or copyright
    # We'll search for common patterns, returning first plausible year in [2000,2026]
    patterns = [
        r"\b(19|20)\d{2}\b",
    ]
    years = []
    for pat in patterns:
        for m in re.finditer(pat, text):
            y = int(m.group(0))
            if 2000 <= y <= 2026:
                years.append(y)
    if not years:
        return None
    # Often the publication year is the earliest year appearing in the header; use min
    return min(years)

# Domain: use keyword in text (author keywords etc.)

def has_physical_activity(text):
    return re.search(r"physical\s+activity", text, flags=re.IGNORECASE) is not None

rows = []
for d in paper_docs:
    fn = d.get('filename','')
    title = re.sub(r"\.txt$", "", fn)
    text = d.get('text','') or ''
    year = extract_year(text)
    if year == 2016 and has_physical_activity(text):
        rows.append({'title': title, 'year': year})

papers_df = pd.DataFrame(rows).drop_duplicates('title')

cit_df = pd.DataFrame(ci)
if not cit_df.empty:
    # ensure numeric
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# total citations across all citation years
if papers_df.empty:
    out = []
else:
    tot = cit_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
    merged = papers_df.merge(tot, on='title', how='left')
    merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)
    out = merged.sort_values(['total_citations','title'], ascending=[False, True])[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_MDgJz3LUtjVI7LEKxT1pAa0W': 'file_storage/call_MDgJz3LUtjVI7LEKxT1pAa0W.json', 'var_call_Ats84aEU42MEzKH9r5ILjr2K': 'file_storage/call_Ats84aEU42MEzKH9r5ILjr2K.json'}

exec(code, env_args)
