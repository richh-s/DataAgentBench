code = """import json
import pandas as pd

path = var_call_SUyFyVRt5bYlDVEPE90EKqG0
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# Ensure strings
for col in ['title','description']:
    df[col] = df[col].fillna('').astype(str)

sports_keywords = [
    'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf',
    'olympic','olympics','fifa','uefa','premier','champions league','world cup','super bowl',
    'playoff','playoffs','season','tournament','coach','quarterback','touchdown','goal','run',
    'home run','grand slam','match','defeat','beats','win','wins','victory','draw','score',
    'cricket','rugby','formula','f1','nascar','motogp','boxing','ufc','mma','wrestling','ski',
    'snowboard','cycling','tour de france','athletics','marathon','sprinter','swimming'
]

def is_sports(row):
    text = (row['title'] + ' ' + row['description']).lower()
    return any(k in text for k in sports_keywords)

sports_df = df[df.apply(is_sports, axis=1)].copy()
sports_df['desc_len'] = sports_df['description'].str.len()

if len(sports_df)==0:
    out = {'title': None}
else:
    top = sports_df.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
    out = {'title': top['title'], 'article_id': top['article_id'], 'description_length': int(top['desc_len'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_SUyFyVRt5bYlDVEPE90EKqG0': 'file_storage/call_SUyFyVRt5bYlDVEPE90EKqG0.json'}

exec(code, env_args)
