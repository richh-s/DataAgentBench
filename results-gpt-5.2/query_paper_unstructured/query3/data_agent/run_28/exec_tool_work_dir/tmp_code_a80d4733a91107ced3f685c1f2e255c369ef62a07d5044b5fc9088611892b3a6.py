code = """import json, re
import pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str) and maybe_path_or_list.endswith('.json'):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

paper_files = load_records(var_call_1cVWmlDMFMLcNBcLUhnC4mlr)
cite_totals = load_records(var_call_JvjOEqhF8vLiTvYXX3H0KRnm)

# candidate titles from filenames
filenames = [r.get('filename','') for r in paper_files]
titles = [re.sub(r'\.txt$', '', fn) for fn in filenames if fn]

# Heuristic: empirical if title contains keywords
empirical_keywords = re.compile(r'\\b(empirical|study|studies|trial|evaluation|field trial|experiment|survey|qualitative|quantitative)\\b', re.IGNORECASE)
empirical_titles = {t for t in titles if empirical_keywords.search(t)}

# publication year: heuristic from title containing 4-digit year, else unknown -> exclude
year_re = re.compile(r'(19|20)\\d{2}')

title_year = {}
for t in titles:
    m = year_re.search(t)
    if m:
        y = int(m.group(0))
        title_year[t] = y

# Filter after 2016
post2016 = {t for t,y in title_year.items() if y > 2016}
filtered_titles = empirical_titles & post2016

# join with citation totals
ct_df = pd.DataFrame(cite_totals)
if not ct_df.empty:
    ct_df['total_citations'] = pd.to_numeric(ct_df['total_citations'], errors='coerce').fillna(0).astype(int)

res_df = ct_df[ct_df['title'].isin(filtered_titles)].copy() if not ct_df.empty else pd.DataFrame(columns=['title','total_citations'])
res_df = res_df.sort_values(['total_citations','title'], ascending=[False, True])
result = res_df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_1cVWmlDMFMLcNBcLUhnC4mlr': 'file_storage/call_1cVWmlDMFMLcNBcLUhnC4mlr.json', 'var_call_JvjOEqhF8vLiTvYXX3H0KRnm': 'file_storage/call_JvjOEqhF8vLiTvYXX3H0KRnm.json'}

exec(code, env_args)
