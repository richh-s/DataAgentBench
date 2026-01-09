code = """import json, pandas as pd, re

path = var_call_U4enKV5xnZWlo8VkdOMpKAQj
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for c in ['title','description']:
    df[c] = df[c].astype(str)

df['desc_len'] = df['description'].str.len()

sports_terms = [
    'football','soccer','nba','nfl','mlb','nhl','golf','tennis','cricket','rugby','hockey','baseball','basketball',
    'olympic','olympics','fifa','uefa','champions league','premier league','la liga','serie a','bundesliga',
    'world cup','grand slam','atp','wta','pga','nascar','formula','f1','motogp','boxing','ufc','mma',
    'coach','season','tournament','match','game','playoff','playoffs','championship','league','cup','score','win','lost','defeat'
]
pattern = '(?i)(' + '|'.join([re.escape(t) for t in sports_terms]) + ')'
mask = df['title'].str.contains(pattern, regex=True, na=False) | df['description'].str.contains(pattern, regex=True, na=False)

dfs = df[mask].copy()
row = dfs.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
result = {'title': row['title']}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_U4enKV5xnZWlo8VkdOMpKAQj': 'file_storage/call_U4enKV5xnZWlo8VkdOMpKAQj.json'}

exec(code, env_args)
