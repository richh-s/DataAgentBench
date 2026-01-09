code = """import json, re
import pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

papers = load_json_maybe(var_call_TKa1wkmAxqzK37wE95iGNxYN)
cits = load_json_maybe(var_call_xjq8D95fmG3jusx8JnpRuMYn)

def extract_year(text):
    candidates = re.findall(r'\b(20\d{2})\b', text)
    years = [int(y) for y in candidates if 2010 <= int(y) <= 2026]
    if not years:
        return None
    return min(years)

def has_empirical(text):
    t = (text or '').lower()
    if re.search(r'\bcontribution\b[^\n]{0,120}\bempirical\b', t):
        return True
    if re.search(r'\b(empirical|user study|field study|participants|interview(s)?|survey(ed)?|experiment(al)?)\b', t):
        return True
    return False

rows = []
for d in papers:
    fn = d.get('filename','') or ''
    if not fn.endswith('.txt'):
        continue
    title = fn[:-4]
    text = d.get('text','')
    year = extract_year(text)
    empirical = has_empirical(text)
    if (year is not None) and (year > 2016) and empirical:
        rows.append({'title': title, 'year': year})

paper_df = pd.DataFrame(rows)
if not paper_df.empty:
    paper_df = paper_df.drop_duplicates('title')

cit_df = pd.DataFrame(cits)
if not cit_df.empty and 'total_citations' in cit_df.columns:
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce')

if paper_df.empty:
    result = []
else:
    out = paper_df.merge(cit_df, on='title', how='left')
    out['total_citations'] = out['total_citations'].fillna(0).astype(int)
    out = out.sort_values(['total_citations','title'], ascending=[False, True])
    result = out[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_TKa1wkmAxqzK37wE95iGNxYN': 'file_storage/call_TKa1wkmAxqzK37wE95iGNxYN.json', 'var_call_xjq8D95fmG3jusx8JnpRuMYn': 'file_storage/call_xjq8D95fmG3jusx8JnpRuMYn.json'}

exec(code, env_args)
