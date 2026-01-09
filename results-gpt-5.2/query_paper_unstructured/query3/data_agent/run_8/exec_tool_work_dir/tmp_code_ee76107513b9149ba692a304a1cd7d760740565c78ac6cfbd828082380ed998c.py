code = """import json, re
import pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

papers = load_json_maybe(var_call_4VYaIeVEDqzm0Z0t4SP4ttKp)
citations = load_json_maybe(var_call_TWhcQoF9rfbZrwClgmm2gLiO)

# Extract year and contribution from text.
# year: first plausible 4-digit year between 1990 and 2026
# contribution: contains 'empirical' (case-insensitive)
rows = []
for d in papers:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    tlow = text.lower()
    if 'empirical' not in tlow:
        continue
    # Find publication year: look for patterns like "'15" with venue? safer: use 4-digit year occurrences
    years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', text)]
    pub_year = None
    if years:
        # choose earliest year as publication year heuristic
        pub_year = min(years)
    if pub_year is None or pub_year <= 2016:
        continue
    rows.append({'title': title, 'pub_year': pub_year})

papers_df = pd.DataFrame(rows).drop_duplicates('title')

cit_df = pd.DataFrame(citations)
if not cit_df.empty:
    # ensure numeric
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce')

out = papers_df.merge(cit_df, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_O05e4rUsZ2q39PV166J8Xky7': 'file_storage/call_O05e4rUsZ2q39PV166J8Xky7.json', 'var_call_TWhcQoF9rfbZrwClgmm2gLiO': 'file_storage/call_TWhcQoF9rfbZrwClgmm2gLiO.json', 'var_call_4VYaIeVEDqzm0Z0t4SP4ttKp': 'file_storage/call_4VYaIeVEDqzm0Z0t4SP4ttKp.json'}

exec(code, env_args)
