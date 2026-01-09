code = """import json, re, pandas as pd

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str) and maybe_path_or_records.endswith('.json'):
        with open(maybe_path_or_records, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_records

paper_docs = load_records(var_call_mBK8SL48jLDFIViERIHVoenr)
cit = load_records(var_call_IvguE1JaoeiLaX7DpRidbR7M)

# Build citations df
cit_df = pd.DataFrame(cit)
if not cit_df.empty:
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

# Extract year and contribution from paper docs
rows = []
for d in paper_docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    low = text.lower()

    # year: try explicit Copyright YEAR, then venue header like CHI '18
    year = None
    m = re.search(r'copyright\s*(?:\(c\)\s*)?(\d{4})', text, flags=re.IGNORECASE)
    if m:
        year = int(m.group(1))
    else:
        m = re.search(r"\b(?:chi|ubicomp|cscw|dis|iui|www|ozchi|tei|ah)\s*['’](\d{2})\b", text, flags=re.IGNORECASE)
        if m:
            yy = int(m.group(1))
            year = 2000 + yy
    # contribution: substring match
    contribution = 'empirical' if 'empirical' in low else None

    if year is not None and contribution is not None:
        rows.append({'title': title, 'year': year, 'contribution': contribution})

papers_df = pd.DataFrame(rows).drop_duplicates(subset=['title'])

# Filter after 2016
papers_df = papers_df[papers_df['year'] > 2016]

# Join citations and aggregate total citations already aggregated
out = papers_df.merge(cit_df, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)

out = out[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True])

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_mBK8SL48jLDFIViERIHVoenr': 'file_storage/call_mBK8SL48jLDFIViERIHVoenr.json', 'var_call_IvguE1JaoeiLaX7DpRidbR7M': 'file_storage/call_IvguE1JaoeiLaX7DpRidbR7M.json'}

exec(code, env_args)
