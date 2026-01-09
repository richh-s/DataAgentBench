code = """import json, re
import pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_x5wwwcDXJaRoYE6AmARANXjR)
cits = load_json_maybe(var_call_P81XAHXJwSC7swWHXcYOGLoF)

# Build citation totals dict
cit_df = pd.DataFrame(cits)
if not cit_df.empty:
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

# Extract title/year/contribution from docs
rows = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text') or ''
    # year extraction: look for 4-digit year 19xx or 20xx near copyright or venue line.
    years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', text)]
    year = None
    if years:
        # choose earliest plausible publication year to avoid citation years in references
        year = min(years)
        if year < 1990 or year > 2026:
            year = None
    # contribution extraction: substring match for 'empirical'
    is_empirical = bool(re.search(r'\bempirical\b', text, flags=re.IGNORECASE))
    if is_empirical and year is not None and year > 2016:
        rows.append({'title': title, 'year': year})

emp_df = pd.DataFrame(rows).drop_duplicates(subset=['title'])

# Join with citations totals
if emp_df.empty:
    out = []
else:
    merged = emp_df.merge(cit_df, on='title', how='left')
    merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)
    merged = merged.sort_values(['total_citations','title'], ascending=[False, True])
    out = merged[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_KGXx9HgyjWczczwkBHfTR6iw': 'file_storage/call_KGXx9HgyjWczczwkBHfTR6iw.json', 'var_call_P81XAHXJwSC7swWHXcYOGLoF': 'file_storage/call_P81XAHXJwSC7swWHXcYOGLoF.json', 'var_call_x5wwwcDXJaRoYE6AmARANXjR': 'file_storage/call_x5wwwcDXJaRoYE6AmARANXjR.json'}

exec(code, env_args)
