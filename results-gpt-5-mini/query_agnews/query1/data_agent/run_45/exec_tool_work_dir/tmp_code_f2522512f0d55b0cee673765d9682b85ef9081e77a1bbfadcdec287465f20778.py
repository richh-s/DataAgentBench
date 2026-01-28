code = """import json
import pandas as pd
import re

with open(var_call_lgxb6TZjxdpNhqMYHh1qGD0s, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df['title'] = df.get('title', '').fillna('').astype(str)
df['description'] = df.get('description', '').fillna('').astype(str)
df['desc_len'] = df['description'].apply(len)

# broader sports keyword set
keywords = ['sport','sports','match','game','team','score','scores','scored','beat','beats','defeat','defeated',
    'win','wins','won','goal','goals','penalty','season','coach','manager','football','soccer',
    'basketball','baseball','cricket','tennis','golf','hockey','racing','race','runner','boxer','boxing','stadium','league','cup','tackle','innings','quarterback','touchdown','players','player','transfer','signed','matchday','pitch','coach','manager','fifa','olympic','olympics','nba','nhl','mlb']
pattern = re.compile(r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b", flags=re.IGNORECASE)

# check for keywords in title or description
matches = []
for _, row in df.iterrows():
    if pattern.search(row['title']) or pattern.search(row['description']):
        matches.append({'title': row['title'], 'desc_len': int(row['desc_len']), 'description_snippet': row['description'][:200]})

# sort matches by desc_len desc
matches_sorted = sorted(matches, key=lambda x: x['desc_len'], reverse=True)
# also include top 200 longest descriptions overall for manual check
top200 = df.sort_values('desc_len', ascending=False).head(200)[['title','desc_len','description']].to_dict(orient='records')

out = {'matches_sorted': matches_sorted, 'top200': top200}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_lgxb6TZjxdpNhqMYHh1qGD0s': 'file_storage/call_lgxb6TZjxdpNhqMYHh1qGD0s.json', 'var_call_4zqdTVXRsE4IbaFKC2DnfeWF': '', 'var_call_S5otKnULYzerPiJYdMjFhgEl': 'file_storage/call_S5otKnULYzerPiJYdMjFhgEl.json'}

exec(code, env_args)
