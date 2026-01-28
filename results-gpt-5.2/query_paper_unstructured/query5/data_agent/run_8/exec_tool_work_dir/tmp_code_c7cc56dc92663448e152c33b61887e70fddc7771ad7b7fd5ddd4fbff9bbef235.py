code = """import json, re
import pandas as pd

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

cit = load_tool_result(var_call_6SRnUnoY4t6iTZB7YrW1ZEce)
docs = load_tool_result(var_call_YSkoPQsxdZcGNMN4D36S0HwZ)

def infer_venue(text):
    t = text.lower()
    # common markers
    if re.search(r"\bchi\s*'?\d{2}\b", t) or 'proceedings of the sigchi conference' in t or 'chi conference on human factors in computing systems' in t or 'chi ' in t and 'sigchi' in t:
        return 'CHI'
    if 'ubicomp' in t:
        return 'Ubicomp'
    if 'cscw' in t:
        return 'CSCW'
    if 'dis ' in t or 'designing interactive systems' in t:
        return 'DIS'
    if 'pervasivehealth' in t:
        return 'PervasiveHealth'
    if 'www ' in t:
        return 'WWW'
    if 'iui' in t:
        return 'IUI'
    if 'ozchi' in t:
        return 'OzCHI'
    if 'tei' in t:
        return 'TEI'
    if 'ah ' in t or 'augmented human' in t:
        return 'AH'
    return None

# build title->venue map
venue_by_title = {}
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    v = infer_venue(d.get('text','') or '')
    if v:
        venue_by_title[title] = v

cit_df = pd.DataFrame(cit)
# ensure int
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

cit_df['venue'] = cit_df['title'].map(venue_by_title)
chi_df = cit_df[cit_df['venue'].eq('CHI')]

result = {
    'citation_year': 2020,
    'venue': 'CHI',
    'total_citations': int(chi_df['citation_count'].sum()),
    'num_papers': int(chi_df.shape[0])
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_6SRnUnoY4t6iTZB7YrW1ZEce': 'file_storage/call_6SRnUnoY4t6iTZB7YrW1ZEce.json', 'var_call_YSkoPQsxdZcGNMN4D36S0HwZ': 'file_storage/call_YSkoPQsxdZcGNMN4D36S0HwZ.json'}

exec(code, env_args)
