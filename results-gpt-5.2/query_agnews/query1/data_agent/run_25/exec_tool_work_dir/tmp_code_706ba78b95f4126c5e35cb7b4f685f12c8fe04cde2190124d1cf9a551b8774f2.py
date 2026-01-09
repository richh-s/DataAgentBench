code = """import json, pandas as pd

path = var_call_UZA77euCZaH7FCwnBXfE11Oc
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# ensure string
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

df['desc_len'] = df['description'].str.len()
max_len = int(df['desc_len'].max())
# heuristic: sports keywords in title/description
sports_kw = [
    'sport','sports','game','match','season','tournament','league','championship','cup','olympic','nba','nfl','nhl','mlb','soccer','football','basketball','baseball','hockey','tennis','golf','cricket','rugby','fifa','uefa','mls','formula','grand prix','nascar','boxing','mma','ufc','wrestling','coach','team','player','win','won','loss','goal','touchdown','home run','pitcher','quarterback','playoff'
]
pattern = r'(?i)(' + '|'.join([pd.regex.escape(k) if hasattr(pd, 'regex') else k for k in sports_kw]) + r')'
# pandas doesn't have regex.escape; use re
import re
pattern = r'(?i)(' + '|'.join([re.escape(k) for k in sports_kw]) + r')'

sports_df = df[df['title'].str.contains(pattern, regex=True, na=False) | df['description'].str.contains(pattern, regex=True, na=False)].copy()
# among sports, get max desc len
sports_max_len = int(sports_df['desc_len'].max()) if len(sports_df) else None
sports_max_titles = sports_df[sports_df['desc_len']==sports_max_len]['title'].tolist() if sports_max_len is not None else []

out = {
    'sports_max_desc_len': sports_max_len,
    'sports_titles': sports_max_titles[:10],
    'sports_count': int(len(sports_df)),
    'overall_max_desc_len': max_len,
    'overall_max_titles': df[df['desc_len']==max_len]['title'].tolist()[:10]
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_UZA77euCZaH7FCwnBXfE11Oc': 'file_storage/call_UZA77euCZaH7FCwnBXfE11Oc.json'}

exec(code, env_args)
