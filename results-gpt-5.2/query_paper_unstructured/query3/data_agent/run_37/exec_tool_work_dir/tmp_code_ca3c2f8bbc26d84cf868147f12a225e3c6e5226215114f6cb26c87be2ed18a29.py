code = """import json, re
import pandas as pd

def load_maybe_path(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

papers = load_maybe_path(var_call_GtgKEVGcc6MSdjZ1O8ktHOLH)
cits = load_maybe_path(var_call_jX8SKFLhLCXYZzxdA1lokhv1)

cdf = pd.DataFrame(cits)
for col in ['citation_count','citation_year']:
    if col in cdf.columns:
        cdf[col] = pd.to_numeric(cdf[col], errors='coerce')

total_cites = cdf.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citation_count'})


def extract_year(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'Copyright\s*(?:\(c\))?\s*(\d{4})', text, re.IGNORECASE)
    if m:
        y = int(m.group(1))
        if 1990 <= y <= 2026:
            return y
    years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', text)]
    years = [y for y in years if 1990 <= y <= 2026]
    return years[0] if years else None

def is_empirical(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    if re.search(r'\bcontribution\b[^\r\n]{0,120}\bempirical\b', t):
        return True
    if re.search(r'\btype\s*of\s*contribution\b[^\r\n]{0,120}\bempirical\b', t):
        return True
    return 'empirical' in t

rows = []
for d in papers:
    fn = d.get('filename','')
    title = fn[:-4] if isinstance(fn, str) and fn.lower().endswith('.txt') else fn
    text = d.get('text','')
    year = extract_year(text)
    emp = is_empirical(text)
    rows.append({'title': title, 'year': year, 'empirical': emp})

pdf = pd.DataFrame(rows)

fdf = pdf[(pdf['empirical'] == True) & (pdf['year'].notna()) & (pdf['year'] > 2016)].copy()

out = fdf.merge(total_cites, on='title', how='left')
out['total_citation_count'] = out['total_citation_count'].fillna(0).astype(int)

out = out[['title','total_citation_count']].sort_values(['total_citation_count','title'], ascending=[False, True])
result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_GtgKEVGcc6MSdjZ1O8ktHOLH': 'file_storage/call_GtgKEVGcc6MSdjZ1O8ktHOLH.json', 'var_call_jX8SKFLhLCXYZzxdA1lokhv1': 'file_storage/call_jX8SKFLhLCXYZzxdA1lokhv1.json'}

exec(code, env_args)
