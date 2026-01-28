code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

paper_docs = load_json_maybe(var_call_RQr6sgJDKSsXyiZn0SyNMtes)
cits = load_json_maybe(var_call_eLqvkLk7LoIBpC6gQvVZELHV)

# Build metadata from documents: title from filename; year from text patterns
rows = []
for d in paper_docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','', fn).strip()
    text = d.get('text','') or ''
    # year: prefer explicit copyright year, else first 4-digit year in plausible range
    m = re.search(r'Copyright\s*(?:\(c\))?\s*(\d{4})', text, flags=re.IGNORECASE)
    year = int(m.group(1)) if m else None
    if year is None:
        years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', text)]
        years = [y for y in years if 2000 <= y <= 2026]
        year = years[0] if years else None
    # domain: contains 'physical activity' anywhere
    domain_pa = bool(re.search(r'physical\s+activity', text, flags=re.IGNORECASE))
    rows.append({'title': title, 'pub_year': year, 'is_physical_activity': domain_pa})

meta = pd.DataFrame(rows)
meta_2016_pa = meta[(meta['pub_year']==2016) & (meta['is_physical_activity'])][['title']].drop_duplicates()

cits_df = pd.DataFrame(cits)
# Ensure numeric
cits_df['citation_count'] = pd.to_numeric(cits_df['citation_count'], errors='coerce').fillna(0).astype(int)

# Total citations across all citation years
cits_tot = cits_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})

out = meta_2016_pa.merge(cits_tot, on='title', how='left').fillna({'total_citations':0})
out['total_citations'] = out['total_citations'].astype(int)

out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_RQr6sgJDKSsXyiZn0SyNMtes': 'file_storage/call_RQr6sgJDKSsXyiZn0SyNMtes.json', 'var_call_eLqvkLk7LoIBpC6gQvVZELHV': 'file_storage/call_eLqvkLk7LoIBpC6gQvVZELHV.json'}

exec(code, env_args)
